#!/usr/bin/env python3
"""Validate meta/works.yaml and the file system layout.

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

Exits non-zero on errors. Warnings (e.g. pending entries lacking files) are
printed but do not fail the run.
"""
from __future__ import annotations

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
