#!/usr/bin/env python3
"""Validate meta/works.yaml, the file system layout, and the data/ sidecars.

Checks:
  - YAML parses
  - Every entry has the required fields with valid types
  - No duplicate ids
  - Dates parse
  - File path conventions match (latin/<cat>/NNN(ad|bc)-<id>.tex)
  - Categories are one of: speeches, rhetoric, philosophy, letters
  - Status is one of: pending, drafted, reviewed, final
  - Every work with status != pending has all three of its files on disk
  - Every Latin file under latin/ corresponds to an entry in works.yaml

Sidecar checks (data/, see data/SCHEMA.md):
  - Corpus-wide files (greek-phrases.json, letter-network.json,
    entities.json) are well-formed JSON with schema_version: 1
  - Every per-work sidecar's id matches a works.yaml id
  - Every work-reference in a corpus-wide sidecar resolves in works.yaml
  - Every entity-id reference resolves in entities.json (when populated)
  - Drafted works that lack a parallel-corpus sidecar emit a warning

Exits non-zero on errors. Warnings (e.g. pending entries lacking files) are
printed but do not fail the run.
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

REQUIRED_FIELDS = (
    "id", "title_latin", "title_english", "category", "date",
    "date_precision", "latin_file", "english_file", "headnote_file",
    "status",
)
VALID_CATEGORIES = {"speeches", "rhetoric", "philosophy", "letters"}
VALID_STATUSES = {"pending", "drafted", "reviewed", "final"}
VALID_PRECISIONS = {"day", "month", "year", "year_range"}

_FILENAME_RE = re.compile(r"^(\d{3,4})(bc|ad)-([a-z0-9-]+)\.tex$")


def parse_date(s: str) -> tuple[int, int, int]:
    if s.startswith("-"):
        ys, rest = s[1:].split("-", 1)
        return -int(ys), *(int(p) for p in rest.split("-"))  # type: ignore[return-value]
    ys, rest = s.split("-", 1)
    return int(ys), *(int(p) for p in rest.split("-"))  # type: ignore[return-value]


def main() -> int:
    if not WORKS_YAML.exists():
        sys.stderr.write(f"meta/works.yaml not found at {WORKS_YAML}\n")
        return 2

    works: list[dict[str, Any]] = yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []
    errors: list[str] = []
    warnings: list[str] = []

    seen_ids: set[str] = set()
    seen_latin: set[str] = set()

    for i, w in enumerate(works):
        prefix = f"works[{i}] (id={w.get('id', '?')})"

        # required fields
        for field in REQUIRED_FIELDS:
            if field not in w:
                errors.append(f"{prefix}: missing required field {field!r}")

        # uniqueness
        wid = w.get("id")
        if wid in seen_ids:
            errors.append(f"{prefix}: duplicate id {wid!r}")
        if wid:
            seen_ids.add(wid)

        # categories / statuses / precisions
        if w.get("category") not in VALID_CATEGORIES:
            errors.append(f"{prefix}: invalid category {w.get('category')!r}")
        if w.get("status") not in VALID_STATUSES:
            errors.append(f"{prefix}: invalid status {w.get('status')!r}")
        if w.get("date_precision") not in VALID_PRECISIONS:
            errors.append(f"{prefix}: invalid date_precision {w.get('date_precision')!r}")

        # date parses
        try:
            parse_date(w["date"])
        except Exception as e:
            errors.append(f"{prefix}: date does not parse: {e}")

        # filename convention
        for ftype in ("latin_file", "english_file", "headnote_file"):
            path = w.get(ftype)
            if not path:
                continue
            name = Path(path).name
            m = _FILENAME_RE.match(name)
            if not m:
                errors.append(
                    f"{prefix}: {ftype} filename does not match NNN(bc|ad)-id.tex: {name}"
                )

        # collect latin paths for orphan-file scan
        if w.get("latin_file"):
            seen_latin.add(w["latin_file"])

        # files must exist for non-pending statuses
        if w.get("status") in {"drafted", "reviewed", "final"}:
            for ftype in ("latin_file", "english_file", "headnote_file"):
                path = REPO / w[ftype]
                if not path.exists():
                    errors.append(
                        f"{prefix}: status={w['status']} but {ftype} missing: {w[ftype]}"
                    )

    # orphan-file scan: every latin file on disk must be in the manifest
    for latin_dir in (REPO / "latin").rglob("*.tex"):
        rel = str(latin_dir.relative_to(REPO))
        if rel not in seen_latin:
            warnings.append(f"orphan Latin file (not in works.yaml): {rel}")

    # Chronological-gap check: every pending work that is dated earlier than
    # the latest-dated `drafted` work means a future session should pick it
    # up, not skip past it. This is here to prevent silent category-skipping
    # of the kind that left letters un-translated for several sessions.
    # The DEFERRED set excludes works that are deliberately on hold:
    #  - Aratea (86 BC) and De Inventione (85 BC), the two pre-Pro-Quinctio
    #    works skipped because Pro Quinctio was the agreed test case.
    #  - The five fragmentary works whose Latin is not in the Perseus corpus
    #    and which need a manual source: de-consulatu-suo (60 BC),
    #    de-temporibus-suis (54 BC), hortensius (45 BC), consolatio (45 BC).
    #    (Aratea is also no_perseus.) These will be picked up when their
    #    Latin sources are supplied; meanwhile they should not block the
    #    chronological catch-up.
    DEFERRED = {
        "aratea", "de-inventione",
        "de-consulatu-suo", "de-temporibus-suis", "hortensius", "consolatio",
    }
    drafted = [w for w in works if w.get("status") in {"drafted", "reviewed", "final"}]
    pending = [w for w in works if w.get("status") == "pending" and w.get("id") not in DEFERRED]
    if drafted and pending:
        try:
            latest_drafted = max(drafted, key=lambda w: parse_date(w["date"]))
            latest_drafted_key = parse_date(latest_drafted["date"])
            earlier_pending = [
                w for w in pending if parse_date(w["date"]) < latest_drafted_key
            ]
            if earlier_pending:
                # Show a representative sample, not all of them.
                warnings.append(
                    f"chronological gap: {len(earlier_pending)} pending work(s) dated "
                    f"earlier than the latest drafted work "
                    f"({latest_drafted['id']}, {latest_drafted['date']})"
                )
                for w in earlier_pending[:5]:
                    warnings.append(
                        f"  earlier-pending: {w['date']} {w['category']:9s} {w['id']}"
                    )
                if len(earlier_pending) > 5:
                    warnings.append(f"  ... and {len(earlier_pending) - 5} more")
        except Exception:
            # Defensive: don't fail validation if dates are mid-edit
            pass

    # ----------------------------------------------------------------
    # Sidecar checks (data/, see data/SCHEMA.md)
    # ----------------------------------------------------------------
    work_ids: set[str] = {w["id"] for w in works if "id" in w}
    drafted_ids: set[str] = {
        w["id"] for w in works
        if w.get("status") in {"drafted", "reviewed", "final"} and "id" in w
    }

    def _load_json(path: Path) -> Any:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return None
        except json.JSONDecodeError as e:
            errors.append(f"data/{path.relative_to(DATA)}: invalid JSON: {e}")
            return None

    if DATA.exists():
        # Corpus-wide files
        for fname, list_key in (
            ("greek-phrases.json", "entries"),
            ("letter-network.json", "letters"),
            ("entities.json", "entities"),
        ):
            p = DATA / fname
            blob = _load_json(p)
            if blob is None:
                continue
            if blob.get("schema_version") != 1:
                errors.append(f"data/{fname}: missing or non-1 schema_version")
            items = blob.get(list_key, [])
            if not isinstance(items, list):
                errors.append(f"data/{fname}: top-level {list_key!r} is not a list")
                continue

        # Greek phrase work-id reconciliation
        gp = _load_json(DATA / "greek-phrases.json") or {}
        for entry in gp.get("entries", []):
            if entry.get("work") and entry["work"] not in work_ids:
                errors.append(
                    f"data/greek-phrases.json: entry {entry.get('id')!r} "
                    f"references unknown work {entry['work']!r}"
                )

        # Letter-network work-id reconciliation
        ln = _load_json(DATA / "letter-network.json") or {}
        ln_letter_ids: set[str] = set()
        for entry in ln.get("letters", []):
            wid = entry.get("id")
            if wid not in work_ids:
                errors.append(
                    f"data/letter-network.json: unknown letter id {wid!r}"
                )
            else:
                ln_letter_ids.add(wid)

        # Entity registry: collect IDs for cross-reference
        ent = _load_json(DATA / "entities.json") or {}
        entity_ids: set[str] = {
            e.get("id") for e in ent.get("entities", []) if isinstance(e, dict)
        }

        # Per-work sidecars: each id must match a works.yaml entry
        for sidecar_dir, list_key in (
            ("parallel", "segments"),
            ("entities-mentions", "mentions"),
            ("crossrefs", "refs"),
            ("allusions", "allusions"),
            ("glossary", "notes"),
        ):
            d = DATA / sidecar_dir
            if not d.exists():
                continue
            for json_path in d.rglob("*.json"):
                blob = _load_json(json_path)
                if blob is None:
                    continue
                if blob.get("schema_version") != 1:
                    errors.append(
                        f"data/{json_path.relative_to(DATA)}: "
                        f"missing or non-1 schema_version"
                    )
                wid = blob.get("id")
                if wid not in work_ids:
                    errors.append(
                        f"data/{json_path.relative_to(DATA)}: "
                        f"id {wid!r} does not match any works.yaml entry"
                    )
                # Entity-id reference checks (when entities.json is populated)
                if entity_ids and sidecar_dir in ("entities-mentions",
                                                   "glossary"):
                    items = blob.get(list_key, [])
                    for item in items:
                        eid = item.get("entity_id") if isinstance(item, dict) else None
                        if eid and eid not in entity_ids:
                            warnings.append(
                                f"data/{json_path.relative_to(DATA)}: "
                                f"unknown entity_id {eid!r}"
                            )
                # Crossref to_work resolution
                if sidecar_dir == "crossrefs":
                    for ref in blob.get("refs", []):
                        tw = ref.get("to_work") if isinstance(ref, dict) else None
                        if tw and tw != "self" and tw not in work_ids:
                            errors.append(
                                f"data/{json_path.relative_to(DATA)}: "
                                f"crossref to unknown work {tw!r}"
                            )

        # Drafted-work parallel-sidecar coverage warning
        parallel_have: set[str] = set()
        pdir = DATA / "parallel"
        if pdir.exists():
            for json_path in pdir.rglob("*.json"):
                try:
                    blob = json.loads(json_path.read_text(encoding="utf-8"))
                    if isinstance(blob, dict) and "id" in blob:
                        parallel_have.add(blob["id"])
                except (json.JSONDecodeError, OSError):
                    pass
        missing_parallel = drafted_ids - parallel_have
        if missing_parallel:
            warnings.append(
                f"parallel-sidecar coverage: {len(missing_parallel)} drafted "
                f"work(s) lack a data/parallel/ sidecar (run "
                f"scripts/backfill_structural.py)"
            )
            for wid in sorted(missing_parallel)[:5]:
                warnings.append(f"  missing-parallel: {wid}")
            if len(missing_parallel) > 5:
                warnings.append(f"  ... and {len(missing_parallel) - 5} more")

        # Letter-network coverage warning
        drafted_letters = {
            w["id"] for w in works
            if w.get("status") in {"drafted", "reviewed", "final"}
            and w.get("category") == "letters"
        }
        missing_letter_net = drafted_letters - ln_letter_ids
        if missing_letter_net:
            warnings.append(
                f"letter-network coverage: {len(missing_letter_net)} drafted "
                f"letter(s) missing from data/letter-network.json"
            )

    if warnings:
        for w in warnings:
            print(f"warning: {w}")
    if errors:
        for e in errors:
            sys.stderr.write(f"error: {e}\n")
        sys.stderr.write(f"\n{len(errors)} error(s), {len(warnings)} warning(s)\n")
        return 1

    print(f"OK: {len(works)} entries, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
