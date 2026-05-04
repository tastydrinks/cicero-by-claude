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

Plus, as a fourth, lower-cost surface:

4. **Agent-discoverable corpus** — the published corpus is structured so
   that any third-party AI agent (Claude, GPT, etc.) brought by a reader
   can navigate and cite it cleanly. This project does NOT host an AI
   companion endpoint or chat widget; it makes the data discoverable so
   readers can bring their own agent on their own budget. Implemented as
   `llms.txt`, sitemap, machine-readable JSON URLs mirroring every page,
   and a downloadable archive (folded into the Tier 2 phasing).

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

**Status**: shipped at v0.3 (`build/output/cicero-v0.3-scholar.pdf`).

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

**Implementation landed (v0.3):**

- `build/preamble.tex` keeps `hyperref[hidelinks]` (the printed page is
  identical to v0.2; on-screen the hand-cursor and bookmarks pane reveal
  clickability), and adds `pdfcomment` plus a `\ciceroGreekGloss` macro
  for Greek tooltips.
- `scripts/preprocess_english.py` reads each per-work English file at
  build time, walks it section by section, and writes a hyperlink-wrapped
  copy to `build/english/<category>/<id>.tex`. The source `english/`
  files are never modified.
  - Every `\ciceroSection{N}` opening becomes a `\hypertarget{work-<id>-sec-N}{}`.
  - Every entity mention with `in` ∈ {`eng`, `both`} wraps its first
    surface-form occurrence in `\hyperlink{entity-<entity-id>}{...}`.
  - Cross-references wrap the originating `\ciceroSection{N}` in
    `\hyperlink{work-<to_work>-sec-<to_loc>}{...}`.
- `scripts/generate_backmatter.py` emits `\hypertarget{entity-<id>}{}`
  next to each glossary entry's name and wraps the cross-reference
  index entries with `\hyperlink` so the apparatus chapters are
  navigable too.
- `scripts/assemble_book.py` invokes `preprocess_english.preprocess_work`
  inline and `\input{}`s the preprocessed copy.

**Counts in v0.3**: 788 entity destinations, ~4,260 section anchors,
~1,350 internal link annotations across the 1,834-page scholar PDF.

**Open follow-ups (v0.4+):**

- Greek tooltips are infrastructure-only at v0.3. The
  `\ciceroGreekGloss` macro and the data-driven wrapping in
  `preprocess_english.py` are in place, but `data/greek-phrases.json`
  carries no `english_gloss` values yet. Filling in the gloss column
  during a Greek-pass session will activate the tooltips automatically
  on the next build, with no further code changes.

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
- **Phase 2.11** — agent discoverability: `/llms.txt`,
  `/sitemap.xml`, machine-readable JSON URL mirrors of every page,
  the downloadable corpus archive, and license signalling. See
  Tier 3 below.
- **Phase 2.12** — EPUB export. Pandoc converts the LaTeX to EPUB;
  output committed to `build/output/cicero-v*.epub` alongside the
  PDF milestones. Mirrors the build profiles (`reading`, `study`,
  `scholar`).

## Confirmed design decisions (Alexander, this session)

These have been answered and are now binding (overridable later, but
the implementation phases proceed under these assumptions):

- **Visual style**: book-mirror. Web edition uses EB Garamond and
  classical proportions to reinforce that print and web are two
  surfaces of one project.
- **Default reading mode**: English-only, with a one-click toggle to
  reveal Latin (side-by-side or interlinear, implementor's choice).
- **Mobile**: desktop-first; mobile is "good enough" but not the
  primary design target. Tablet-readable a priority within "desktop-
  first."
- **Search scope**: bilingual (Latin + English), with a language
  filter in the UI. Phase 2.7 implementation needs a Latin
  tokenizer and diacritic normalization; budget extra time.
- **`llms.txt`**: yes, ship at site root in Phase 2.11.
- **Downloadable archive**: yes, ship as `/cicero-by-claude.zip` in
  Phase 2.11.
- **License**: CC BY-NC-SA 4.0 stays. The NC clause is the
  protection against commercial scraping; personal-agent use by a
  reader is non-commercial and permitted. `llms.txt` should state
  this explicitly so agents read the constraint upfront.
- **EPUB**: yes, future addition (Phase 2.12), not blocking.

Each phase is one or two sessions. Translation batches continue
in parallel; the web edition deepens automatically as the corpus
deepens.

## Tier 3 — Agent-discoverable corpus

**Status**: scoped. Folded into the Tier 2 phasing rather than built as
a separate hosted service.

**Reframe (per Alexander)**: this project does NOT host an AI companion
endpoint. The reader who wants AI assistance brings their own agent
(Claude Code, ChatGPT, a third-party tool — their choice, on their
budget). Tier 3 is therefore the discipline of making the corpus
maximally discoverable and usable by *someone else's* agent.

**Goal**: when an external agent is pointed at the published web
edition, it should be able to:

- Discover the corpus structure from a small set of canonical entry
  points without crawling everything blindly.
- Fetch the full structured data (entities, mentions, parallel corpus,
  letter network, Greek catalogue) from stable machine-readable URLs.
- Cite passages with stable permalinks the user can verify in a
  browser.
- Optionally consume the entire corpus offline as a single archive.

**Implementation (folded into Tier 2 phases):**

- **`/llms.txt`** at the site root — a small markdown file pointing
  agents at the canonical entry points (chronology, glossary, parallel
  corpus, letter network) and stating the project's purpose, license,
  and citation form. The emerging convention for agent-discoverability.
- **`/sitemap.xml`** auto-generated from the work IDs — every work
  page, every glossary entry, every index page enumerated.
- **Machine-readable JSON URLs** mirroring every page:
  `/works/<id>.json` returns the parallel corpus + sidecars for that
  work; `/glossary/<entity-id>.json` returns the entity record plus
  its mention back-links; etc. The web edition serves these as static
  files generated alongside the HTML.
- **Downloadable archive**: `/cicero-by-claude.zip` containing the
  full `data/` directory, prose files, and a README pointing at the
  web edition. Regenerated on each web build.
- **Stable URL grammar**: work IDs become permanent slugs; section
  anchors are `#section-<n>`; any restructuring requires HTTP
  redirects from the old URL.
- **License signalling**: `/llms.txt` and the archive's README state
  the license clearly. (Currently CC BY-NC-SA 4.0; the NC clause
  may need revisiting for commercial AI use, but that's an
  Alexander-decides question deferred until needed.)

**What this means for Tier 2's phasing:**

- Phase 2.1 (skeleton) bakes in the URL grammar; once published,
  changing it later is expensive.
- Phase 2.2 (per-work pages) emits `/works/<id>.json` alongside the
  HTML page from the same data loader.
- A new **Phase 2.11 — agent discoverability** lands `llms.txt`,
  `sitemap.xml`, the archive build step, and the license signalling.

**What this is NOT:**

- Not a hosted AI endpoint, not an "Ask" widget, not a chat UI, not
  an Anthropic API key in this project's deployment. None of those.
  Readers who want AI bring their own.

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
| Tier 1: hyperlinked PDF | shipped (v0.3 scholar; Greek tooltips pending gloss data) |
| Tier 2: web edition (Phase 2.1: skeleton) | shipped (Astro + GitHub Pages workflow; landing page reads `meta/works.yaml`) |
| Tier 2: web edition (Phase 2.2: per-work pages) | not yet implemented |
| Tier 2: web edition (later phases) | not yet implemented |
| Tier 3: agent-discoverable corpus (Phase 2.11) | not yet implemented; folded into Tier 2 |

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
