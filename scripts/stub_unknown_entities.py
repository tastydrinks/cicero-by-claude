#!/usr/bin/env python3
"""Generate stub entries in data/entities.json for any entity_id referenced
in a sidecar but missing from the registry.

Used to clean up after a polishing-pass session that produced lots of
entity_id references without populating the registry. The script:

  1. Scans data/{entities-mentions,glossary,crossrefs,allusions}/ for
     entity_id references.
  2. Identifies any id not present in data/entities.json.
  3. For each missing id, derives a canonical_name and aliases from the
     surface/anchor strings in the sidecars where it appears.
  4. Determines the type from the id prefix (person:..., place:..., etc.).
  5. Picks first_appearance from the chronologically-earliest work the id
     appears in.
  6. Writes a stub entry with summary="(stub - to be enriched)".

The stubs satisfy the validator and the build's glossary lookup. A later
enrichment pass should fill in summaries and external_ids by hand or with
research help.

Idempotent: only adds entries that don't already exist.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    raise

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
WORKS_YAML = REPO / "meta" / "works.yaml"


def parse_date(s: str) -> tuple[int, int, int]:
    if s.startswith("-"):
        ys, rest = s[1:].split("-", 1)
        year = -int(ys)
    else:
        ys, rest = s.split("-", 1)
        year = int(ys)
    m, d = rest.split("-")
    return year, int(m), int(d)


def main() -> int:
    works = yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []
    work_date = {w["id"]: parse_date(w["date"]) for w in works if "id" in w}

    entities_blob = json.loads((DATA / "entities.json").read_text(encoding="utf-8"))
    known = {e["id"] for e in entities_blob.get("entities", [])}

    # surface_forms[entity_id] = Counter({surface: count})
    surface_forms: dict[str, Counter] = {}
    work_appearances: dict[str, list[tuple[tuple[int, int, int], str]]] = {}

    def record(eid: str, surface: str, work_id: str) -> None:
        if eid in known:
            return
        surface_forms.setdefault(eid, Counter())[surface] += 1
        wd = work_date.get(work_id, (9999, 1, 1))
        work_appearances.setdefault(eid, []).append((wd, work_id))

    for sub, list_key, surface_key in (
        ("entities-mentions", "mentions", "surface"),
        ("glossary", "notes", "anchor"),
        ("crossrefs", "refs", None),
        ("allusions", "allusions", "surface"),
    ):
        d = DATA / sub
        if not d.exists():
            continue
        for jp in d.rglob("*.json"):
            try:
                blob = json.loads(jp.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            wid = blob.get("id", "")
            for item in blob.get(list_key, []):
                if not isinstance(item, dict):
                    continue
                eid = item.get("entity_id")
                if not eid:
                    continue
                surface = item.get(surface_key, "") if surface_key else ""
                record(eid, surface, wid)

    new_entries: list[dict] = []
    for eid, surfaces in sorted(surface_forms.items()):
        type_ = eid.split(":", 1)[0] if ":" in eid else "person"
        # Canonical name = most common non-empty surface, else id-derived.
        non_empty = [(s, n) for s, n in surfaces.items() if s.strip()]
        if non_empty:
            non_empty.sort(key=lambda x: -x[1])
            canonical = non_empty[0][0]
            aliases = [s for s, _ in non_empty[1:] if s != canonical]
        else:
            slug = eid.split(":", 1)[1] if ":" in eid else eid
            canonical = slug.replace("-", " ").title()
            aliases = []

        appearances = sorted(work_appearances[eid])
        first_app = appearances[0][1] if appearances else ""

        new_entries.append({
            "id": eid,
            "type": type_,
            "canonical_name": canonical,
            "short_name": canonical,
            "aliases": aliases,
            "external_ids": {},
            "summary": "(stub --- to be enriched)",
            "first_appearance": first_app,
            "categories": [],
        })

    # Combine and sort
    all_entries = entities_blob.get("entities", []) + new_entries
    all_entries.sort(key=lambda e: (e.get("type", ""), e["id"]))

    out = {"schema_version": 1, "entities": all_entries}
    (DATA / "entities.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Existing entities: {len(known)}")
    print(f"New stubs added: {len(new_entries)}")
    print(f"Total entities: {len(all_entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
