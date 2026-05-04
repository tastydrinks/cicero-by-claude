#!/usr/bin/env python3
"""Generate ``build/backmatter-generated.tex`` from data/ sidecars.

The bound volume can be built in three reader-selectable profiles. This script
emits the profile-appropriate apparatus into a single LaTeX file that
``build/backmatter.tex`` then ``\\input``s.

Profiles (see build/PROFILES.md):

  reading  — default. No generated apparatus.
  study    — adds: glossary of names, Greek-phrase catalogue, letter-network
             appendix.
  scholar  — adds the study sections plus: cross-reference index, allusion
             apparatus, translator's-notes appendix.

Run after ``scripts/backfill_structural.py`` (or after a translation session
that emitted new sidecars).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    raise

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
WORKS_YAML = REPO / "meta" / "works.yaml"
OUT = REPO / "build" / "backmatter-generated.tex"

PROFILES = ("reading", "study", "scholar")

_TEX_REPLACEMENTS = {
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    "\\": r"\textbackslash{}",
}


def tex_escape(s: str) -> str:
    return "".join(_TEX_REPLACEMENTS.get(c, c) for c in (s or ""))


def entity_hyperlink_target(entity_id: str) -> str:
    """Stable hyperref anchor name for an entity_id.

    Entity IDs are kebab-case slugs prefixed with type, separated by a colon
    (e.g. ``person:cicero``). hyperref names treat ``:`` as ordinary, but for
    durability across PDF readers we replace it with ``-``. The ``entity-``
    prefix scopes the namespace so entity anchors don't collide with section
    anchors (``work-...``) or other targets.
    """
    return "entity-" + entity_id.replace(":", "-")


def section_hyperlink_target(work_id: str, loc: str) -> str:
    """Stable anchor for a section within a work."""
    safe_loc = str(loc).replace(":", "-")
    return f"work-{work_id}-sec-{safe_loc}"


def _section_anchor_loc(loc: str) -> str:
    """Extract a single section number for anchor purposes.

    crossrefs and other sidecars carry locs like ``"5"``, ``"5.2"``,
    ``"5.2-5.4"``, or ``"117-141"``. Section anchors are placed at the
    integer-section opening (``\\ciceroSection{N}``), so we resolve any of
    those forms back to the leading section number for the link target.
    """
    if not loc:
        return ""
    head = str(loc).split("-", 1)[0]
    head = head.split(".", 1)[0]
    return head.strip()


def parse_date(s: str) -> tuple[int, int, int]:
    if s.startswith("-"):
        ys, rest = s[1:].split("-", 1)
        year = -int(ys)
    else:
        ys, rest = s.split("-", 1)
        year = int(ys)
    m, d = rest.split("-")
    return year, int(m), int(d)


def short_year(date: str) -> str:
    y, _, _ = parse_date(date)
    return f"{abs(y)} BC" if y < 0 else f"{y} AD"


# ----------------------------------------------------------------------
# Loaders
# ----------------------------------------------------------------------

def load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def load_works() -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    works = yaml.safe_load(WORKS_YAML.read_text(encoding="utf-8")) or []
    return works, {w["id"]: w for w in works if "id" in w}


# ----------------------------------------------------------------------
# Section emitters
# ----------------------------------------------------------------------

def emit_glossary(works_by_id: dict[str, dict[str, Any]]) -> str:
    """Emit a glossary chapter from data/entities.json + data/glossary/."""
    entities_blob = load_json(DATA / "entities.json") or {}
    entities = {
        e["id"]: e
        for e in entities_blob.get("entities", [])
        if isinstance(e, dict) and "id" in e
    }
    # Aggregate glossary notes per entity_id (when one is set).
    notes_by_entity: dict[str, list[dict[str, Any]]] = defaultdict(list)
    glossary_dir = DATA / "glossary"
    if glossary_dir.exists():
        for jp in sorted(glossary_dir.rglob("*.json")):
            blob = load_json(jp) or {}
            wid = blob.get("id", "?")
            for note in blob.get("notes", []):
                eid = note.get("entity_id")
                if eid:
                    notes_by_entity[eid].append({**note, "work": wid})

    if not entities and not notes_by_entity:
        return (
            "\\chapter*{Glossary of names}\n"
            "\\addcontentsline{toc}{chapter}{Glossary of names}\n"
            "\\markboth{Glossary of names}{Glossary of names}\n\n"
            "\\noindent\n\\textit{The glossary will populate as named "
            "entities are tagged across the corpus.}\n\n"
        )

    lines = [
        "\\chapter*{Glossary of names}",
        "\\addcontentsline{toc}{chapter}{Glossary of names}",
        "\\markboth{Glossary of names}{Glossary of names}",
        "",
        "\\begin{description}",
    ]
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in entities.values():
        by_type[e.get("type", "other")].append(e)
    for etype in sorted(by_type):
        for entity in sorted(by_type[etype], key=lambda x: x.get("canonical_name", "")):
            eid = entity["id"]
            target = entity_hyperlink_target(eid)
            name = tex_escape(entity.get("canonical_name", eid))
            summary = tex_escape(entity.get("summary", ""))
            aliases = entity.get("aliases", []) or []
            alias_str = ""
            if aliases:
                alias_str = " (" + ", ".join(
                    "\\textit{" + tex_escape(a) + "}" for a in aliases
                ) + ")"
            lines.append(
                f"  \\item[\\hypertarget{{{target}}}{{}}{name}]{alias_str} {summary}"
            )
    lines.append("\\end{description}")
    lines.append("")
    return "\n".join(lines)


def emit_greek_catalogue(works_by_id: dict[str, dict[str, Any]]) -> str:
    blob = load_json(DATA / "greek-phrases.json") or {}
    entries = blob.get("entries", [])
    if not entries:
        return ""
    lines = [
        "\\chapter*{Cicero's Greek}",
        "\\addcontentsline{toc}{chapter}{Cicero's Greek}",
        "\\markboth{Cicero's Greek}{Cicero's Greek}",
        "",
        "\\noindent",
        f"Cicero salts his prose --- especially the letters --- with Greek "
        f"phrases of every register: technical, jocular, literary, "
        f"euphemistic. {len(entries)} Greek occurrences are catalogued here, "
        f"with their work and section, the meaning where it is recoverable, "
        f"and the source where one is suspected.",
        "",
        "\\begin{longtable}{p{0.30\\textwidth}p{0.20\\textwidth}p{0.42\\textwidth}}",
        "\\textbf{Greek} & \\textbf{Locus} & \\textbf{Gloss / source} \\\\",
        "\\hline",
    ]
    for e in entries:
        wid = e.get("work", "")
        loc = tex_escape(e.get("loc", ""))
        work_label = ""
        if wid in works_by_id:
            wl = works_by_id[wid]
            work_label = tex_escape(wl.get("title_english", wid))
        else:
            work_label = tex_escape(wid)
        greek = tex_escape(e.get("greek_original") or e.get("transliteration", ""))
        gloss = tex_escape(e.get("english_gloss", "") or "")
        src = e.get("suspected_source") or ""
        gloss_src = gloss
        if src:
            gloss_src = (gloss + (" --- " if gloss else "") + tex_escape(src)).strip()
        lines.append(f"{greek} & {work_label} {loc} & {gloss_src} \\\\")
    lines.append("\\end{longtable}")
    lines.append("")
    return "\n".join(lines)


def emit_letter_network(works_by_id: dict[str, dict[str, Any]]) -> str:
    blob = load_json(DATA / "letter-network.json") or {}
    letters = blob.get("letters", [])
    if not letters:
        return ""
    lines = [
        "\\chapter*{Letter network}",
        "\\addcontentsline{toc}{chapter}{Letter network}",
        "\\markboth{Letter network}{Letter network}",
        "",
        "\\noindent",
        f"Cicero's correspondence as a graph: sender, recipient, place "
        f"written, date, length. {len(letters)} letters are tabulated below, "
        f"in chronological order.",
        "",
        "\\begin{longtable}{p{0.20\\textwidth}p{0.18\\textwidth}p{0.16\\textwidth}p{0.14\\textwidth}p{0.18\\textwidth}r}",
        "\\textbf{Letter} & \\textbf{To} & \\textbf{From (place)} & \\textbf{Date} & \\textbf{Mood} & \\textbf{\\S\\S} \\\\",
        "\\hline",
    ]
    for letter in letters:
        wid = letter.get("id", "")
        title = tex_escape(works_by_id.get(wid, {}).get("title_english", wid))
        recip = tex_escape(letter.get("recipient", "") or "")
        place = tex_escape(letter.get("place_written", "") or "")
        date = tex_escape(letter.get("date", ""))
        mood = tex_escape(letter.get("mood", "") or "")
        n = letter.get("length_sections", 0)
        lines.append(f"{title} & {recip} & {place} & {date} & {mood} & {n} \\\\")
    lines.append("\\end{longtable}")
    lines.append("")
    return "\n".join(lines)


def emit_crossrefs(works_by_id: dict[str, dict[str, Any]]) -> str:
    crossref_dir = DATA / "crossrefs"
    if not crossref_dir.exists():
        return ""
    by_work: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for jp in sorted(crossref_dir.rglob("*.json")):
        blob = load_json(jp) or {}
        wid = blob.get("id", "?")
        for ref in blob.get("refs", []):
            by_work[wid].append(ref)
    if not by_work:
        return ""
    lines = [
        "\\chapter*{Cross-references}",
        "\\addcontentsline{toc}{chapter}{Cross-references}",
        "\\markboth{Cross-references}{Cross-references}",
        "",
        "\\noindent",
        "Where Cicero refers (explicitly or implicitly) to one of his own "
        "earlier works, or to an earlier passage within the same work.",
        "",
    ]
    for wid in sorted(by_work, key=lambda i: works_by_id.get(i, {}).get("date", "")):
        title = tex_escape(works_by_id.get(wid, {}).get("title_english", wid))
        lines.append(f"\\subsection*{{{title}}}")
        lines.append("\\begin{description}")
        for ref in by_work[wid]:
            from_loc_raw = str(ref.get("from_loc", ""))
            from_loc = tex_escape(from_loc_raw)
            tw_raw = ref.get("to_work", "")
            tw = tw_raw if tw_raw != "self" else wid
            to_loc_raw = str(ref.get("to_loc", ""))
            to_loc = tex_escape(to_loc_raw)
            tw_label = tex_escape(works_by_id.get(tw, {}).get("title_english", tw))
            kind = tex_escape(ref.get("kind", ""))
            note = tex_escape(ref.get("note", "") or "")
            from_anchor = section_hyperlink_target(
                wid, _section_anchor_loc(from_loc_raw)
            )
            to_anchor = section_hyperlink_target(
                tw, _section_anchor_loc(to_loc_raw)
            )
            lines.append(
                f"  \\item[\\hyperlink{{{from_anchor}}}{{\\S{from_loc}}}] "
                f"$\\to$ \\hyperlink{{{to_anchor}}}{{{tw_label} \\S{to_loc}}} "
                f"({kind}). {note}"
            )
        lines.append("\\end{description}")
        lines.append("")
    return "\n".join(lines)


def emit_allusions(works_by_id: dict[str, dict[str, Any]]) -> str:
    allusion_dir = DATA / "allusions"
    if not allusion_dir.exists():
        return ""
    by_work: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for jp in sorted(allusion_dir.rglob("*.json")):
        blob = load_json(jp) or {}
        wid = blob.get("id", "?")
        for a in blob.get("allusions", []):
            by_work[wid].append(a)
    if not by_work:
        return ""
    lines = [
        "\\chapter*{Allusions and quotations}",
        "\\addcontentsline{toc}{chapter}{Allusions and quotations}",
        "\\markboth{Allusions and quotations}{Allusions and quotations}",
        "",
        "\\noindent",
        "Suspected quotations of and allusions to other ancient authors. "
        "Certainty levels are flagged; some are explicit citations, others "
        "are thematic echoes.",
        "",
    ]
    for wid in sorted(by_work, key=lambda i: works_by_id.get(i, {}).get("date", "")):
        title = tex_escape(works_by_id.get(wid, {}).get("title_english", wid))
        lines.append(f"\\subsection*{{{title}}}")
        lines.append("\\begin{description}")
        for a in by_work[wid]:
            loc = tex_escape(a.get("loc", ""))
            src = tex_escape(a.get("suspected_source", ""))
            kind = tex_escape(a.get("kind", ""))
            cert = tex_escape(a.get("certainty", ""))
            tnote = tex_escape(a.get("translator_note", "") or "")
            lines.append(
                f"  \\item[\\S{loc}] {src} ({kind}, {cert}). {tnote}"
            )
        lines.append("\\end{description}")
        lines.append("")
    return "\n".join(lines)


def emit_translator_notes(works_by_id: dict[str, dict[str, Any]]) -> str:
    p = DATA / "translator-notes.jsonl"
    if not p.exists():
        return ""
    notes: list[dict[str, Any]] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            notes.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if not notes:
        return ""
    lines = [
        "\\chapter*{Translator's notes}",
        "\\addcontentsline{toc}{chapter}{Translator's notes}",
        "\\markboth{Translator's notes}{Translator's notes}",
        "",
        "\\noindent",
        "A selection of contested rendering choices, with the alternatives "
        "considered and the reasoning. Logged at the time of translation.",
        "",
    ]
    by_work: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for n in notes:
        by_work[n.get("work", "?")].append(n)
    for wid in sorted(by_work, key=lambda i: works_by_id.get(i, {}).get("date", "")):
        title = tex_escape(works_by_id.get(wid, {}).get("title_english", wid))
        lines.append(f"\\subsection*{{{title}}}")
        lines.append("\\begin{description}")
        for n in by_work[wid]:
            loc = tex_escape(n.get("loc", ""))
            lat = tex_escape(n.get("lat", ""))
            eng = tex_escape(n.get("eng", ""))
            note = tex_escape(n.get("note", "") or "")
            lines.append(
                f"  \\item[\\S{loc}] \\textit{{{lat}}} $\\to$ "
                f"\\textbf{{{eng}}}. {note}"
            )
        lines.append("\\end{description}")
        lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile", choices=PROFILES, default="reading",
        help="Build profile. reading=clean text only; study=+glossary, "
             "Greek catalogue, letter network; scholar=+crossrefs, "
             "allusions, translator's notes.",
    )
    args = parser.parse_args(argv)

    works, works_by_id = load_works()

    sections: list[str] = [
        f"% backmatter-generated.tex --- profile: {args.profile}",
        "% Generated by scripts/generate_backmatter.py from data/ sidecars.",
        "% Do not edit by hand.",
        "",
    ]

    if args.profile in ("study", "scholar"):
        sections.append(emit_glossary(works_by_id))
        sections.append(emit_greek_catalogue(works_by_id))
        sections.append(emit_letter_network(works_by_id))

    if args.profile == "scholar":
        sections.append(emit_crossrefs(works_by_id))
        sections.append(emit_allusions(works_by_id))
        sections.append(emit_translator_notes(works_by_id))

    body = "\n".join(s for s in sections if s)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(body + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT.relative_to(REPO)} (profile={args.profile}, "
        f"{len(body)} bytes)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
