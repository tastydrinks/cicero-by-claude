#!/usr/bin/env python3
"""Enrich data/letter-network.json with mood and topic tags for the most-read
letters.

This is hand-curated content: a small but growing list of notable letters
where a one-word mood and a few topic tags are worth recording. Run after
scripts/backfill_structural.py to apply the enrichments to whatever the
backfill script produced.

Idempotent: re-running overwrites the same fields. Letters not in the
table here are left untouched.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LN = REPO / "data" / "letter-network.json"

ENRICHMENTS: dict[str, dict[str, object]] = {
    # The exile correspondence
    "ad-atticum-03-03": {
        "mood": "anguished",
        "topics": ["exile", "self-reproach", "atticus's-silence", "journey-south"],
    },
    "ad-atticum-03-07": {
        "mood": "despondent",
        "topics": ["exile", "brundisium", "crossing", "destination-uncertain"],
    },
    "ad-atticum-03-15": {
        "mood": "anguished",
        "topics": ["exile", "self-reproach", "caeci-caeci-fuimus", "thessalonica"],
    },
    "ad-atticum-03-19": {
        "mood": "despondent",
        "topics": ["exile", "thessalonica", "no-news"],
    },
    "ad-atticum-03-22": {
        "mood": "resigned",
        "topics": ["exile", "dyrrachium", "move"],
    },
    "ad-quintum-fratrem-01-03": {
        "mood": "anguished",
        "topics": ["exile", "thessalonica", "mi-frater", "self-reproach"],
    },
    "ad-quintum-fratrem-01-04": {
        "mood": "anguished",
        "topics": ["exile", "thessalonica", "instructions"],
    },
    "ad-familiares-14-01": {
        "mood": "anguished",
        "topics": ["exile", "dyrrachium", "terentia", "vicus-sale"],
    },
    "ad-familiares-14-02": {
        "mood": "anguished",
        "topics": ["exile", "thessalonica", "terentia", "vesta-temple"],
    },
    "ad-familiares-14-03": {
        "mood": "anguished",
        "topics": ["exile", "dyrrachium", "terentia", "self-reproach"],
    },
    "ad-familiares-14-04": {
        "mood": "anguished",
        "topics": ["exile", "brundisium", "terentia", "first-letter-from-exile"],
    },

    # The recovery year (57 BC)
    "ad-atticum-04-01": {
        "mood": "triumphant",
        "topics": ["return-from-exile", "atticus", "second-life"],
    },
    "ad-atticum-04-03": {
        "mood": "anxious",
        "topics": ["clodian-violence", "milo", "sacra-via-ambush"],
    },
    "ad-quintum-fratrem-02-01": {
        "mood": "businesslike",
        "topics": ["senate-proceedings", "campanian-land", "quintus"],
    },

    # Early-56 BC dense political sequence
    "ad-familiares-01-01": {
        "mood": "businesslike",
        "topics": ["egyptian-question", "lentulus-spinther", "senate-report"],
    },
    "ad-familiares-01-02": {
        "mood": "businesslike",
        "topics": ["egyptian-question", "lentulus-spinther"],
    },
    "ad-familiares-01-04": {
        "mood": "businesslike",
        "topics": ["egyptian-question", "lentulus-spinther"],
    },
    "ad-familiares-01-05a": {
        "mood": "businesslike",
        "topics": ["egyptian-question", "lentulus-spinther"],
    },
    "ad-familiares-01-05b": {
        "mood": "anxious",
        "topics": ["egyptian-question", "milo-riot", "pompey-collapse"],
    },
    "ad-quintum-fratrem-02-02": {
        "mood": "hurried",
        "topics": ["dictated", "eye-inflammation", "senate"],
    },
    "ad-quintum-fratrem-02-03": {
        "mood": "anxious",
        "topics": ["milo-riot", "apollo-meeting", "crassus-break"],
    },
    "ad-quintum-fratrem-02-04": {
        "mood": "warm",
        "topics": ["sestius-acquittal", "tyrannio", "tullia-engagement"],
    },

    # The earliest Atticus letters
    "ad-atticum-01-05": {
        "mood": "businesslike",
        "topics": ["estate-business", "tusculanum"],
    },
    "ad-atticum-01-12": {
        "mood": "anxious",
        "topics": ["clodius-bona-dea", "tullia-affairs"],
    },
    "ad-atticum-01-16": {
        "mood": "indignant",
        "topics": ["clodius-bona-dea", "trial", "verdict"],
    },
    "ad-atticum-01-17": {
        "mood": "warm",
        "topics": ["quintus-rebuke", "atticus-friendship"],
    },

    # The 59 BC Vettius affair / closing of book 2
    "ad-atticum-02-19": {
        "mood": "anxious",
        "topics": ["clodius", "caesar-consulship", "vettius"],
    },
    "ad-atticum-02-21": {
        "mood": "anxious",
        "topics": ["caesar-consulship", "popular-feeling"],
    },
    "ad-atticum-02-24": {
        "mood": "alarmed",
        "topics": ["vettius", "caesar"],
    },
    "ad-atticum-02-25": {
        "mood": "businesslike",
        "topics": ["closing-of-book"],
    },
}


def main() -> int:
    if not LN.exists():
        sys.stderr.write(f"data/letter-network.json not found at {LN}\n")
        return 1

    blob = json.loads(LN.read_text(encoding="utf-8"))
    letters = blob.get("letters", [])
    by_id: dict[str, dict] = {l["id"]: l for l in letters if "id" in l}

    n_updated = 0
    for wid, fields in ENRICHMENTS.items():
        if wid in by_id:
            for k, v in fields.items():
                by_id[wid][k] = v
            n_updated += 1
        else:
            sys.stderr.write(f"warning: enrichment target not in letter-network: {wid}\n")

    LN.write_text(
        json.dumps(blob, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Enriched {n_updated} letter(s) with mood/topics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
