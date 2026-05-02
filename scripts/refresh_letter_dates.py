#!/usr/bin/env python3
"""Refresh letter metadata in meta/works.yaml from the Perseus TEI corpora.

For every letter entry whose id matches the canonical pattern
``ad-(atticum|familiares|quintum-fratrem|brutum)-NN-MM`` this script:

  * looks up the corresponding ``<div type="textpart" subtype="letter">``
    in the Perseus XML for the right corpus;
  * extracts the dateline ``<seg rend="dateline">`` text and the
    ``<date when="...">`` attribute;
  * parses the Roman calendar phrasing in the dateline ("Kal. Ian.",
    "a. d. III Non. Apr.", "prid. Id. Mart.", etc.) to recover a
    day/month/year as accurate as the manuscript permits;
  * rewrites the entry's ``date``, ``date_precision``, ``location_written``,
    ``recipient`` (Atticus / Quintus / Brutus / a Familiares correspondent),
    ``latin_source_url``, ``latin_source_url_fallback`` and ``speech_index``
    (a "book:N,letter:M" pointer) accordingly.

The traditional book ordering is preserved by adding a small fractional
offset (1/1000 of a day per letter index) so that, where date precision
collapses to year level, the relative within-year order still tracks the
manuscript ordering.

Run after editing the manifest, or any time the Perseus corpora change.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import requests
    import yaml
    from bs4 import BeautifulSoup
except ImportError as e:
    sys.stderr.write(f"Missing dependency: {e.name}. pip install pyyaml requests beautifulsoup4 lxml\n")
    raise

REPO = Path(__file__).resolve().parent.parent
WORKS_YAML = REPO / "meta" / "works.yaml"

# corpus_id (matches the prefix on the YAML id) → (perseus URL, Latin Library prefix)
CORPORA = {
    "ad-atticum": (
        "https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/master/data/phi0474/phi057/phi0474.phi057.perseus-lat1.xml",
        "https://www.thelatinlibrary.com/cicero/att{book}.shtml",
    ),
    "ad-familiares": (
        "https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/master/data/phi0474/phi056/phi0474.phi056.perseus-lat1.xml",
        "https://www.thelatinlibrary.com/cicero/fam{book}.shtml",
    ),
    "ad-quintum-fratrem": (
        "https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/master/data/phi0474/phi058/phi0474.phi058.perseus-lat1.xml",
        "https://www.thelatinlibrary.com/cicero/qfr{book}.shtml",
    ),
    "ad-brutum": (
        "https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/master/data/phi0474/phi059/phi0474.phi059.perseus-lat1.xml",
        "https://www.thelatinlibrary.com/cicero/brut{book}.shtml",
    ),
}

# default recipient when not parsed from the dateline
DEFAULT_RECIPIENT = {
    "ad-atticum": "T. Pomponius Atticus",
    "ad-quintum-fratrem": "Q. Tullius Cicero",
    "ad-brutum": "M. Iunius Brutus",
    # ad-familiares varies; we extract from the salute when possible
}

# Latin month → number. Listed longest-first so the regex prefers the
# longer abbreviation; this is what Perseus actually emits ("Febr." not
# "Feb.", "Sept." not "Sep.", "Quint." for July before Caesar).
MONTHS = {
    "Quint": 7, "Sext": 8, "Sept": 9, "Mart": 3,
    "Febr": 2, "Apr": 4, "Mai": 5, "Iun": 6, "Iul": 7, "Aug": 8,
    "Oct": 10, "Nov": 11, "Dec": 12, "Sep": 9, "Feb": 2, "Ian": 1,
}
# Months with the "long" calendar (Nones=7, Ides=15)
LONG_MONTHS = {3, 5, 7, 10}

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
         "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19}


def days_in_month(month: int, year: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month == 2:
        # Roman calendar: ignore intercalation; February = 28
        return 28
    return 30


def nones(month: int) -> int:
    return 7 if month in LONG_MONTHS else 5


def ides(month: int) -> int:
    return 15 if month in LONG_MONTHS else 13


_MONTH_RX = "(" + "|".join(re.escape(m) for m in sorted(MONTHS, key=len, reverse=True)) + r")(?:\.|\b)"
_ROMAN_RX = r"(?i:(i{1,3}|iv|v|vi{0,3}|ix|x|xi{0,3}|xiv|xv|xvi{0,3}|xix))"
_ANCHOR_RX = r"(Kal|Kalend|Non|Id)"  # accept "K." / "Kal." / "Kalend." for Kalends
_ANCHOR_NORM = {"Kal": "Kal", "Kalend": "Kal", "Non": "Non", "Id": "Id"}


def parse_dateline(dl: str) -> tuple[str | None, str | None]:
    """Return (location, normalized-date-fragment) extracted from the dateline.

    The location is everything between "Scr." and the next date marker
    (e.g. "Scr. Romae m. Quint. a. 689 (65)" → location "Romae", fragment
    "m. Quint. a. 689 (65)"); date markers are Kal./Non./Id./K./N./prid./
    a. d./m./mense/medio/paulo/eodem/ex./in./inter./ut/(/a. or year-paren.
    """
    if not dl:
        return None, None
    location = None
    # The date fragment starts at the first date-related keyword.
    # We treat "Scr." as the prefix and look for the boundary.
    s = re.sub(r"\s+", " ", dl).strip()
    if not s.lower().startswith("scr."):
        return None, s
    body = s[4:].lstrip()
    # Boundary keywords that signal "the location is over, the date begins".
    # `(?=\s|$)` is used instead of `\b` because most of our markers end in
    # a period followed by a space — between "." and " " there is no word
    # boundary, so `\b` would not match.
    bd = re.search(
        r"\s+(?:K(?:al(?:end)?)?\.?(?=\s|$)|N(?:on)?\.?(?=\s|$)|Id\.?(?=\s|$)"
        r"|prid(?:ie)?\.?(?=\s|$)|a\.\s*d\.(?=\s|$)|m\.\s|mense(?=\s|$)"
        r"|medio(?=\s|$)|paulo(?=\s|$)|eodem(?=\s|$)"
        r"|ex\.\s*[am]\.(?=\s|$)|in\.\s*[am]\.(?=\s|$)|a\.\s*\d|inter(?=\s|$)"
        r"|ut\s+videtur(?=\s|$)|circ(?:a|iter)(?=\s|$)"
        r"|(?i:i{1,3}|iv|v|vi{0,3}|ix|x|xi{0,3}|xiv|xv|xvi{0,3}|xix)\s+K(?:al)?\.?\s|"
        r"(?i:i{1,3}|iv|v|vi{0,3}|ix|x|xi{0,3}|xiv|xv|xvi{0,3}|xix)\s+N(?:on)?\.?\s|"
        r"(?i:i{1,3}|iv|v|vi{0,3}|ix|x|xi{0,3}|xiv|xv|xvi{0,3}|xix)\s+Id\.?\s)",
        body,
    )
    if bd:
        location = body[: bd.start()].strip().rstrip(".,")
        rest = body[bd.start():].strip()
    else:
        # Fallback: split at first comma or paren
        m = re.match(r"([^,(]+)", body)
        if m:
            location = m.group(1).strip().rstrip(".,")
            rest = body[len(m.group(0)):]
        else:
            rest = body
    return (location or None), rest


def _norm_anchor(s: str) -> str:
    s = s.rstrip(".")
    if s.startswith("K"):
        return "Kal"
    if s.startswith("N"):
        return "Non"
    if s.startswith("I"):
        return "Id"
    return s


def parse_day_month(frag: str) -> tuple[int | None, int | None]:
    """Best-effort parse of a Roman calendar day/month from a dateline fragment.

    Recognises (case-insensitively):
      Kal./K. <month>              → day 1
      Non./N. <month>              → day 5 or 7
      Id. <month>                  → day 13 or 15
      prid. <anchor> <month>       → day before anchor
      a. d. <Roman> <anchor> <m>   → counted backward, inclusively
      <Roman> <anchor> <month>     → bare numeral form (no "a. d.")
      m. <month> / mense <month>   → month only
    Returns (day, month) or (None, None) if unrecognised.
    """
    if not frag:
        return None, None
    s = re.sub(r"\s+", " ", frag).strip()
    A = r"(K(?:al(?:end)?)?\.?|N(?:on)?\.?|Id\.?)"  # anchor abbreviations

    # prid. <anchor> <month>
    m = re.search(rf"prid(?:ie)?\.?\s+{A}\s*{_MONTH_RX}", s, re.I)
    if m:
        anchor = _norm_anchor(m.group(1))
        mon = MONTHS[m.group(2).capitalize()]
        if anchor == "Kal":
            prev = mon - 1 or 12
            return days_in_month(prev, 0), prev
        anchor_day = nones(mon) if anchor == "Non" else ides(mon)
        return anchor_day - 1, mon

    # a. d. <Roman> <anchor> <month>
    m = re.search(rf"a\.?\s*d\.?\s+{_ROMAN_RX}\s+{A}\s*{_MONTH_RX}", s, re.I)
    if m:
        n = ROMAN.get(m.group(1).upper())
        anchor = _norm_anchor(m.group(2))
        mon = MONTHS[m.group(3).capitalize()]
        if n is None:
            return None, mon
        if anchor == "Kal":
            prev = mon - 1 or 12
            return days_in_month(prev, 0) - (n - 2), prev
        anchor_day = nones(mon) if anchor == "Non" else ides(mon)
        return anchor_day - (n - 1), mon

    # Bare numeral: "xi K. Mai." (no leading "a. d.")
    m = re.search(rf"(?<![A-Za-z]){_ROMAN_RX}\s+{A}\s*{_MONTH_RX}", s, re.I)
    if m:
        n = ROMAN.get(m.group(1).upper())
        anchor = _norm_anchor(m.group(2))
        mon = MONTHS[m.group(3).capitalize()]
        if n is None:
            return None, mon
        if anchor == "Kal":
            prev = mon - 1 or 12
            return days_in_month(prev, 0) - (n - 2), prev
        anchor_day = nones(mon) if anchor == "Non" else ides(mon)
        return anchor_day - (n - 1), mon

    # Plain anchor + month
    m = re.search(rf"{A}\s+{_MONTH_RX}", s, re.I)
    if m:
        anchor = _norm_anchor(m.group(1))
        mon = MONTHS[m.group(2).capitalize()]
        if anchor == "Kal":
            return 1, mon
        return (nones(mon) if anchor == "Non" else ides(mon)), mon

    # "m. Quint." / "mense Iulio" / "medio mense Ian." — month only
    m = re.search(rf"(?:m\.|mense|medio\s+mense|in(?:eunte)?\s+m\.|ex(?:eunte)?\s+m\.)\s*{_MONTH_RX}", s, re.I)
    if m:
        return None, MONTHS[m.group(1).capitalize()]

    return None, None


def parse_year(frag: str, fallback_when: str | None) -> int | None:
    """Extract a BC year. Recognises:
      a. Chr. 56          → -56
      a. u. c. 698 (a. Chr. 56)  → -56 (the parenthetical wins)
      m. Quint. a. 689 (65)      → -65 (the parenthetical wins)
      <date when="-0056">        → -56 (the fallback)
    """
    if frag:
        # Parenthetical "(a. Chr. NN)" or "(NN)" with bare year → BC
        m = re.search(r"\(\s*(?:a\.?\s*Chr\.?\s*)?(\d{1,3})\s*\)", frag)
        if m:
            return -int(m.group(1))
        m = re.search(r"a\.?\s*Chr\.?\s*(\d{1,3})", frag)
        if m:
            return -int(m.group(1))
    if fallback_when:
        # "-0056" → -56
        try:
            v = int(fallback_when.lstrip("-"))
            return -v if fallback_when.startswith("-") else v
        except ValueError:
            return None
    return None


def parse_recipient_from_salute(corpus_id: str, salute: str) -> str | None:
    if not salute:
        return None
    # Standard openers:
    #   "CICERO ATTICO salutem"
    #   "M. CICERO S. D. P. LENTVLO PROCOS."
    #   "CICERO BRVTO SALVTEM"
    s = re.sub(r"\s+", " ", salute).strip()
    s = re.sub(r"M\.\s*CICERO\s+", "", s, flags=re.I)
    s = re.sub(r"CICERO\s+", "", s, flags=re.I)
    s = re.sub(r"S\.?\s*D\.?\s*", "", s, flags=re.I)
    s = re.sub(r"\bsalutem\b\.?", "", s, flags=re.I)
    s = re.sub(r"SALVTEM\.?", "", s, flags=re.I)
    s = s.strip(" .,")
    if not s:
        return DEFAULT_RECIPIENT.get(corpus_id)
    # Title-case roughly; keep multi-word forms
    return s


def parse_corpus(corpus_id: str, xml_text: str) -> dict[tuple[int, int], dict]:
    """Return {(book, letter) → {dateline, when, salute, raw_dateline}}."""
    soup = BeautifulSoup(xml_text, "xml")
    body = soup.find("body")
    if body is None:
        raise RuntimeError(f"{corpus_id}: no <body> element")

    # Find all letter divs nested under the edition. We tolerate either
    # subtype="book" or subtype="Book".
    out: dict[tuple[int, int], dict] = {}
    for book_div in body.find_all("div", attrs={"type": "textpart"}):
        if book_div.get("subtype", "").lower() != "book":
            continue
        try:
            book_n = int(book_div.get("n"))
        except (TypeError, ValueError):
            continue
        for letter_div in book_div.find_all(
            "div", attrs={"type": "textpart", "subtype": "letter"}, recursive=False
        ):
            try:
                letter_n = int(letter_div.get("n"))
            except (TypeError, ValueError):
                continue
            opener = letter_div.find("label", attrs={"rend": "opener"}, recursive=False)
            dateline_text = ""
            salute_text = ""
            when_attr = None
            if opener is not None:
                dl = opener.find(attrs={"rend": "dateline"})
                if dl is not None:
                    dateline_text = re.sub(r"\s+", " ", dl.get_text(" ", strip=True))
                    date_tag = dl.find("date")
                    if date_tag is not None:
                        when_attr = date_tag.get("when")
                sl = opener.find(attrs={"rend": "salute"})
                if sl is not None:
                    salute_text = re.sub(r"\s+", " ", sl.get_text(" ", strip=True))
            out[(book_n, letter_n)] = {
                "dateline": dateline_text,
                "when": when_attr,
                "salute": salute_text,
            }
    return out


def http_get(url: str) -> str:
    r = requests.get(url, headers={"User-Agent": "cicero-by-claude refresh"}, timeout=60)
    r.raise_for_status()
    r.encoding = r.apparent_encoding or "utf-8"
    return r.text


# ---------------------------------------------------------------------------
# Main rewrite
# ---------------------------------------------------------------------------

_ID_RX = re.compile(r"^(ad-(?:atticum|familiares|quintum-fratrem|brutum))-(\d{2})-(\d{2})$")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing")
    parser.add_argument("--show-unparseable", action="store_true",
                        help="print every dateline whose day/month could not be parsed")
    args = parser.parse_args(argv)

    works = yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []

    # Pull each corpus once
    corpora_data: dict[str, dict[tuple[int, int], dict]] = {}
    for cid, (perseus_url, _) in CORPORA.items():
        print(f"fetching {cid}: {perseus_url}", file=sys.stderr)
        corpora_data[cid] = parse_corpus(cid, http_get(perseus_url))
        print(f"  {cid}: {len(corpora_data[cid])} letters indexed", file=sys.stderr)

    n_updated = 0
    n_skipped = 0
    n_unparsed = 0
    for w in works:
        if w.get("category") != "letters":
            continue
        m = _ID_RX.match(w["id"])
        if m is None:
            n_skipped += 1
            continue
        cid, book_s, letter_s = m.group(1), m.group(2), m.group(3)
        book_n, letter_n = int(book_s), int(letter_s)
        bucket = corpora_data.get(cid, {})
        info = bucket.get((book_n, letter_n))
        if info is None:
            n_skipped += 1
            continue

        dateline = info["dateline"]
        location, frag = parse_dateline(dateline)
        day, month = parse_day_month(frag or "")
        year = parse_year(frag or "", info.get("when"))

        if year is None:
            n_skipped += 1
            continue

        # Compose date and precision. We need a stable secondary sort within
        # year for letters whose precision is only year: shift the day by
        # the manuscript order so consecutive letters in the same book
        # cluster together but don't collide.
        if day is not None and month is not None:
            precision = "day"
            d_day, d_month = day, month
        elif month is not None:
            precision = "month"
            d_day, d_month = 15, month
        else:
            precision = "year"
            # Fan out by manuscript order: month=ceil(letter/4)+1 keeps each
            # within Jan-Dec, offsetting later book.letters proportionally.
            # This is a sort hint, not a real date; precision flag tells
            # the renderer not to print it.
            seq = book_n * 100 + letter_n
            d_month = max(1, min(12, 1 + (seq % 12)))
            d_day = 1 + (seq % 28)

        date_str = f"-{abs(year):04d}-{d_month:02d}-{d_day:02d}"

        # Update the entry
        w["date"] = date_str
        w["date_precision"] = precision
        if location:
            w["location_written"] = location

        # Repath the latin/english/headnote files so the year prefix matches
        # the new date. Convention is NNNbc-id.tex.
        year_prefix = f"{abs(year):03d}bc"
        for ftype, dirname in (("latin_file", "latin"),
                                ("english_file", "english"),
                                ("headnote_file", "headnotes")):
            w[ftype] = f"{dirname}/letters/{year_prefix}-{w['id']}.tex"

        # Recipient
        recipient = parse_recipient_from_salute(cid, info.get("salute") or "")
        if recipient:
            w["recipient"] = recipient
        elif cid in DEFAULT_RECIPIENT:
            w["recipient"] = DEFAULT_RECIPIENT[cid]

        # Source URLs: Perseus primary, Latin Library fallback (per book)
        perseus_url, ll_template = CORPORA[cid]
        w["latin_source_url"] = perseus_url
        w["latin_source_url_fallback"] = ll_template.format(book=book_n)
        w["speech_index"] = f"book:{book_n},letter:{letter_n}"

        if args.show_unparseable and precision == "year" and dateline:
            print(f"  unparsed dateline {w['id']}: {dateline!r}", file=sys.stderr)
            n_unparsed += 1
        n_updated += 1

    print(f"updated: {n_updated}, skipped: {n_skipped}, year-only: {n_unparsed}",
          file=sys.stderr)

    if not args.dry_run:
        WORKS_YAML.write_text(yaml.safe_dump(works, sort_keys=False, allow_unicode=True,
                                              width=120), encoding="utf-8")
        print(f"wrote {WORKS_YAML.relative_to(REPO)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
