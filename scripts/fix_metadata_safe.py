#!/usr/bin/env python3
"""fix_metadata_safe.py --- apply conservative auto-fixes to meta/works.yaml.

The audit script (`scripts/audit_metadata.py`) reports OCR-bleed in the
`location_written` and `recipient` fields, plus some date-precision
discrepancies. This script applies the safe, high-confidence subset:

  1. Strip trailing salutation tails from `recipient`
     (e.g. `BRVTO S` --> `BRVTO`, `TVLLIVS TERENTIAE SVAE S. P` -->
     `TVLLIVS TERENTIAE SVAE`).
  2. Fix common mixed-case OCR typos in `recipient`
     (e.g. `ATTlCO` --> `ATTICO`).
  3. Strip trailing OCR-bleed fragments from `location_written`
     (e.g. `in Puteolano vht` --> `in Puteolano`, `Romae circ` -->
     `Romae`, `Brundisi pauli post` --> `Brundisi`).
  4. Apply the year-precision --> month-precision date corrections
     enumerated below (only the ones whose Perseus dateline gives a
     bare month with no day-precision).

The script edits meta/works.yaml at the text level (one field-line at
a time) to preserve the existing YAML formatting and avoid massive
re-serialization churn. It is idempotent.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKS_YAML = REPO_ROOT / "meta" / "works.yaml"

# ---------- recipient cleanup ----------

SALUTATION_TAILS = [
    r"S\.?\s*R\.?\s*D",
    r"S\.?\s*P\.?\s*D",
    r"S\.?\s*P",
    r"S\.?\s*R",
    r"SVO\s+S\.?",
    r"SALVTEM\s+DICIT",
    r"SALVTEM",
    r"SAL\.?",
    r"DIC\.?",
    r"D\.?",
    r"P\.?",
    r"S\.?",
]
SALUTATION_TAIL_RE = re.compile(
    r"\s+(?:" + r"|".join(SALUTATION_TAILS) + r")\s*$",
)
MIXED_CASE_TYPO_RE = re.compile(r"\b([A-Z]+)([a-z])([A-Z]+)\b")


def strip_salutation_tail(recipient: str) -> str:
    prev = None
    cur = recipient.strip()
    while prev != cur:
        prev = cur
        cur = SALUTATION_TAIL_RE.sub("", cur).rstrip(",")
        # Strip trailing whitespace only; preserve legitimate trailing
        # periods like `IMP.` or `PROCONSVLI` abbreviations.
        cur = cur.rstrip()
    cur = re.sub(r"\s{2,}", " ", cur)
    return cur


def fix_mixed_case_typos(recipient: str) -> str:
    def _replace(m: re.Match[str]) -> str:
        before, lower, after = m.group(1), m.group(2), m.group(3)
        if lower == "l":
            return before + "I" + after
        return before + lower.upper() + after
    return MIXED_CASE_TYPO_RE.sub(_replace, recipient)


# ---------- location_written cleanup ----------

LOCATION_TRAILING_JUNK = [
    r"a\.\s*d\.",
    r"K\.?", r"Kal\.?", r"Non\.?", r"Id\.?", r"Idus",
    r"prid\.?", r"postr(?:idie)?",
    r"ante", r"post",
    r"circ\.?", r"med\.?", r"medio", r"ineunte", r"extremo",
    r"ex\.?", r"exeunte",
    r"in\.?", r"fort\.?", r"fortasse",
    r"vel", r"aut", r"sive",
    r"ut", r"videtur",
    r"pauli", r"paulo",
    r"pr\.?", r"prior(?:e)?", r"post(?:erior(?:e)?)?",
    r"interc(?:al(?:ari)?)?\.?",
    r"sub", r"noctem", r"mane", r"vesp(?:eri|er(?:e)?)?\.?",
    r"a\.", r"m\.",
    r"anno", r"anni",
    r"ep\.?", r"diebus",
    r"i{1,3}\.?", r"iv\.?", r"v\.?", r"vi\.?", r"vii\.?", r"viii\.?",
    r"ix\.?", r"x\.?", r"xi\.?", r"xii\.?", r"xiii\.?", r"xiv\.?",
    r"xv\.?", r"xvi\.?", r"xvii\.?", r"xviii\.?", r"xix\.?", r"xx\.?",
    r"viW", r"vht", r"prict", r"xttv", r"xt", r"viil", r"viq",
    r"ld\.?", r"id\.?", r"iiii\.?",
    r"Quint(?:il(?:is)?)?\.?",
    r"Sext(?:il(?:is)?)?\.?",
    r"Iun(?:ias|i|io)?\.?",
    r"Iul(?:ias|i|io)?\.?",
    r"Mai(?:as|i|o)?\.?",
    r"Apr(?:il)?(?:is|es|i)?\.?",
    r"Mart(?:ias|i|io)?\.?",
    r"Febr(?:uar(?:ias|i|io|do|nto))?\.?",
    r"Ian(?:uar(?:ias|i|io))?\.?",
    r"Aug(?:ust(?:as|i|o))?\.?",
    r"Sept(?:embr(?:es|is|i))?\.?",
    r"Oct(?:obr(?:es|is|i))?\.?",
    r"Nov(?:embr(?:es|is|i))?\.?",
    r"Dec(?:embr(?:es|is|i))?\.?",
    r"\(\d+\)",
    r"\d{2,3}",
    r",", r":", r";",
]
LOCATION_JUNK_RE = re.compile(
    r"\s+(?:" + r"|".join(LOCATION_TRAILING_JUNK) + r")\s*$",
    re.IGNORECASE,
)


def strip_location_trailing_junk(loc: str) -> str:
    """Strip recognised trailing junk tokens *only at end-of-string*.

    Iterates until stable so a chain like `circ. m. Iun.` collapses
    one token at a time. Preserves prepositions and place-name
    fragments anywhere except the very end.
    """
    prev = None
    cur = loc.strip().rstrip(",;:")
    while prev != cur:
        prev = cur
        cur = LOCATION_JUNK_RE.sub("", cur).rstrip(",;:").rstrip()
        cur = re.sub(r"\s{2,}", " ", cur)
    return cur


# ---------- Year/month -> day or month precision corrections,
#            manually verified against the audit report ----------

DATE_PRECISION_CORRECTIONS: list[tuple[str, str, str, str]] = [
    # (work_id, new_date, new_precision, source_note)
    ("ad-atticum-02-04", "-0059-04-15", "month",
     "Perseus: medio circ. m. Aprili"),
    ("ad-atticum-02-16", "-0059-05-05", "month",
     "Perseus: in m. Maio (early May)"),
    ("ad-atticum-04-12", "-0055-05-15", "month",
     "Perseus: m. Mai. (OCR `um Mai.`)"),
    ("ad-quintum-fratrem-02-07", "-0055-02-15", "month",
     "Perseus: mense Februario (OCR `Februado`)"),
    ("ad-quintum-fratrem-02-08", "-0055-05-15", "month",
     "Perseus: mense Maio"),
    ("ad-quintum-fratrem-02-09", "-0054-02-05", "month",
     "Perseus: ineunte mense Februario (OCR `Februanto`)"),
    ("ad-familiares-02-10", "-0051-11-15", "day",
     "Perseus: a. d. xvii K. Decembr. = 15 Nov; flip year->day"),
]


# ---------- Text-level YAML editing ----------

ID_LINE_RE = re.compile(r"^-\s*id:\s*(\S+)\s*$")
FIELD_LINE_RE = re.compile(r"^(\s+)([\w_]+):\s*(.*)$")


def process_yaml_text(text: str) -> tuple[str, list[str]]:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    changes: list[str] = []

    cur_id: str | None = None
    date_corr_map = {wid: (d, p, note) for wid, d, p, note in DATE_PRECISION_CORRECTIONS}

    i = 0
    while i < len(lines):
        line = lines[i]
        m = ID_LINE_RE.match(line.rstrip("\n"))
        if m:
            cur_id = m.group(1)
            out.append(line)
            i += 1
            continue

        fm = FIELD_LINE_RE.match(line.rstrip("\n"))
        if fm and cur_id:
            indent, key, value = fm.group(1), fm.group(2), fm.group(3)
            new_value = value
            if key == "recipient" and value.strip():
                stripped = strip_salutation_tail(value.strip())
                stripped = fix_mixed_case_typos(stripped)
                if stripped != value.strip():
                    new_value = stripped
                    changes.append(
                        f"recipient {cur_id}: {value.strip()!r} -> {stripped!r}"
                    )
            elif key == "location_written" and value.strip():
                stripped = strip_location_trailing_junk(value.strip())
                if stripped != value.strip() and stripped:
                    new_value = stripped
                    changes.append(
                        f"location {cur_id}: {value.strip()!r} -> {stripped!r}"
                    )
            elif key == "date" and cur_id in date_corr_map:
                new_date, _, note = date_corr_map[cur_id]
                if value.strip() != new_date:
                    new_value = new_date
                    changes.append(
                        f"date {cur_id}: {value.strip()} -> {new_date} ({note})"
                    )
            elif key == "date_precision" and cur_id in date_corr_map:
                _, new_prec, _ = date_corr_map[cur_id]
                if value.strip() != new_prec:
                    new_value = new_prec
                    changes.append(
                        f"date_precision {cur_id}: {value.strip()} -> {new_prec}"
                    )

            if new_value != value:
                out.append(f"{indent}{key}: {new_value}\n")
            else:
                out.append(line)
            i += 1
            continue

        out.append(line)
        i += 1

    return "".join(out), changes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="print changes without writing")
    args = parser.parse_args(argv)

    text = WORKS_YAML.read_text(encoding="utf-8")
    new_text, changes = process_yaml_text(text)

    print(f"Applied {len(changes)} changes:")
    for line in changes[:60]:
        print(f"  {line}")
    if len(changes) > 60:
        print(f"  ... and {len(changes) - 60} more (showing first 60)")

    if args.dry_run:
        print("(dry-run; works.yaml unchanged)")
        return 0

    if new_text != text:
        WORKS_YAML.write_text(new_text, encoding="utf-8")
        print(f"Wrote {WORKS_YAML.relative_to(REPO_ROOT)}")
    else:
        print("No changes; works.yaml left as-is.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
