#!/usr/bin/env python3
"""Pre-process per-work English translation files into hyperlinked copies.

The bound-volume PDF is built from ``english/<category>/<id>.tex`` source
files. Those files carry clean prose with ``\\ciceroSection{N}`` markers and
the occasional ``\\textit{[Greek: transliteration]}``; they do not carry any
hyperref machinery, because the same prose is the source of truth for both
the print PDF and the (Tier 2) web edition.

For the *hyperlinked* PDF (Tier 1, see PLAN.md), we want the prose to carry
clickable internal links: tagged entity surface forms jump to their glossary
entries, cross-references jump to their target sections, Greek phrases with
a recoverable gloss reveal the gloss as a PDF tooltip. None of that is in
the source files.

This module does the wrapping at build time. Given a work entry from
``meta/works.yaml``, it reads ``english/<cat>/<id>.tex``, walks the file
section by section, and emits a transformed copy at
``build/english/<cat>/<id>.tex``:

  * After every ``\\ciceroSection{N}`` it inserts a
    ``\\hypertarget{work-<id>-sec-N}{}`` so other passages can link there.
  * If a cross-reference's ``from_loc`` matches that section, the section
    marker itself is wrapped in a ``\\hyperlink{work-<to_work>-sec-<to_loc>}``
    so a reader can click forward to the target.
  * For each entity mention with ``in`` in (``"eng"``, ``"both"``), the
    first occurrence of the recorded surface form within the section is
    wrapped in ``\\hyperlink{entity-<id>}{<surface>}``. The corresponding
    ``\\hypertarget{entity-<id>}{}`` is emitted by
    ``generate_backmatter.py`` next to the entity's glossary entry.
  * Greek tooltips: if a ``data/greek-phrases.json`` entry for this work
    carries a non-empty ``english_gloss``, a matching
    ``\\textit{[Greek: transliteration]}`` block in the English file is
    wrapped in ``\\ciceroGreekGloss{...}{gloss}`` (defined in preamble.tex).
    None of the v0.3 entries carry a gloss, so this pass is a no-op for now;
    the infrastructure is ready for when glosses are filled in.

The source ``english/`` files are never modified.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
BUILD_ENGLISH = REPO / "build" / "english"

_SECTION_RE = re.compile(r"\\ciceroSection\{([^}]+)\}")


# ----------------------------------------------------------------------
# Sidecar loaders
# ----------------------------------------------------------------------

def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _entity_target(entity_id: str) -> str:
    return "entity-" + entity_id.replace(":", "-")


def _section_target(work_id: str, loc: str) -> str:
    return f"work-{work_id}-sec-{str(loc).replace(':', '-')}"


def _section_anchor_loc(loc: str) -> str:
    """Reduce a sidecar ``loc`` to the leading section number for anchors.

    Sidecar locs look like ``"5"``, ``"5.2"``, ``"5.2-5.4"``, or ``"117-141"``.
    Section anchors land at the integer-section opening, so we strip range and
    sentence parts.
    """
    if not loc:
        return ""
    head = str(loc).split("-", 1)[0]
    head = head.split(".", 1)[0]
    return head.strip()


# ----------------------------------------------------------------------
# Surface-form wrapping
# ----------------------------------------------------------------------

def _wrap_first_surface(
    text: str, surface: str, prefix: str, suffix: str
) -> tuple[str, bool]:
    """Wrap the first non-overlapping occurrence of ``surface`` in ``text``.

    Returns ``(new_text, did_wrap)``. The wrap is word-boundary-aware where
    the surface starts/ends with a word character. To avoid corrupting
    already-emitted hyperlink macros, we never replace inside a substring
    that begins with ``\\hyperlink{`` and runs to its closing ``}``.
    """
    if not surface:
        return text, False

    # Locate all already-wrapped spans we should skip over.
    blocked: list[tuple[int, int]] = []
    i = 0
    while True:
        j = text.find("\\hyperlink{", i)
        if j == -1:
            break
        # find matching close-brace of the wrapper's second arg
        depth = 0
        k = j
        end = -1
        while k < len(text):
            ch = text[k]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    # Closed the entity-id arg; need the second {...}.
                    # Skip whitespace, expect '{'.
                    m = k + 1
                    while m < len(text) and text[m].isspace():
                        m += 1
                    if m < len(text) and text[m] == "{":
                        depth = 1
                        m += 1
                        while m < len(text) and depth:
                            if text[m] == "{":
                                depth += 1
                            elif text[m] == "}":
                                depth -= 1
                            m += 1
                        end = m
                    else:
                        end = k + 1
                    break
            k += 1
        if end == -1:
            break
        blocked.append((j, end))
        i = end

    pattern = re.escape(surface)
    if surface[:1].isalnum() or surface[:1] == "_":
        pattern = r"(?<!\w)" + pattern
    if surface[-1:].isalnum() or surface[-1:] == "_":
        pattern = pattern + r"(?!\w)"

    for m in re.finditer(pattern, text):
        s, e = m.start(), m.end()
        if any(bs <= s < be for bs, be in blocked):
            continue
        return text[:s] + prefix + text[s:e] + suffix + text[e:], True
    return text, False


# ----------------------------------------------------------------------
# Per-section processing
# ----------------------------------------------------------------------

def _split_into_sections(text: str) -> list[tuple[str, str]]:
    """Split ``text`` into ``(section_label, chunk)`` pairs.

    The first chunk's label is ``""`` for any prose preceding the first
    ``\\ciceroSection``. Each subsequent chunk's label is the section number;
    its text begins with the ``\\ciceroSection{N}`` macro itself.
    """
    parts: list[tuple[str, str]] = []
    last = 0
    last_label = ""
    for m in _SECTION_RE.finditer(text):
        parts.append((last_label, text[last:m.start()]))
        last_label = m.group(1).strip()
        last = m.start()
    parts.append((last_label, text[last:]))
    return parts


def _crossref_target_for_loc(
    crossrefs: list[dict[str, Any]], section_label: str, work_id: str
) -> str | None:
    """First crossref originating in this section, returned as an anchor."""
    for ref in crossrefs:
        from_loc = _section_anchor_loc(str(ref.get("from_loc", "")))
        if from_loc == section_label:
            tw_raw = ref.get("to_work", "")
            tw = work_id if tw_raw == "self" else tw_raw
            to_loc = _section_anchor_loc(str(ref.get("to_loc", "")))
            if tw and to_loc:
                return _section_target(tw, to_loc)
    return None


def _process_section(
    work_id: str,
    section_label: str,
    chunk: str,
    mentions_for_section: Iterable[dict[str, Any]],
    crossref_target: str | None,
) -> str:
    """Apply the link transformations to one section's text."""
    if not section_label:
        # Pre-section preamble (file-header comments, etc.); pass through.
        return chunk

    # Replace the leading \ciceroSection{N} with the wrapped + targeted form.
    target = _section_target(work_id, section_label)
    head_re = re.compile(r"\\ciceroSection\{" + re.escape(section_label) + r"\}")
    head_match = head_re.match(chunk)
    if head_match:
        original = head_match.group(0)
        if crossref_target:
            replacement = (
                f"\\hyperlink{{{crossref_target}}}{{{original}}}"
                f"\\hypertarget{{{target}}}{{}}"
            )
        else:
            replacement = original + f"\\hypertarget{{{target}}}{{}}"
        chunk = replacement + chunk[head_match.end():]

    # Wrap entity surface forms. Process unique (surface, entity_id) pairs in
    # document order so the same surface form on a section's second appearance
    # remains plain (a single visible link per surface per section is enough).
    seen: set[tuple[str, str]] = set()
    for mention in mentions_for_section:
        if mention.get("in") not in ("eng", "both"):
            continue
        surface = mention.get("surface") or ""
        eid = mention.get("entity_id") or ""
        if not surface or not eid:
            continue
        key = (surface, eid)
        if key in seen:
            continue
        seen.add(key)
        target_anchor = _entity_target(eid)
        chunk, _ = _wrap_first_surface(
            chunk,
            surface,
            prefix="\\hyperlink{" + target_anchor + "}{",
            suffix="}",
        )

    return chunk


