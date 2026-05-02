#!/usr/bin/env python3
"""One-shot fix: rewrite the Perseus URLs for philosophy/rhetoric works to
the phi numbers that actually exist in PerseusDL/canonical-latinLit.

The original seed used incorrect / placeholder URLs for most non-letter
non-speech corpora; this script rebuilds them from a verified mapping.
"""
from __future__ import annotations

from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parent.parent
WORKS_YAML = REPO / "meta" / "works.yaml"

# id → (phi number, variant). Verified against PerseusDL/canonical-latinLit
# at the time this script was written.
PHI = {
    "de-inventione":             ("036", "perseus-lat1"),
    "de-oratore":                ("037", "perseus-lat1"),
    "partitiones-oratoriae":     ("038", "perseus-lat1"),
    "brutus":                    ("039", "perseus-lat1"),
    "orator":                    ("040", "perseus-lat1"),
    "de-optimo-genere-oratorum": ("041", "perseus-lat1"),
    "topica":                    ("042", "perseus-lat1"),
    "de-re-publica":             ("043", "perseus-lat1"),
    "academica":                 ("045", "perseus-lat1"),
    "paradoxa-stoicorum":        ("047", "perseus-lat1"),
    "de-finibus":                ("048", "perseus-lat1"),
    "tusculanae-disputationes":  ("049", "perseus-lat1"),
    "de-natura-deorum":          ("050", "perseus-lat1"),
    "cato-maior-de-senectute":   ("051", "perseus-lat1"),
    "laelius-de-amicitia":       ("052", "perseus-lat2"),
    "de-divinatione":            ("053", "perseus-lat1"),
    "de-fato":                   ("054", "perseus-lat1"),
    "de-officiis":               ("055", "perseus-lat1"),
    "timaeus":                   ("072", "perseus-lat1"),
}

# Latin Library fallback for works missing from Perseus, keyed by id
LATIN_LIBRARY_FALLBACK = {
    # De Legibus has 3 books on the Latin Library; the script that fetches
    # it will need to either pick a single book per call or be extended.
    "de-legibus": "https://www.thelatinlibrary.com/cicero/leg1.shtml",
}


def perseus_url(phi: str, variant: str) -> str:
    return (
        f"https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/"
        f"master/data/phi0474/phi{phi}/phi0474.phi{phi}.{variant}.xml"
    )


def main() -> int:
    works = yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []
    n = 0
    for w in works:
        if w["category"] not in {"philosophy", "rhetoric"}:
            continue
        wid = w["id"]
        if wid in PHI:
            phi, variant = PHI[wid]
            w["latin_source_url"] = perseus_url(phi, variant)
            n += 1
        elif wid in LATIN_LIBRARY_FALLBACK:
            w["latin_source_url"] = LATIN_LIBRARY_FALLBACK[wid]
            w["latin_source_url_fallback"] = LATIN_LIBRARY_FALLBACK[wid]
            n += 1
    WORKS_YAML.write_text(
        yaml.safe_dump(works, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(f"updated {n} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
