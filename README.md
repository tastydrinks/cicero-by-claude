# Cicero by Claude

A fresh, chronological English translation of the complete surviving works of
Marcus Tullius Cicero, rendered from the Latin in a single translator's voice
across the entire corpus.

The translator is Claude (Anthropic). The human collaborator is Alexander
Woods. The project is named in the tradition of attributed classical
translations — Lattimore's *Iliad*, Fagles' *Odyssey*.

## What this produces

The same translation feeds **multiple surfaces**:

1. **A typeset bound volume on India paper** — the named artifact, finished
   by a specialty bookbinder. Speeches, philosophical treatises, rhetorical
   works, and letters interleaved in strict chronological order, with
   letters given a distinct visual treatment.
2. **A hyperlinked digital PDF** — the same volume with internal links
   activated; entities tap to glossary entries, cross-references resolve,
   Greek phrases reveal their gloss. Built by `scripts/assemble_book.py
   --profile scholar` against the structured sidecars in `data/`.
3. **A web edition** — interactive reading and research surface (lives
   under `web/`, deploys to GitHub Pages). Side-by-side Latin/English on
   toggle, hover prosopography, letter-network graph, chronology timeline,
   full-text search, collapsible apparatus. See `web/README.md`.
4. **An agent-discoverable corpus** — the published web edition includes
   `llms.txt`, machine-readable JSON URL mirrors, and a downloadable
   archive so any third-party AI agent (Claude, GPT, etc.) brought by a
   reader can navigate and cite the corpus cleanly. The project itself
   does not host an AI companion endpoint.

All four surfaces read from the same source: the prose files in `latin/`,
`english/`, and `headnotes/`, plus the structured sidecars in `data/`.
The bound book is one expression and the digital surfaces are others —
no copy-pasting, no parallel maintenance.

## What this is not

Not a re-edition of an existing translation. Translations are produced
fresh from the Latin, not derived from any existing English version.
Not a one-shot work — this is a multi-year project at a sustainable pace
(see `PROGRESS.md`).

Not a hosted AI service. The project produces a corpus and the surfaces
above; AI consumption (by readers' own agents) is a use case the
structure supports, not a service the project provides.

## Repository layout

```
latin/             Source Latin texts, one file per work
english/           Fresh English translations, mirroring latin/
headnotes/         Short contextual note for each work (date, circumstance)
meta/              works.yaml — the chronological master index
data/              Structured sidecars (entities, parallel corpus,
                   Greek catalogue, letter network, etc.)
build/             LaTeX preamble, master document, build profiles
                   (reading/study/scholar), output PDFs
web/               Astro static site for the web edition (Tier 2)
scripts/           Python tooling (fetch, manifest, assembly,
                   validation, finalization, sidecar generators)
.github/           Workflows: web edition deploy + Claude Code action
                   for the PM-Claude orchestration
```

The single source of truth for the corpus and its ordering is
`meta/works.yaml`. Every work has an entry with date, category, paths,
and status. The book's chronological order is derived from sorting that
file by date.

## Required reading for any contributor (human or agent)

In order:

1. `STYLE.md` — translation voice (binding)
2. `BRIEF.md` — what this project is
3. `PROGRESS.md` — what's drafted and where to resume
4. `meta/works.yaml` — the manifest entry shape
5. `data/SCHEMA.md` — sidecar schemas
6. `build/PROFILES.md` — the bound-volume build profiles
7. `PLAN.md` — the multi-surface roadmap
8. `CLAUDE.md` — operating brief that ties it all together

## Building the bound volume

Requirements: Python 3.9+ with `pyyaml`, `requests`, `beautifulsoup4`. A
TeX distribution with `xelatex` (or `lualatex`) and `memoir`, `fontspec`,
`lettrine`, `polyglossia`, `longtable`. EB Garamond as the body font. A
Greek script font (DejaVu Sans is the placeholder; configurable in
`build/preamble.tex`).

```bash
# Validate the manifest and sidecars
python scripts/validate.py

# Regenerate MANIFEST.md, build/chronology.tex, body.tex, backmatter
python scripts/build_manifest.py
python scripts/assemble_book.py --profile scholar   # or reading / study

# Compile (run twice for cross-references)
cd build && xelatex -interaction=nonstopmode cicero.tex && xelatex cicero.tex
```

Output milestone PDFs are committed under `build/output/cicero-v*.pdf`.
The latest is `cicero-v0.3-scholar.pdf` (with internal hyperlinks).

## Building the web edition

```bash
cd web
npm install
npm run build       # generates web/dist/
npm run dev         # local preview at http://localhost:4321
```

Deploys automatically to GitHub Pages on pushes that touch `web/`,
`meta/`, `data/`, or the prose directories. See `.github/workflows/web-deploy.yml`.

## Running a translation session

The translation discipline is documented in `CLAUDE.md`. In brief:

```bash
bash scripts/session_start.sh     # fast-forward, validate, print next pending
# … translate the next pending work end-to-end, emitting all sidecars …
bash scripts/session_end.sh       # push session branch, fast-forward main
```

For parallel sessions, an explicit work-id list in the launch prompt
overrides the chronology rule. See `CLAUDE.md` § "Parallel sessions"
for the protocol.

After a parallel batch finishes, `scripts/finalize_parallel_batch.py`
auto-merges stuck branches, regenerates derived files, and validates.

## Translation philosophy

See `STYLE.md`. In short: render Cicero in clear, confident modern English
at a high register, faithful to the meaning above all. Preserve the shape
of his thought, the rhythm of his clauses, and the architecture of his
rhetorical figures. The poetry comes through his structure — not through
ornament added in English.

## Status

See `PROGRESS.md` for the current state and the chronology resume pointer.
See `PLAN.md` for the multi-surface roadmap and tier-by-tier status.

## License

The translations are released under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) —
share and adapt with attribution, non-commercial use only, derivatives
must use the same license. Personal-agent reading and research is
non-commercial use; commercial AI scraping is not. See `LICENSE`.

The Latin source texts are in the public domain. The Python tooling, web
edition code, and LaTeX configuration are under the same license as the
translations.