# ----------------------------------------------------------------------
# Greek tooltips
# ----------------------------------------------------------------------

_GREEK_BLOCK_RE = re.compile(
    r"\\textit\{\[Greek:\s*([^\]]+)\]\}"
)


def _apply_greek_tooltips(text: str, greek_entries: list[dict[str, Any]]) -> str:
    """Wrap ``[Greek: x]`` italic blocks with a pdftooltip macro when a gloss
    is on file. v0.3: ``data/greek-phrases.json`` carries no glosses yet, so
    this pass is a no-op in practice; the wrapping is data-driven so it
    activates automatically once glosses are added.
    """
    glossed = [
        e for e in greek_entries
        if (e.get("english_gloss") or "").strip()
    ]
    if not glossed:
        return text

    by_translit: dict[str, str] = {}
    for e in glossed:
        translit = (e.get("transliteration") or "").strip()
        if translit:
            by_translit[translit] = e["english_gloss"].strip()

    def _replace(m: re.Match[str]) -> str:
        translit = m.group(1).strip()
        gloss = by_translit.get(translit)
        if not gloss:
            return m.group(0)
        # Escape braces in the tooltip text minimally; pdftooltip accepts
        # plain text in its second argument.
        gloss_safe = gloss.replace("\\", "").replace("{", "(").replace("}", ")")
        return (
            "\\ciceroGreekGloss{" + m.group(0) + "}{" + gloss_safe + "}"
        )

    return _GREEK_BLOCK_RE.sub(_replace, text)


