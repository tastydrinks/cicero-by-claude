# PLAN.md — cicero-by-claude master plan

This is the binding plan for the project. Read it after `STYLE.md`,
`BRIEF.md`, and `CLAUDE.md` and before doing any infrastructure work.
The translation discipline is unchanged from `CLAUDE.md`; this document
adds the broader vision — the project is producing a **multi-surface
edition** of Cicero, of which the bound book is one expression and the
web edition is another.

If you are an agent picking this project up cold, the chain of
required reading is:

1. `STYLE.md` — translation voice
2. `BRIEF.md` — what the project is
3. `PROGRESS.md` — what's drafted
4. `meta/works.yaml` — the manifest
5. `data/SCHEMA.md` — the structured-sidecar schemas
6. `build/PROFILES.md` — the bound-volume build profiles
7. **`PLAN.md` (this file)** — the multi-surface roadmap
8. `CLAUDE.md` — the operating brief that ties it all together

## The vision

A first-class English edition of the complete surviving works of
Cicero, in a single translator's voice (Claude), released in three
forms:

1. **The bound book** — a typeset volume on India paper, set in
   EB Garamond, finished by a specialty bookbinder. The single
   physical artifact for which the project is named. STYLE.md
   governs.
2. **The hyperlinked digital PDF** — the same translation, the same
   typesetting, with internal links activated. Entities click to
   their glossary entries. Cross-references resolve to their
   targets. Greek phrases reveal their gloss on tap. Identical to
   the bound print PDF when the links are stripped.
3. **The web edition** — the corpus rendered as an interactive
   reading and research surface. Side-by-side Latin/English. Hover
   prosopography. Letter-network graph. Timeline of Cicero's life
   with the works arrayed chronologically. Full-text search. The
   apparatus collapsible by reader preference.

Plus, as a deferred fourth surface:

