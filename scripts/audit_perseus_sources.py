#!/usr/bin/env python3
"""audit_perseus_sources.py --- survey Perseus source availability for the corpus.

For each pending entry in meta/works.yaml, classify the latin-source
state so future Cowork sessions can plan around known gaps:

  ok               - Latin file already fetched and is real content
  placeholder      - Latin file present but is a `% PLACEHOLDER` stub
  unfetched-ok     - no Latin file yet; speech_index resolves in Perseus
                     TEI (verified by scanning the TEI for the textpart)
  unfetched-missing - no Latin file yet AND the requested textpart is
                     NOT in the Perseus TEI (e.g. numbering anomaly)
  no-perseus       - no Perseus URL at all; needs manual sourcing
  no-pending-fetch  - already drafted, ignored

The script fetches each Perseus book-level TEI file ONCE (not per
letter) and scans for `<div n="N">` to determine which textparts exist.
It caches book files in /tmp to avoid re-fetching.

Output: a markdown report at meta/perseus-audit.md, plus a JSON
machine-readable summary at meta/perseus-audit.json.

Usage:
    python scripts/audit_perseus_sources.py [--out PATH] [--no-fetch]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKS_YAML = REPO_ROOT / "meta" / "works.yaml"
DEFAULT_REPORT = REPO_ROOT / "meta" / "perseus-audit.md"
DEFAULT_JSON = REPO_ROOT / "meta" / "perseus-audit.json"
CACHE_DIR = Path("/tmp") / "cicero-perseus-cache"

SPEECH_INDEX_RE = re.compile(r"book:\s*(\d+)\s*,\s*letter:\s*(\d+)")
# Match a <div ...> tag with type="textpart". We then pull subtype= and n=
# from inside the tag independently of attribute order.
TEI_DIV_OPEN_RE = re.compile(
    r'<div\b[^>]*\btype="textpart"[^>]*>',
    re.IGNORECASE,
)
ATTR_SUBTYPE_RE = re.compile(r'\bsubtype="(book|letter|section)"', re.IGNORECASE)
ATTR_N_RE = re.compile(r'\bn="([^"]+)"')


def fetch_tei(url: str, timeout: int = 30) -> str | None:
    """Fetch a Perseus TEI URL, with on-disk cache. Returns None on failure."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    safe = urllib.parse.quote_plus(url)
    cache_path = CACHE_DIR / safe
    if cache_path.exists() and cache_path.stat().st_size > 0:
        return cache_path.read_text(encoding="utf-8", errors="replace")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "cicero-audit/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8", errors="replace")
        cache_path.write_text(data, encoding="utf-8")
        return data
    except Exception as e:  # noqa: BLE001
        print(f"  [warn] fetch failed {url}: {e}", file=sys.stderr)
        return None


def index_perseus_tei(text: str) -> dict[str, set[str]]:
    """Index a Perseus TEI document by book and the letters it contains.

    Returns {book_n: {letter_n, ...}}.

    The Perseus TEI uses `<div type="textpart" n="N" subtype="...">` with
    subtype in {book, letter, section}. Attribute order isn't fixed in
    the Perseus serialization, so we extract attributes independently.

    For speech-corpus files, there is no book/letter structure --- only
    sections. Those return an empty mapping (the caller treats no-books
    as "always present" since speeches are addressed by section anyway).
    """
    by_book: dict[str, set[str]] = defaultdict(set)
    current_book: str | None = None
    for m in TEI_DIV_OPEN_RE.finditer(text):
        tag = m.group(0)
        sub_m = ATTR_SUBTYPE_RE.search(tag)
        n_m = ATTR_N_RE.search(tag)
        if not sub_m or not n_m:
            continue
        subtype = sub_m.group(1).lower()
        n = n_m.group(1)
        if subtype == "book":
            current_book = n
        elif subtype == "letter":
            book_key = current_book if current_book is not None else "1"
            by_book[book_key].add(n)
    return by_book


