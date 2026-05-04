# cicero-by-claude — Project Brief

## What this is

A repository for producing a fresh, chronological English translation of the
complete surviving works of Marcus Tullius Cicero, rendered from the Latin.
The translation is single-voice across the entire corpus.

The project produces **multiple surfaces** over the same translation:

1. **A typeset bound volume on India paper**, finished by a specialty
   bookbinder — the named artifact.
2. **A hyperlinked digital PDF** — the same volume with internal links
   activated; entities click to glossary entries, cross-references resolve,
   Greek phrases reveal their gloss.
3. **A web edition** — interactive reading and research surface, side-by-side
   Latin/English, hover prosopography, letter-network graph, timeline,
   full-text search, collapsible apparatus.
4. **An AI companion** (deferred) — the structured corpus exposed through
   an LLM that answers reader questions with the sidecar data as ground
   truth.

All surfaces read from the same source (`data/` plus the prose files); the
bound book is one expression and the digital surfaces are others. See
`PLAN.md` for the multi-surface roadmap.

The translator is Claude (Anthropic). The human collaborator is Alexander
Woods. The project is named in the tradition of attributed classical
translations (Lattimore's *Iliad*, Fagles' *Odyssey*).

## Repository structure

```
cicero-by-claude/
├── README.md
├── LICENSE                      # CC BY-NC-SA 4.0 for the translations
├── MANIFEST.md                  # The chronological master list
├── PROGRESS.md                  # Tracks what's translated, reviewed, typeset
├── STYLE.md                     # Translation style guide
│
├── latin/                       # Source Latin texts, one file per work
│   ├── speeches/
│   ├── philosophy/
│   ├── rhetoric/
│   └── letters/
│
├── english/                     # Fresh translations, mirroring latin/ structure
├── headnotes/                   # One short headnote per work
│
├── build/
│   ├── cicero.tex               # Master LaTeX file
│   ├── preamble.tex             # Document class, packages, custom commands
│   ├── chronology.tex           # Auto-generated TOC/timeline from MANIFEST.md
│   ├── frontmatter.tex          # Title, dedication, translator's preface
│   ├── backmatter.tex           # Index, glossary of names
│   └── output/                  # Generated PDFs
│
├── scripts/
│   ├── fetch_latin.py           # Pulls Latin texts from Perseus / Latin Library
│   ├── build_manifest.py        # Generates ordered manifest from metadata
│   ├── assemble_book.py         # Stitches translations into LaTeX in chronological order
│   └── validate.py              # Checks every Latin file has a translation, headnote, and date
│
└── meta/
    └── works.yaml               # Structured metadata for every work
```

## The metadata file: meta/works.yaml

The single source of truth for ordering and structure. Every work has an
entry; the chronological order of the book is determined by sorting
`works.yaml` by date. Where dates are imprecise, use a sensible default
(mid-month for month precision, July 1 for year precision) and flag in the
headnote.

## The translation workflow

For each work, in chronological order:

1. **Fetch the Latin.** `scripts/fetch_latin.py` pulls the source from a
   public-domain repository (Perseus, Latin Library, or LacusCurtius) and
   saves it to `latin/<category>/<id>.tex`. Light cleanup: remove HTML,
   normalize quotation marks, preserve section/chapter numbers as LaTeX
   commands.

2. **Translate.** Claude reads the Latin file and produces an English
   translation in `english/<category>/<id>.tex`, preserving the
   section/chapter structure. Translation follows `STYLE.md`. The translation
   is fresh — Claude works from the Latin, not from existing English versions.

3. **Write the headnote.** A 2–4 sentence contextual note in
   `headnotes/<category>/<id>.tex`: date, circumstance, why it matters, what
   Cicero is doing in his life at that moment.

4. **Update status.** Mark `status: drafted` in `works.yaml`. After human
   review, mark `reviewed` or `final`.

5. **Commit.** One commit per work.

## The build pipeline

`scripts/assemble_book.py` reads `works.yaml`, sorts chronologically, and
generates a master LaTeX file that `\input`s every translation in order. Each
entry is wrapped in a custom environment that handles its visual treatment:

- Speeches / treatises: full display, opening drop cap, work title in display
  size, headnote in italic below title.
- Letters: italic small-caps dateline, narrower measure, indented from outer
  margin, thin rules above and below.

Running heads carry the date so the book reads as a timeline.

## Typesetting

- Document class: `memoir`
- Body font: EB Garamond
- Page size: 6" × 9" trim, single volume on India paper
- Layout: single column, generous margins, ~32 lines per page
- Running heads: verso = work title, recto = date
- Page numbers: bottom center; small-caps roman in front matter, arabic in
  main text

## Translation principles

See `STYLE.md` for the full guide. The governing principle: render Cicero in
clear, confident modern English at a high register, faithful to the meaning
above all. Preserve the shape of his thought, the rhythm of his clauses, and
the architecture of his rhetorical figures. Let Cicero's poetry come through
his structure, not through ornament added in English.

## First-pass execution plan

1. Initialize the repo with the structure above.
2. Write `README.md`.
3. Write `MANIFEST.md` as a human-readable chronological table of contents,
   generated from `works.yaml`.
4. Populate `meta/works.yaml` with the full list of Cicero's surviving works,
   using Shackleton Bailey numbering for the letters.
5. Write `scripts/fetch_latin.py`. Source preference: Perseus first, Latin
   Library as fallback.
6. Write `scripts/validate.py` to check repo consistency.
7. Write `build/preamble.tex` and a minimal `build/cicero.tex` that compiles
   to a stub PDF.
8. Translate the first work as a test: *Pro Quinctio* (81 BC, Cicero's
   earliest surviving speech). Produce the Latin file, the translation, and
   the headnote. Run the build and confirm the PDF renders correctly.
9. Stop and report.

After approval of step 9, proceed in chronological order. Commit each work as
a separate commit. Update `PROGRESS.md` after every translation.

## What "done" looks like

- Every work in `meta/works.yaml` has `status: final`.
- `scripts/assemble_book.py` produces a clean PDF of the complete corpus as a
  single volume, formatted for India-paper printing and sewn binding.
- The PDF is print-ready for delivery to a specialty bookbinder.
- The `LICENSE` is CC BY-NC-SA 4.0 — Alexander Woods and Claude retain
  credit; non-commercial reuse permitted with attribution.

## Scope note

This is a multi-year project at a sustainable pace. The infrastructure
(scripts, metadata, build pipeline, first work translated) is the realistic
goal of the initial setup. Subsequent translations happen one work at a
time, in chronological order, with human review between works.