4. **The AI companion** — a small companion endpoint backed by an
   LLM and the structured corpus, that can answer reader questions
   ("what's the political context of this letter?", "show me where
   Cicero says something similar elsewhere") with the actual sidecar
   data as ground truth.

## What makes this project unprecedented

Three things, in combination, none of which individually are
particularly novel:

- **One translator's voice across an entire major classical author**
  (Lattimore did this for the Iliad; Fagles did Homer; nobody has
  done it for the complete Cicero in modern English).
- **Structured apparatus generated as a side effect of producing the
  voice** — entity registry, sentence-aligned parallel corpus,
  Greek catalogue, letter network, allusions, cross-references
  (this kind of structured digital apparatus does not exist for any
  classical author at corpus scale).
- **Multiple complementary surfaces over the same corpus** — print
  and web editions sharing one source of truth, each playing to its
  medium's strengths, neither forced to be the other.

Loeb is multiple translators. Perseus has structured data but no
consistent voice. Delphi is a stitched compilation. The combination
sketched above does not currently exist for any major classical
author.

## The shared data layer

All four surfaces read from the same source:

```
data/
├── SCHEMA.md                       — canonical schema reference
├── greek-phrases.json              — corpus-wide Greek catalogue
├── letter-network.json             — corpus-wide letter graph
├── entities.json                   — corpus-wide entity registry
├── translator-notes.jsonl          — append-only rendering decisions
├── parallel/<category>/<id>.json   — sentence-aligned Lat/Eng
├── entities-mentions/<category>/<id>.json
├── glossary/<category>/<id>.json   — realia footnotes
├── allusions/<category>/<id>.json  — suspected allusions
└── crossrefs/<category>/<id>.json  — internal cross-references
```

This is the single source of truth. The translation files
(`latin/`, `english/`, `headnotes/`) carry the prose. Together
those two layers — prose + structured sidecars — are what every
surface consumes.

**Adding a new surface means: write a new build target that reads
those files. Nothing else.** The data layer is deliberately
upstream-of and independent-from the rendering layer.

## Tier 1 — The hyperlinked PDF

**Status**: not yet implemented.

**Goal**: turn the existing scholar-profile PDF into a navigable
digital document. Print remains identical (links don't print).

**Implementation sketch:**

- LaTeX changes only; no new infrastructure.
- `\hyperref` is already loaded. Extend `assemble_book.py` and the
  preamble's environments to:
  - Wrap entity surface forms in `\hyperlink{entity-<id>}{...}`
    when an entity_id is recorded for that locus in
    `data/entities-mentions/<cat>/<id>.json`.
  - Emit `\hypertarget{entity-<id>}{}` next to each entity's
    glossary entry in `backmatter-generated.tex`.
  - For cross-references in `data/crossrefs/`, emit
    `\hyperref[work-<id>-sec-<loc>]{...}` and corresponding
    `\hypertarget{work-<id>-sec-<loc>}{}` at each section opening.
  - Greek tooltips: use `pdfcomment` or similar to attach a
    tooltip annotation to each `\textgreek{...}` whose gloss is
    known in `data/greek-phrases.json`.

**Deliverable**: `build/output/cicero-v0.3-scholar.pdf` with internal
links live and visible in any PDF reader that supports them.

**Not part of Tier 1**: external links (Wikidata, Pleiades, etc.).
Those are web-edition territory. The print PDF stays self-contained.

## Tier 2 — The web edition

**Status**: not yet implemented. Lives in (the not-yet-created)
`web/` directory. See `web/README.md` once it exists.

**Goal**: the corpus as a first-class interactive reading surface.

**Architecture sketch:**

- **Static site generator**, building from the same `data/` and
  prose files at build time. Default candidate: Astro (modern,
  content-focused, supports MDX, ships zero JS by default).
  Alternatives considered but not chosen: Eleventy (simpler but
  less component-friendly), Next.js (overkill for static), hand-
  rolled HTML (initial appeal, scales badly).
- **Per-work pages**: `/works/<id>/` with sentence-aligned
  Latin/English in two columns. Reading mode toggles single-
  language. Headnote at top, collapsible.
- **Index pages**:
  - `/chronology/` — timeline of Cicero's life with the works
    arrayed along it; clickable.
  - `/letters/` — letter-network table and graph view.
  - `/glossary/` — entity registry, browsable by type.
  - `/greek/` — Greek-phrase catalogue.
  - `/concordance/` — cross-reference and allusion index.
- **Search**: prebuilt full-text index (Lunr or MiniSearch).
  Indexes both Latin and English; results show snippets.
- **Hover prosopography**: every entity-tagged surface form is a
  link; hovering pops a card with the entity's summary, type, and
  external links to Wikidata / DPRR / Pleiades.
- **Letter-network graph**: D3-force or visx, rendered from
  `data/letter-network.json`. Filterable by year, correspondent,
  mood. Click a letter to read it.
- **Apparatus toggle**: reader picks `reading` / `study` / `scholar`
  level the same way the PDF does; web stores the preference in
  localStorage.
- **Deployment**: static site to GitHub Pages (default, zero
  setup) or Cloudflare Pages (faster CDN, free).

**Build pipeline:**

```
python scripts/assemble_book.py --profile scholar    # PDF
npm --prefix web run build                            # web
```

Both read from the same `data/` directory. Translation batches
deepen both simultaneously.

**Phasing** (so each session can ship a visible thing):

- **Phase 2.1** — repo skeleton (`web/` directory, package.json,
  Astro project, deployment workflow). Site builds and shows a
  homepage.
- **Phase 2.2** — per-work pages. Read each work, render with
  parallel Latin/English. Navigation: previous/next chronological.
- **Phase 2.3** — chronology timeline.
- **Phase 2.4** — entity glossary index.
- **Phase 2.5** — hover prosopography (link every tagged mention
  to its glossary card).
- **Phase 2.6** — letter-network graph.
- **Phase 2.7** — full-text search.
- **Phase 2.8** — Greek catalogue, cross-reference / allusion
  indices, translator's-notes appendix.
- **Phase 2.9** — apparatus profile toggle in localStorage.
- **Phase 2.10** — visual polish, mobile responsiveness, RSS feed,
  whatever else the corpus deserves.

Each phase is one or two sessions. Translation batches continue
in parallel; the web edition deepens automatically as the corpus
deepens.

## Tier 3 — The AI companion

**Status**: deferred. Architecture documented now so Tier 2 doesn't
make decisions that block it.

**Goal**: the reader can ask natural-language questions of the
corpus and get answers backed by the structured data.

**Implementation sketch:**

- Cloudflare Worker (or any small endpoint) wrapping an Anthropic
  Claude API call.
- The full `data/` directory fits easily in a single context
  window (a few hundred KB at corpus completion).
- System prompt: "You are a research companion for cicero-by-claude.
  Use the structured sidecars as ground truth. When you cite a
  passage, link to the work-page on the web edition."
- Web edition embeds an "Ask" widget on each page that posts the
  current page's context plus the user's question to the worker.
- Cost-bounded by use; can be rate-limited per IP.

**What Tier 2 should do to keep Tier 3 cheap to add:**

- Keep `data/` directly URL-addressable from the web edition's
  origin (so the worker can fetch it at runtime, not bundle it).
- Use canonical work URLs (`/works/<id>/`) so citations from the
  AI link cleanly.
- Don't strip or transform the structured fields when rendering;
  the same JSON should be the AI's source of truth and the
  rendering layer's source of truth.

## What stays the same

The translation backbone — STYLE.md, the chronology rule, the
sidecar emit discipline, the parallel-session protocol — does not
change. Translation agents continue exactly as before. The
multi-surface plan is downstream of translation, not a substitute
for it.

`session_start.sh` and `session_end.sh` continue to work the same
way.

`scripts/finalize_parallel_batch.py` continues to be the post-
batch reconciliation command.

`scripts/validate.py` continues to be the gate.

## How to extend

When a future agent adds anything substantial to the project:

- New surface? Add a section to this PLAN.md describing it,
  pointing at its implementation directory.
- New sidecar artifact? Document its schema in `data/SCHEMA.md`,
  add it to `scripts/validate.py`, and update CLAUDE.md's "What
  'done' looks like" list.
- New build target? Add a section to `build/PROFILES.md` and
  document how it consumes the `data/` files.
- New top-level concept? Update this PLAN.md.

The single rule: **agents read the documentation first, then make
the change in a way the next agent will discover by reading the
same documentation.**

## Status tracking

Living progress on the multi-surface plan tracks here so it does
not get buried in `PROGRESS.md` (which is translation-focused).

| Item | Status |
|---|---|
| Translation backbone (single-voice corpus) | in progress (185 / ~795 works as of v0.2) |
| Sidecar infrastructure | shipped (`data/SCHEMA.md`, validators, backfill) |
| Bound-book build pipeline (`reading` profile) | shipped |
| Bound-book build pipeline (`study` profile) | shipped |
| Bound-book build pipeline (`scholar` profile) | shipped |
| Tier 1: hyperlinked PDF | not yet implemented |
| Tier 2: web edition (Phase 2.1: skeleton) | not yet implemented |
| Tier 2: web edition (Phase 2.2: per-work pages) | not yet implemented |
| Tier 2: web edition (later phases) | not yet implemented |
| Tier 3: AI companion | deferred |

Update this table as work lands.

## What Alexander needs to do

The translator and the infrastructure are Claude. The collaborator
(Alexander Woods) makes the directional and editorial calls.
Concretely:

- Approve `PLAN.md` (this file) when first written.
- Pick a deployment target for the web edition (default suggestion:
  GitHub Pages).
- Continue running translation agent batches; each batch deepens
  every surface automatically.
- Make UX/design judgment calls when surfaced one at a time.
- Eventually pick: a Greek font for the print PDF, a domain (or
  GitHub Pages URL) for the web edition, and the bookbinder.

The plan does not require Alexander to write code, run scripts, or
debug builds. Those are Claude's responsibilities.
