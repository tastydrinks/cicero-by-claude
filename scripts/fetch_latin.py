#!/usr/bin/env python3
"""Fetch Latin source text for one or more works listed in meta/works.yaml.

Source preference (set in works.yaml per entry):
  1. Perseus / Scaife — for canonical Latin (CTS-aware)
  2. Latin Library — fallback (HTML scrape)

Light cleanup is applied:
  - HTML stripped, entities decoded
  - Quotation marks normalized
  - Section / chapter markers preserved as \\ciceroSection{N}
  - Whitespace collapsed but paragraph breaks kept

Usage:
  python scripts/fetch_latin.py <work-id>
  python scripts/fetch_latin.py --all          # fetch every entry
  python scripts/fetch_latin.py --pending      # only entries without latin_file
  python scripts/fetch_latin.py --dry-run <id> # show what would be fetched

The script is intentionally per-translation: in normal use you only fetch a
work's Latin just before translating it.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import time
from pathlib import Path
from typing import Iterable

try:
    import requests
    import yaml
    from bs4 import BeautifulSoup
except ImportError as e:
    sys.stderr.write(
        f"Missing dependency: {e.name}. Install with:\n"
        f"  pip install pyyaml requests beautifulsoup4\n"
    )
    raise

REPO = Path(__file__).resolve().parent.parent
WORKS_YAML = REPO / "meta" / "works.yaml"

USER_AGENT = "cicero-by-claude fetcher (https://github.com/tastydrinks/cicero-by-claude)"
TIMEOUT = 30
RETRY_COUNT = 3
RETRY_BACKOFF = 2  # seconds


# ---------------------------------------------------------------------------
# Loading the manifest
# ---------------------------------------------------------------------------

def load_works() -> list[dict]:
    if not WORKS_YAML.exists():
        sys.stderr.write(f"meta/works.yaml not found at {WORKS_YAML}\n")
        sys.stderr.write("Run scripts/seed_works.py first.\n")
        sys.exit(2)
    return yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []


def find_work(works: list[dict], work_id: str) -> dict:
    for w in works:
        if w["id"] == work_id:
            return w
    sys.stderr.write(f"Unknown work id: {work_id!r}\n")
    sys.exit(2)


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def http_get(url: str) -> str:
    last_err: Exception | None = None
    for attempt in range(RETRY_COUNT):
        try:
            r = requests.get(
                url,
                headers={"User-Agent": USER_AGENT},
                timeout=TIMEOUT,
            )
            r.raise_for_status()
            r.encoding = r.apparent_encoding or "utf-8"
            return r.text
        except Exception as e:
            last_err = e
            wait = RETRY_BACKOFF * (2**attempt)
            sys.stderr.write(
                f"  HTTP error ({e}); retrying in {wait}s ({attempt + 1}/{RETRY_COUNT})\n"
            )
            time.sleep(wait)
    raise RuntimeError(f"failed after {RETRY_COUNT} attempts: {url}: {last_err}")


# ---------------------------------------------------------------------------
# Parsing — Latin Library
# ---------------------------------------------------------------------------

# Latin Library marks section numbers either as inline numerals before clauses
# (e.g. "[1]" or "1.") or as bracketed integers in the running text. We
# capture both common conventions.

_LL_SECTION_INLINE = re.compile(r"\s*\[\s*(\d+)\s*\]\s*")
_LL_SECTION_BARE = re.compile(r"^\s*(\d+)\.\s+", re.MULTILINE)
_WS = re.compile(r"[ \t]+")
_BLANK_LINES = re.compile(r"\n{3,}")


def parse_latin_library(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")
    # The Latin Library wraps the running text in a series of <p> elements.
    # Strip nav, headers, links to home page.
    for tag in soup(["script", "style", "head", "title"]):
        tag.decompose()
    # Remove "back to" navigation paragraphs and image links, often the very
    # first and last paragraphs.
    paragraphs: list[str] = []
    for p in soup.find_all(["p", "div"]):
        text = p.get_text(" ", strip=True)
        if not text:
            continue
        if text.lower().startswith(("the latin library", "the classics page")):
            continue
        if "thelatinlibrary.com" in text.lower() and len(text) < 200:
            continue
        paragraphs.append(text)

    if not paragraphs:
        # Fallback: take everything in the body
        body = soup.find("body")
        if body is not None:
            paragraphs = [body.get_text(" ", strip=True)]

    raw = "\n\n".join(paragraphs)
    raw = html.unescape(raw)
    return convert_to_tex(raw)


def convert_to_tex(text: str) -> str:
    """Normalize whitespace, replace section markers with LaTeX macros, and
    return text suitable for a TeX file."""
    # Normalize quotation marks
    text = text.replace("“", "``").replace("”", "''")
    text = text.replace("‘", "`").replace("’", "'")
    text = text.replace("«", "<<").replace("»", ">>")

    # Section markers like [12] become \ciceroSection{12}
    text = _LL_SECTION_INLINE.sub(lambda m: f"\n\n\\ciceroSection{{{m.group(1)}}}\n\n", text)

    # Standalone numeric paragraph leads (rare on Latin Library): "12. lorem..."
    text = _LL_SECTION_BARE.sub(lambda m: f"\\ciceroSection{{{m.group(1)}}} ", text)

    # Tabs / multiple spaces → single space
    text = _WS.sub(" ", text)
    # Collapse runs of blank lines
    text = _BLANK_LINES.sub("\n\n", text)
    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# Parsing — Perseus / Scaife reader (best-effort)
# ---------------------------------------------------------------------------

def parse_perseus_tei(xml_text: str, speech_index: str | None = None) -> str:
    """Parse a Perseus canonical-latinLit TEI XML file and emit LaTeX.

    The TEI structure used in PerseusDL/canonical-latinLit:
      <body>
        <div type="edition">
          [optional <div type="textpart" subtype="speech" n="N">]
            <div type="textpart" subtype="section" n="N">
              <p>... <milestone n="N" unit="chapter"/> ...</p>
            </div>

    For multi-speech bundles (Catilinarians, Verrines, Philippics, Agrarians)
    pass speech_index="1" through "14" to select one. For single-speech files
    pass speech_index=None.
    """
    soup = BeautifulSoup(xml_text, "xml")
    body = soup.find("body")
    if body is None:
        raise RuntimeError("no <body> element in TEI XML")

    edition = body.find("div", attrs={"type": "edition"})
    root = edition or body

    if speech_index is not None:
        speech = root.find(
            "div",
            attrs={"type": "textpart", "subtype": "speech", "n": str(speech_index)},
        )
        if speech is None:
            raise RuntimeError(f"speech {speech_index} not found in bundle")
        root = speech

    # Strip critical apparatus before extracting text. TEI variants live
    # inside <app><rdg>...</rdg></app>; we keep <lem> (the chosen reading)
    # and discard <rdg>, <witDetail>, <note>, <app>'s loose siglum tails.
    for tag_name in ("rdg", "witDetail", "note", "app", "lem"):
        # We have to handle <app> specially: keep inner <lem> text, drop the
        # rest. Easiest is to replace each <app> with the text of its <lem>.
        if tag_name == "app":
            for app in root.find_all("app"):
                lem = app.find("lem")
                replacement = lem.get_text(" ", strip=True) if lem is not None else ""
                app.replace_with(replacement)
        elif tag_name == "lem":
            # After <app> processing all remaining <lem>s should be gone, but
            # protect against malformed XML.
            for lem in root.find_all("lem"):
                lem.unwrap()
        else:
            for tag in root.find_all(tag_name):
                tag.decompose()

    sections = root.find_all(
        "div", attrs={"type": "textpart", "subtype": "section"}
    )
    if not sections:
        # Some files have only chapter divisions or flat <p> children.
        sections = []

    pieces: list[str] = []
    if sections:
        for sec in sections:
            n = sec.get("n", "?")
            text = sec.get_text(" ", strip=True)
            text = text.replace("\n", " ").strip()
            text = re.sub(r"\s+", " ", text)
            pieces.append(f"\\ciceroSection{{{n}}} {text}")
    else:
        # Fallback: flatten paragraphs in document order
        for p in root.find_all("p"):
            t = p.get_text(" ", strip=True)
            if t:
                pieces.append(t)

    if not pieces:
        raise RuntimeError("Perseus TEI parse produced no text")

    body_text = "\n\n".join(pieces)

    # Light cleanup: normalize quotes, drop chapter milestones (they appear
    # inside section text after get_text; harmless but redundant).
    body_text = body_text.replace("“", "``").replace("”", "''")
    body_text = body_text.replace("‘", "`").replace("’", "'")
    return body_text + "\n"


# Back-compat alias (the previous parse_perseus signature was HTML-based)
def parse_perseus(text: str, speech_index: str | None = None) -> str:
    return parse_perseus_tei(text, speech_index=speech_index)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def fetch_one(work: dict, dry_run: bool = False) -> bool:
    target = REPO / work["latin_file"]
    if target.exists() and target.stat().st_size > 0:
        print(f"  {work['id']}: already fetched ({target.relative_to(REPO)}), skipping")
        return True

    primary = work.get("latin_source_url")
    fallback = work.get("latin_source_url_fallback")
    sources: list[tuple[str, str]] = []
    if primary:
        sources.append(("perseus", primary))
    if fallback:
        sources.append(("latin_library", fallback))
    # Need lxml for the BeautifulSoup XML parser; importing lazily keeps
    # the script usable for HTML-only sources without lxml installed.
    try:
        import lxml  # noqa: F401
    except ImportError:
        sys.stderr.write(
            "  (note: lxml not installed; install for fastest XML parsing: pip install lxml)\n"
        )

    if not sources:
        print(f"  {work['id']}: no source URL configured, skipping")
        return False

    last_err: Exception | None = None
    speech_index = work.get("speech_index")
    for kind, url in sources:
        print(f"  {work['id']}: fetching {kind} {url}")
        if dry_run:
            return True
        try:
            text = http_get(url)
        except Exception as e:
            last_err = e
            sys.stderr.write(f"    {kind} fetch failed: {e}\n")
            continue
        try:
            if kind == "perseus":
                tex = parse_perseus(text, speech_index=speech_index)
            else:
                tex = parse_latin_library(text)
        except Exception as e:
            last_err = e
            sys.stderr.write(f"    {kind} parse failed: {e}\n")
            continue

        # Sanity check: too-short outputs almost certainly mean we got an
        # error page or wrong selector.
        if len(tex.strip()) < 200:
            sys.stderr.write(
                f"    {kind} produced suspiciously short output ({len(tex)} chars); "
                f"trying next source\n"
            )
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        header = (
            f"% {work['title_latin']} ({work['id']})\n"
            f"% Source: {url}\n"
            f"% Fetched by scripts/fetch_latin.py\n\n"
        )
        target.write_text(header + tex, encoding="utf-8")
        print(f"    wrote {target.relative_to(REPO)} ({len(tex)} chars)")
        return True

    sys.stderr.write(f"  {work['id']}: all sources failed (last error: {last_err})\n")
    return False


def select_works(
    works: list[dict],
    ids: Iterable[str],
    all_: bool,
    pending: bool,
) -> list[dict]:
    if all_:
        return list(works)
    if pending:
        return [w for w in works if not (REPO / w["latin_file"]).exists()]
    chosen = []
    for wid in ids:
        chosen.append(find_work(works, wid))
    return chosen


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch Latin source for Cicero works.")
    parser.add_argument("ids", nargs="*", help="Work id(s) to fetch")
    parser.add_argument("--all", action="store_true", help="Fetch every work in the manifest")
    parser.add_argument("--pending", action="store_true", help="Fetch only works whose latin_file does not yet exist")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fetched without writing files")
    args = parser.parse_args(argv)

    if not (args.ids or args.all or args.pending):
        parser.error("Specify one or more work ids, or --all / --pending")

    works = load_works()
    targets = select_works(works, args.ids, args.all, args.pending)

    print(f"Fetching {len(targets)} work(s)")
    failed = 0
    for w in targets:
        ok = fetch_one(w, dry_run=args.dry_run)
        if not ok:
            failed += 1

    if failed:
        sys.stderr.write(f"\n{failed} fetch(es) failed.\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
