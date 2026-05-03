#!/usr/bin/env python3
"""Backfill structural sidecars for already-drafted works.

For every entry in ``meta/works.yaml`` whose status is drafted/reviewed/final,
this script regenerates (or creates) three structural artifacts:

  1. ``data/parallel/<category>/<id>.json`` — section-aligned Latin/English
     parallel corpus, derived mechanically from ``latin/.../<id>.tex`` and
     ``english/.../<id>.tex``.

  2. Updates the corpus-wide ``data/greek-phrases.json`` with every Greek
     phrase encountered (Unicode Greek block, ``\\textgreek{...}`` macro, or
     ``[Greek: ...]`` form).

  3. Updates the corpus-wide ``data/letter-network.json`` with sender,
     recipient, place, date, and length for every drafted letter.

Idempotent. Re-running rebuilds the artifacts from scratch.

This script does NOT produce judgment-heavy artifacts (named-entity
mentions, allusions, cross-references, glossary notes). Those are emitted
by the translator session-by-session, going forward, and may be backfilled
in a later judgment pass.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    raise

REPO = Path(__file__).resolve().parent.parent
WORKS_YAML = REPO / "meta" / "works.yaml"
DATA = REPO / "data"

DRAFTED = {"drafted", "reviewed", "final"}

# Match \ciceroSection{N} where N is an integer or a small dotted form.
SECTION_RX = re.compile(r"\\ciceroSection\{([^}]+)\}")

# Match \textgreek{...} (single-line, no nesting).
GREEK_MACRO_RX = re.compile(r"\\textgreek\{([^}]+)\}")

# Match [Greek: ...] convention from STYLE.md.
GREEK_BRACKET_RX = re.compile(r"\[Greek:\s*([^\]]+)\]")

# Greek Unicode ranges (basic + extended).
GREEK_CHAR_RX = re.compile(r"[Ͱ-Ͽἀ-῿]+(?:\s+[Ͱ-Ͽἀ-῿]+)*")

# Common LaTeX macros to strip down to their content.
KEEP_CONTENT_MACROS = ("emph", "textit", "textbf", "textsc")
# Macros to drop entirely (with their argument):
DROP_MACROS = ("ciceroLetterOpener",)


def parse_date(s: str) -> tuple[int, int, int]:
    if s.startswith("-"):
        ys, rest = s[1:].split("-", 1)
        year = -int(ys)
    else:
        ys, rest = s.split("-", 1)
        year = int(ys)
    m, d = rest.split("-")
    return year, int(m), int(d)


def chronological_key(w: dict) -> tuple[int, int, int, str]:
    y, m, d = parse_date(w["date"])
    return (y, m, d, w["id"])


def strip_latex(s: str) -> str:
    """Remove cicero-specific LaTeX macros and emphasis macros, keeping the
    underlying prose. Intended for the parallel-corpus text fields, where we
    want clean text rather than typesetting."""
    # Drop the \ciceroLetterOpener{...} macro entirely (its argument is the
    # Latin salutation, which is not part of the body prose).
    for macro in DROP_MACROS:
        s = re.sub(r"\\" + macro + r"\{[^}]*\}", "", s)
    # Strip the section marker; it is captured separately.
    s = SECTION_RX.sub("", s)
    # \emph{x}, \textit{x}, etc. → x
    for macro in KEEP_CONTENT_MACROS:
        s = re.sub(r"\\" + macro + r"\{([^}]*)\}", r"\1", s)
    # \textgreek{x} → x  (preserve the Greek but drop the wrapper)
    s = re.sub(r"\\textgreek\{([^}]*)\}", r"\1", s)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def read_section_split(path: Path) -> list[tuple[str, str]]:
    """Read a Cicero .tex source and return [(loc, prose), ...].

    If no \\ciceroSection markers are present (typical for short letters),
    the whole body after stripping the salutation and comments is returned
    as a single section labelled "1".
    """
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    # Drop comment lines (anywhere on the line, but cicero TeX uses
    # full-line comments at top).
    text = "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%")
    )
    matches = list(SECTION_RX.finditer(text))
    if not matches:
        body = strip_latex(text)
        return [("1", body)] if body else []
    pieces: list[tuple[str, str]] = []
    last_end = 0
    last_loc = None
    for m in matches:
        if last_loc is not None:
            pieces.append((last_loc, text[last_end:m.start()]))
        last_loc = m.group(1)
        last_end = m.end()
    if last_loc is not None:
        pieces.append((last_loc, text[last_end:]))
    return [(loc, strip_latex(prose)) for loc, prose in pieces]


def build_parallel(work: dict) -> dict[str, Any] | None:
    lat_path = REPO / work["latin_file"]
    eng_path = REPO / work["english_file"]
    lat_sections = read_section_split(lat_path)
    eng_sections = read_section_split(eng_path)
    if not lat_sections or not eng_sections:
        return None
    # Index by loc on the English side so we tolerate Latin lacunae
    eng_index = {loc: text for loc, text in eng_sections}
    segments = []
    for loc, lat_text in lat_sections:
        eng_text = eng_index.get(loc, "")
        segments.append({
            "loc": loc,
            "section": _safe_int(loc),
            "lat": lat_text,
            "eng": eng_text,
            "notes": None,
        })
    return {
        "schema_version": 1,
        "id": work["id"],
        "category": work["category"],
        "title_latin": work["title_latin"],
        "title_english": work["title_english"],
        "date": work["date"],
        "source_latin": _source_label(work),
        "translator": "Claude (Anthropic), via cicero-by-claude",
        "license": "CC BY-NC-SA 4.0",
        "alignment_grain": "section",
        "segments": segments,
    }


def _safe_int(loc: str) -> int | None:
    try:
        return int(loc)
    except ValueError:
        # Dotted forms like "1.34" — we keep the loc string but the
        # primary integer section is the leading number.
        try:
            return int(loc.split(".", 1)[0])
        except ValueError:
            return None


def _source_label(work: dict) -> str:
    url = work.get("latin_source_url") or ""
    if "perseus" in url.lower() or "PerseusDL" in url:
        return "Perseus Digital Library (canonical-latinLit)"
    if "thelatinlibrary" in url.lower():
        return "The Latin Library"
    return "manual / mixed"


def collect_greek_from_text(text: str) -> list[dict[str, str]]:
    """Return a list of {kind, raw} dicts for Greek occurrences in a chunk
    of prose text."""
    out: list[dict[str, str]] = []
    for m in GREEK_MACRO_RX.finditer(text):
        out.append({"kind": "macro", "raw": m.group(1)})
    for m in GREEK_BRACKET_RX.finditer(text):
        out.append({"kind": "bracket", "raw": m.group(1)})
    for m in GREEK_CHAR_RX.finditer(text):
        if m.group(0).strip():
            out.append({"kind": "unicode", "raw": m.group(0)})
    return out


def build_greek_entries(work: dict, next_id: int) -> tuple[list[dict[str, Any]], int]:
    lat_path = REPO / work["latin_file"]
    eng_path = REPO / work["english_file"]
    if not lat_path.exists():
        return [], next_id
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()  # (loc, raw, kind)

    for path in (lat_path, eng_path):
        if not path.exists():
            continue
        for loc, prose in read_section_split(path):
            # We need to look at the raw text (with macros) for Greek detection
            # in some forms; re-read raw section here.
            pass

    # Re-read raw (without strip) to catch \textgreek{} and [Greek: ...]
    for path in (lat_path, eng_path):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        # Drop comments
        text = "\n".join(
            line for line in text.splitlines()
            if not line.lstrip().startswith("%")
        )
        # Walk sections in raw text
        last_end = 0
        last_loc = None
        section_chunks: list[tuple[str, str]] = []
        for m in SECTION_RX.finditer(text):
            if last_loc is not None:
                section_chunks.append((last_loc, text[last_end:m.start()]))
            last_loc = m.group(1)
            last_end = m.end()
        if last_loc is not None:
            section_chunks.append((last_loc, text[last_end:]))

        for loc, raw in section_chunks:
            for hit in collect_greek_from_text(raw):
                key = (loc, hit["raw"].strip(), hit["kind"])
                if key in seen:
                    continue
                seen.add(key)
                out.append({
                    "id": f"gr-{next_id:04d}",
                    "work": work["id"],
                    "loc": loc,
                    "greek_original": hit["raw"].strip() if hit["kind"] == "unicode" else "",
                    "transliteration": hit["raw"].strip() if hit["kind"] != "unicode" else "",
                    "english_gloss": "",
                    "context": "",
                    "suspected_source": None,
                    "source_certainty": "unknown",
                    "register": "technical",
                    "notes": f"backfilled (kind={hit['kind']})",
                })
                next_id += 1
    return out, next_id


def count_sections(path: Path) -> int:
    if not path.exists():
        return 0
    return len(SECTION_RX.findall(path.read_text(encoding="utf-8")))


def _slug(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
    return s


def build_letter_entry(work: dict) -> dict[str, Any]:
    """Build one entry for data/letter-network.json from a letter work."""
    lat_path = REPO / work["latin_file"]
    sender = "M. Tullius Cicero"
    sender_id = "person:cicero"
    recipient = work.get("recipient") or ""
    recipient_id = f"person:{_slug(recipient)}" if recipient else None
    place = work.get("location_written") or None
    place_id = f"place:{_slug(place)}" if place else None
    return {
        "id": work["id"],
        "sender": sender,
        "sender_id": sender_id,
        "recipient": recipient,
        "recipient_id": recipient_id,
        "place_written": place,
        "place_written_id": place_id,
        "place_received": None,
        "place_received_id": None,
        "date": work["date"],
        "date_precision": work.get("date_precision", "year"),
        "topics": [],
        "mood": None,
        "length_sections": count_sections(lat_path),
        "carries_greek": False,  # filled in after greek pass
    }


def main() -> int:
    if not WORKS_YAML.exists():
        sys.stderr.write(f"meta/works.yaml not found at {WORKS_YAML}\n")
        return 2

    works: list[dict[str, Any]] = yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []
    drafted = [w for w in works if w.get("status") in DRAFTED]
    drafted.sort(key=chronological_key)

    n_parallel = 0
    n_letters = 0
    greek_entries: list[dict[str, Any]] = []
    next_greek_id = 1
    letter_entries: list[dict[str, Any]] = []
    works_with_greek: set[str] = set()

    for work in drafted:
        # Parallel corpus
        parallel = build_parallel(work)
        if parallel is not None:
            cat_dir = DATA / "parallel" / work["category"]
            cat_dir.mkdir(parents=True, exist_ok=True)
            base = Path(work["english_file"]).stem  # e.g. 081bc-pro-quinctio
            (cat_dir / f"{base}.json").write_text(
                json.dumps(parallel, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            n_parallel += 1

        # Greek phrases
        greeks, next_greek_id = build_greek_entries(work, next_greek_id)
        if greeks:
            works_with_greek.add(work["id"])
            greek_entries.extend(greeks)

        # Letter network
        if work["category"] == "letters":
            letter_entries.append(build_letter_entry(work))
            n_letters += 1

    # Mark letters that carry Greek
    for entry in letter_entries:
        if entry["id"] in works_with_greek:
            entry["carries_greek"] = True

    # Stable sort for corpus-wide files
    work_date: dict[str, tuple[int, int, int]] = {
        w["id"]: parse_date(w["date"]) for w in works
    }
    greek_entries.sort(key=lambda e: (work_date.get(e["work"], (0, 0, 0)), e.get("loc", "")))
    letter_entries.sort(key=lambda e: (work_date.get(e["id"], (0, 0, 0)), e["id"]))

    # Reassign greek IDs in sorted order so they read chronologically
    for i, entry in enumerate(greek_entries, start=1):
        entry["id"] = f"gr-{i:04d}"

    (DATA / "greek-phrases.json").write_text(
        json.dumps({"schema_version": 1, "entries": greek_entries},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (DATA / "letter-network.json").write_text(
        json.dumps({"schema_version": 1, "letters": letter_entries},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        f"Backfill: {n_parallel} parallel sidecar(s), "
        f"{len(greek_entries)} Greek-phrase entry(ies), "
        f"{n_letters} letter-network entry(ies)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
