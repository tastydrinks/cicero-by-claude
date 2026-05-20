#!/usr/bin/env python3
"""audit_metadata.py --- audit meta/works.yaml for OCR-bleed and date errors.

Checks every entry whose Latin file exists, against the
% Dateline (Perseus): ... comment in the Latin file:

  1. Field hygiene --- OCR-bleed of date-numerals or salutation tokens
     into location_written / recipient.
  2. Date sanity --- computed Julian date from the Perseus dateline
     vs the stored works.yaml date. Flags year-precision placeholders
     when Perseus has day-precision; flags computed/stored mismatches.
  3. Placeholder detection --- Latin files containing % PLACEHOLDER,
     and works whose only working source is the now-403 Latin Library
     fallback.

Output: a markdown report written to meta/audit-report.md.
The script does not auto-fix; corrections are applied by hand.

Usage:
    python scripts/audit_metadata.py [--out PATH]
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKS_YAML = REPO_ROOT / "meta" / "works.yaml"
DEFAULT_REPORT = REPO_ROOT / "meta" / "audit-report.md"

# ---------- Roman date arithmetic ----------

MONTH_ABBR_TO_NUM = {
    # 3-letter prefix keys, lowercased; covers Quint (Quintilis), Sext
    # (Sextilis), Iul, Iun, Mart, Februar, etc.
    "ian": 1, "jan": 1, "feb": 2, "mar": 3, "apr": 4,
    "mai": 5, "may": 5, "iun": 6, "jun": 6, "qui": 7, "iul": 7, "jul": 7,
    "sex": 8, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def month_name_to_num(word: str) -> int | None:
    """Look up a Latin month word by its 3-letter prefix, lowercased.

    Handles abbreviated forms (`Iun.`), older names (`Quintilis`,
    `Sextilis`), and OCR-corrupted variants whose first three letters
    survive (e.g. `Februado`, `Februanto`, `Februardo` --- all start
    `feb`).
    """
    if not word:
        return None
    return MONTH_ABBR_TO_NUM.get(word.lower()[:3])

# Nones fall on the 7th in March, May, July (Quintilis), October; on the 5th
# in all other months. Ides are 8 days after the Nones.
NONES_LATE_MONTHS = {3, 5, 7, 10}

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}

# Roman lowercase numerals seen in datelines (i..xx) plus the spelled-out
# pridie/postridie. We allow up to xviii because Roman date arithmetic
# almost never exceeds about 19 days before a marker.
ROMAN_NUM = r"(?:i{1,3}|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv|xvi|xvii|xviii|xix)"
DATELINE_RE = re.compile(
    r"%\s*Dateline\s*\(Perseus\):\s*(?P<body>.+)",
    re.IGNORECASE,
)


def nones_day(month: int) -> int:
    return 7 if month in NONES_LATE_MONTHS else 5


def ides_day(month: int) -> int:
    return nones_day(month) + 8


def roman_to_int(s: str) -> int:
    s = s.lower()
    # Special common forms first
    table = {
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6,
        "vii": 7, "viii": 8, "ix": 9, "x": 10, "xi": 11, "xii": 12,
        "xiii": 13, "xiv": 14, "xv": 15, "xvi": 16, "xvii": 17,
        "xviii": 18, "xix": 19,
    }
    return table.get(s, -1)


@dataclass
class ComputedDate:
    year: int  # negative for BC, e.g. -44 for 44 BC
    month: int
    day: int
    precision: str  # 'day' | 'month' | 'year'

    def iso(self) -> str:
        # works.yaml uses YYYY-MM-DD with negative year padded to 4 digits
        y = self.year
        sign = "-" if y <= 0 else ""
        # Cicero is BC; works.yaml writes e.g. -0044
        abs_y = abs(y)
        return f"{sign}{abs_y:04d}-{self.month:02d}-{self.day:02d}"


def parse_dateline(body: str, fallback_year: int) -> ComputedDate | None:
    """Parse a Perseus dateline body into a computed date.

    Examples handled:
      "Scr. in Puteolano vi Id. Quint. a. 710 (44)."
      "Scr. Vibone viii K. Sext. a. 710 (44) ."
      "Scr. in Tusculano inter v et prid. Non. Quint. a. 710 (44)."
      "Scr. in Arpinati medio mense Novembri a. 710 (44) ."
      "Scr. in Puteolano Non. Nov. a. 710 (44) ."
      "Scr. Aquini iv Id. Nov. a. 710 (44)."

    Returns None if it can't extract a coherent date.
    """
    text = body.strip().rstrip(".").strip()

    # 1. Extract year hint --- "a. NNN (YY)" gives both ab urbe condita and BC
    year_m = re.search(r"a\.\s*\d+\s*\((\d+)\)", text)
    year_bc = int(year_m.group(1)) if year_m else fallback_year
    year = -year_bc

    # 2. Imprecise month-only phrasings:
    #    "medio mense Novembri", "ineunte mense Februario",
    #    "extremo m. Dec.", "in m. Sext.", "med. m. Iun.", "ex. m. Maio"
    qualifier_pat = r"(?P<q>medio|med\.?|ineunte|in\.?|extremo|ex\.?|exeunte)"
    imprecise_m = re.search(
        rf"{qualifier_pat}?\s*(?:mense|m\.?)\s+(?P<month>[A-Za-z]+)",
        text, re.IGNORECASE,
    )
    if imprecise_m:
        month_num = month_name_to_num(imprecise_m.group("month"))
        if month_num:
            kind = (imprecise_m.group("q") or "medio").lower().rstrip(".")
            if kind in ("medio", "med"):
                day = 15
            elif kind in ("ineunte", "in"):
                day = 5
            elif kind in ("extremo", "ex", "exeunte"):
                day = 25
            else:
                day = 15
            return ComputedDate(year, month_num, day, "month")

    # 3. Roman-style precise dates: look for Kal./Non./Id. + month
    # Pattern: optional roman numeral, optional "prid.", then marker, then month
    # We also try the "inter X et Y" range pattern, taking the later end.
    range_m = re.search(
        rf"inter\s+(?:a\.?\s*d\.?\s*)?(?P<a_num>{ROMAN_NUM})\.?\s+et\s+"
        rf"(?:(?P<prid>prid\.?)|(?:a\.?\s*d\.?\s*)?(?P<b_num>{ROMAN_NUM})\.?)\s+"
        rf"(?P<marker>Kal|K|Non|Id)\.?\s+(?P<month>[A-Za-z]+)",
        text, re.IGNORECASE,
    )
    if range_m:
        marker = range_m.group("marker")
        month_word = range_m.group("month")
        # use the later end: prid = 1 before the marker; smaller roman numeral
        # is the later day
        if range_m.group("prid"):
            offset = 1
        else:
            offset = roman_to_int(range_m.group("b_num")) - 1
        return _resolve_roman_date(year, month_word, marker, offset, "day")

    single_m = re.search(
        rf"(?:(?P<prid>prid\.?|postr(?:idie)?)|(?:a\.?\s*d\.?\s*)?(?P<num>{ROMAN_NUM})\.?)?"
        rf"\s*(?P<marker>Kal|K|Non|Id)\.?\s+(?P<month>[A-Za-z]+)",
        text, re.IGNORECASE,
    )
    if single_m:
        marker = single_m.group("marker")
        month_word = single_m.group("month")
        prid = single_m.group("prid")
        num = single_m.group("num")
        if prid:
            offset = 1 if prid.lower().startswith("prid") else -1
        elif num:
            n = roman_to_int(num)
            if n < 0:
                return None
            offset = n - 1
        else:
            offset = 0
        return _resolve_roman_date(year, month_word, marker, offset, "day")

    # Year-only is what works.yaml already has as fallback; no extra precision
    return None


def _resolve_roman_date(year: int, month_word: str, marker: str,
                        offset: int, precision: str) -> ComputedDate | None:
    """Given a Roman date marker and offset, return the Julian (proleptic) date.

    marker: 'Kal' or 'K' (Kalends, day 1), 'Non' (Nones), 'Id' (Ides)
    offset: 0 = on the marker, 1 = pridie (day before), N = N days before
            inclusive-count - 1; postridie passes offset=-1.
    """
    month_num = month_name_to_num(month_word)
    if not month_num:
        return None

    if marker.lower().startswith("k"):
        # Kalends = day 1 of THIS month, but "vi K. Sept" is in August
        if offset > 0:
            # vi K. Sept = day (DaysInAug + 1 - offset)
            prev_month = 12 if month_num == 1 else month_num - 1
            day = DAYS_IN_MONTH[prev_month] + 1 - offset
            return ComputedDate(year, prev_month, day, precision)
        elif offset == 0:
            return ComputedDate(year, month_num, 1, precision)
        elif offset == -1:  # postridie K.
            return ComputedDate(year, month_num, 2, precision)
    elif marker.lower().startswith("n"):
        n = nones_day(month_num)
        return ComputedDate(year, month_num, n - offset, precision)
    elif marker.lower().startswith("i"):
        i = ides_day(month_num)
        return ComputedDate(year, month_num, i - offset, precision)

    return None


# ---------- Field-hygiene regexes ----------

LOC_DATETOKEN_RE = re.compile(
    rf"\b(ante|post|postr(?:idie)?|prid\.?|{ROMAN_NUM}|aut|K\.?|Id\.?|Non\.?|Kal\.?)\b",
    re.IGNORECASE,
)
# Strip any leading "in Pompeiano", "in Tusculano", etc. then check what remains
LOC_PREFIX_RE = re.compile(
    r"^\s*(in\s+)?[A-Z][a-z]+(?:o|ae|is|i|a|um|e)?\s*",
)

RECIPIENT_SUSPECT_RE = re.compile(
    r"(?:\bDIC\.?\b|\bsalutem\b|\bsuo\b|\bS\.?\b|\s{2,})",
    re.IGNORECASE,
)
# Lowercase-letter typos in otherwise-uppercase recipient (ATTlCO has a
# lowercase L for an I)
RECIPIENT_CASE_RE = re.compile(r"[A-Z]+[a-z]+[A-Z]+")


@dataclass
class AuditReport:
    field_hygiene: list[str] = field(default_factory=list)
    date_sanity: list[str] = field(default_factory=list)
    placeholders: list[str] = field(default_factory=list)
    fallback_only: list[str] = field(default_factory=list)
    parse_failures: list[str] = field(default_factory=list)


def audit_entry(entry: dict, repo_root: Path, report: AuditReport) -> None:
    work_id = entry.get("id", "<no-id>")
    latin_file_rel = entry.get("latin_file")
    if not latin_file_rel:
        return
    latin_path = repo_root / latin_file_rel
    if not latin_path.exists():
        return

    # ---------- placeholder detection ----------
    try:
        text = latin_path.read_text(encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        report.parse_failures.append(f"{work_id}: cannot read {latin_file_rel} ({e})")
        return

    if "% PLACEHOLDER" in text:
        report.placeholders.append(f"- `{work_id}` --- {latin_file_rel}")
        return  # don't audit fields on placeholder stubs

    # ---------- field hygiene ----------
    loc = (entry.get("location_written") or "").strip()
    if loc:
        # Strip a leading "in X-ano/X-i" pattern, see what's left
        residual = LOC_PREFIX_RE.sub("", loc, count=1).strip()
        if LOC_DATETOKEN_RE.search(residual):
            report.field_hygiene.append(
                f"- `{work_id}` `location_written`: `{loc}` (date-token residue: `{residual}`)"
            )
        # Also flag double-spaces or trailing single letters
        elif re.search(r"\s{2,}|[A-Za-z]\s*$", loc) and len(residual) > 0 and len(residual) <= 4:
            report.field_hygiene.append(
                f"- `{work_id}` `location_written`: `{loc}` (suspicious trailing fragment: `{residual}`)"
            )

    recipient = (entry.get("recipient") or "").strip()
    if recipient:
        if RECIPIENT_SUSPECT_RE.search(recipient):
            report.field_hygiene.append(
                f"- `{work_id}` `recipient`: `{recipient}` (contains salutation/whitespace token)"
            )
        elif RECIPIENT_CASE_RE.search(recipient):
            report.field_hygiene.append(
                f"- `{work_id}` `recipient`: `{recipient}` (mixed-case mid-word --- possible OCR typo)"
            )

    # ---------- date sanity ----------
    dateline_m = DATELINE_RE.search(text)
    if not dateline_m:
        return
    dateline_body = dateline_m.group("body").strip()
    stored_date = entry.get("date") or ""
    stored_prec = entry.get("date_precision") or ""

    # Extract BC year hint from stored date for the parse_dateline fallback
    fallback_year = 0
    m = re.match(r"-(\d{4})", stored_date)
    if m:
        fallback_year = int(m.group(1))

    computed = parse_dateline(dateline_body, fallback_year)
    if computed is None:
        report.parse_failures.append(
            f"- `{work_id}` --- dateline did not parse: `{dateline_body}`"
        )
        return

    # Year-precision in works.yaml but day-precision available in dateline
    if stored_prec == "year" and computed.precision in ("day", "month"):
        report.date_sanity.append(
            f"- `{work_id}` --- works.yaml date `{stored_date}` (precision year) "
            f"but Perseus dateline supplies `{computed.precision}` precision: "
            f"`{dateline_body}` --> suggest `{computed.iso()}` ({computed.precision})"
        )
        return

    # Month-precision stored but day-precision available
    if stored_prec == "month" and computed.precision == "day":
        # Compare months
        stored_m = stored_date[6:8] if len(stored_date) >= 8 else "??"
        try:
            if int(stored_m) != computed.month:
                report.date_sanity.append(
                    f"- `{work_id}` --- works.yaml date `{stored_date}` (month) "
                    f"vs Perseus day-precision `{computed.iso()}`: `{dateline_body}`"
                )
        except ValueError:
            pass
        return

    # Day-precision both: compare
    if stored_prec == "day" and computed.precision == "day":
        if stored_date != computed.iso():
            # Tolerate 1-day-off (different conventions on inclusive count for K/Non/Id)
            try:
                from datetime import date as _date
                sy = -int(stored_date[1:5]) if stored_date.startswith("-") else int(stored_date[:4])
                sm = int(stored_date[6:8])
                sd = int(stored_date[9:11])
                if sy == computed.year and sm == computed.month and abs(sd - computed.day) <= 1:
                    return
            except Exception:  # noqa: BLE001
                pass
            report.date_sanity.append(
                f"- `{work_id}` --- works.yaml `{stored_date}` vs Perseus dateline "
                f"`{dateline_body}` --> computed `{computed.iso()}`"
            )

    # ---------- fallback-only check ----------
    psrc = entry.get("latin_source_url") or ""
    fsrc = entry.get("latin_source_url_fallback") or ""
    if not psrc and "thelatinlibrary" in fsrc:
        report.fallback_only.append(
            f"- `{work_id}` --- no Perseus URL, only Latin Library fallback "
            f"(currently 403): {fsrc}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(DEFAULT_REPORT),
                        help="output markdown report path")
    args = parser.parse_args(argv)

    with WORKS_YAML.open(encoding="utf-8") as f:
        works = yaml.safe_load(f)

    report = AuditReport()
    entries = works if isinstance(works, list) else works.get("works", [])
    for entry in entries:
        audit_entry(entry, REPO_ROOT, report)

    out_path = Path(args.out)
    lines: list[str] = []
    lines.append("# Metadata audit report\n")
    lines.append(f"Generated by `scripts/audit_metadata.py` against `meta/works.yaml` "
                 f"and the Latin files.\n")

    def section(title: str, items: list[str]) -> None:
        lines.append(f"\n## {title} ({len(items)})\n")
        if not items:
            lines.append("None.\n")
            return
        lines.extend(items)
        lines.append("")

    section("Field hygiene (location_written / recipient)", report.field_hygiene)
    section("Date sanity (Perseus dateline vs works.yaml date)", report.date_sanity)
    section("Placeholder Latin files (% PLACEHOLDER)", report.placeholders)
    section("Fallback-only sources (no Perseus, Latin Library 403)",
            report.fallback_only)
    section("Dateline parse failures (script could not parse Perseus dateline)",
            report.parse_failures)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {out_path.relative_to(REPO_ROOT) if out_path.is_absolute() else out_path}")
    print(f"  field_hygiene: {len(report.field_hygiene)}")
    print(f"  date_sanity:   {len(report.date_sanity)}")
    print(f"  placeholders:  {len(report.placeholders)}")
    print(f"  fallback_only: {len(report.fallback_only)}")
    print(f"  parse_failures: {len(report.parse_failures)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