# ----------------------------------------------------------------------
# Public API
# ----------------------------------------------------------------------

def preprocess_work(work: dict[str, Any]) -> Path | None:
    """Pre-process one work's English file into ``build/english/...``.

    Returns the path of the generated file, or ``None`` if the source file
    does not exist (caller should skip the work).
    """
    src = REPO / work["english_file"]
    if not src.exists():
        return None
    work_id = work["id"]
    category = work["category"]
    rel = Path(work["english_file"]).name  # e.g. 081bc-pro-quinctio.tex
    out = BUILD_ENGLISH / category / rel

    text = src.read_text(encoding="utf-8")

    # Load sidecars once.
    mentions_blob = _load_json(
        DATA / "entities-mentions" / category / rel.replace(".tex", ".json")
    ) or {}
    crossrefs_blob = _load_json(
        DATA / "crossrefs" / category / rel.replace(".tex", ".json")
    ) or {}
    greek_blob = _load_json(DATA / "greek-phrases.json") or {}

    mentions = mentions_blob.get("mentions", []) if isinstance(mentions_blob, dict) else []
    crossrefs = crossrefs_blob.get("refs", []) if isinstance(crossrefs_blob, dict) else []
    greek_entries = [
        e for e in greek_blob.get("entries", [])
        if e.get("work") == work_id
    ]

    # Index mentions by leading section.
    mentions_by_section: dict[str, list[dict[str, Any]]] = {}
    for m in mentions:
        sec = _section_anchor_loc(str(m.get("loc", "")))
        mentions_by_section.setdefault(sec, []).append(m)

    sections = _split_into_sections(text)
    rebuilt: list[str] = []
    for label, chunk in sections:
        crossref_target = (
            _crossref_target_for_loc(crossrefs, label, work_id)
            if label else None
        )
        rebuilt.append(
            _process_section(
                work_id,
                label,
                chunk,
                mentions_by_section.get(label, []),
                crossref_target,
            )
        )
    transformed = "".join(rebuilt)
    transformed = _apply_greek_tooltips(transformed, greek_entries)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(transformed, encoding="utf-8")
    return out


def preprocess_works(works: list[dict[str, Any]]) -> int:
    count = 0
    for w in works:
        if preprocess_work(w) is not None:
            count += 1
    return count


if __name__ == "__main__":
    import argparse
    import sys
    try:
        import yaml
    except ImportError:
        sys.stderr.write("PyYAML required: pip install pyyaml\n")
        raise

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "ids", nargs="*",
        help="Optional list of work IDs to preprocess (default: all drafted)",
    )
    args = parser.parse_args()

    works = yaml.safe_load((REPO / "meta" / "works.yaml").read_text(encoding="utf-8")) or []
    if args.ids:
        wanted = set(args.ids)
        works = [w for w in works if w.get("id") in wanted]
    n = preprocess_works(works)
    print(f"Preprocessed {n} work(s) into {BUILD_ENGLISH.relative_to(REPO)}/")