def classify_entry(
    entry: dict,
    tei_indexes: dict[str, dict[str, set[str]]],
    do_fetch: bool,
) -> tuple[str, str]:
    """Return (category, detail). Categories listed in module docstring."""
    work_id = entry.get("id", "<no-id>")
    status = entry.get("status", "pending")
    if status not in ("pending",):
        return ("no-pending-fetch", f"status={status}")

    latin_file_rel = entry.get("latin_file")
    if latin_file_rel:
        latin_path = REPO_ROOT / latin_file_rel
        if latin_path.exists():
            try:
                head = latin_path.read_text(encoding="utf-8")[:2000]
            except Exception:  # noqa: BLE001
                head = ""
            if "% PLACEHOLDER" in head:
                return ("placeholder", latin_file_rel)
            return ("ok", latin_file_rel)

    psrc = entry.get("latin_source_url") or ""
    if not psrc:
        return ("no-perseus", "no latin_source_url")

    if not do_fetch:
        return ("unfetched-unverified", psrc)

    idx = tei_indexes.get(psrc)
    if idx is None:
        text = fetch_tei(psrc)
        if text is None:
            return ("unfetched-missing", f"fetch failed: {psrc}")
        idx = index_perseus_tei(text)
        tei_indexes[psrc] = idx

    speech_index = entry.get("speech_index") or ""
    m = SPEECH_INDEX_RE.search(speech_index)
    if not m:
        # A speech with section-only index (e.g. `5` for Philippic 5):
        # the TEI for speeches has only section divs, so if the TEI
        # fetched OK we consider it present.
        if idx is not None:
            return ("unfetched-ok",
                    f"speech, no book/letter structure --- TEI fetched OK")
        return ("unfetched-missing", f"no speech_index, TEI not indexable")
    book_n, letter_n = m.group(1), m.group(2)
    if not idx:
        return ("unfetched-missing", f"TEI returned no divs from {psrc}")
    book_letters = idx.get(book_n) or idx.get(book_n.lstrip("0")) or set()
    if not book_letters:
        return ("unfetched-missing",
                f"book {book_n} not found in TEI (books available: {sorted(idx.keys())[:5]}...)")
    if letter_n in book_letters or letter_n.lstrip("0") in book_letters:
        return ("unfetched-ok", f"book:{book_n}, letter:{letter_n} present in TEI")
    return ("unfetched-missing",
            f"book:{book_n}, letter:{letter_n} NOT in TEI (book has letters: "
            f"{sorted(book_letters, key=lambda s: (len(s), s))[:20]})")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(DEFAULT_REPORT))
    parser.add_argument("--json", default=str(DEFAULT_JSON))
    parser.add_argument("--no-fetch", action="store_true",
                        help="skip Perseus HTTP probes (rely on local Latin files only)")
    args = parser.parse_args(argv)

    with WORKS_YAML.open(encoding="utf-8") as f:
        works = yaml.safe_load(f)
    if not isinstance(works, list):
        works = works.get("works", works)

    tei_indexes: dict[str, dict[str, set[str]]] = {}
    do_fetch = not args.no_fetch

    buckets: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for entry in works:
        cat, detail = classify_entry(entry, tei_indexes, do_fetch)
        if cat == "no-pending-fetch":
            continue
        buckets[cat].append((entry.get("id", ""), entry.get("date", ""), detail))

    out = Path(args.out)
    lines: list[str] = []
    lines.append("# Perseus source-availability audit\n")
    lines.append(f"Generated by `scripts/audit_perseus_sources.py`.\n")
    if args.no_fetch:
        lines.append("(`--no-fetch` mode: local Latin files only; "
                     "unfetched works classified as `unfetched-unverified`.)\n")
    lines.append(f"\nTotal pending entries surveyed: "
                 f"{sum(len(v) for v in buckets.values())}\n")
    for cat in ("placeholder", "no-perseus", "unfetched-missing",
                "unfetched-ok", "ok", "unfetched-unverified"):
        items = buckets.get(cat, [])
        lines.append(f"\n## {cat} ({len(items)})\n")
        if not items:
            lines.append("None.\n")
            continue
        for work_id, date, detail in sorted(items, key=lambda t: t[1]):
            lines.append(f"- `{work_id}` ({date}) --- {detail}")
        lines.append("")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    Path(args.json).write_text(
        json.dumps(
            {cat: [{"id": i, "date": d, "detail": x} for i, d, x in items]
             for cat, items in buckets.items()},
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Wrote {Path(args.out).relative_to(REPO_ROOT) if Path(args.out).is_absolute() else args.out}")
    for cat in ("placeholder", "no-perseus", "unfetched-missing",
                "unfetched-ok", "ok", "unfetched-unverified"):
        print(f"  {cat}: {len(buckets.get(cat, []))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
