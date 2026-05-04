# web/ — the cicero-by-claude web edition

This directory will hold the Tier 2 web edition (see `../PLAN.md` for
the multi-surface roadmap). It is **not yet implemented** — this README
is the placeholder that documents what will live here.

## What this is

A static-site-generated reading and research surface for the complete
Cicero corpus, built from the same `data/` and prose files that feed
the bound book and the print PDF. Same source of truth, different
medium.

## Architecture (as of PLAN.md v1)

- **Generator**: Astro (chosen for content focus, MDX support, zero-JS
  defaults). Alternatives considered: Eleventy, Next.js, hand-rolled
  HTML. Astro picked for the right balance of features and
  build-output size.
- **Source data**:
  - `../data/parallel/<cat>/<id>.json` — sentence-aligned Lat/Eng
  - `../data/entities.json` — entity registry (used for hover popups
    and the glossary index)
  - `../data/entities-mentions/<cat>/<id>.json` — per-work mention tags
    (used to wrap surface forms in the rendered work pages)
  - `../data/glossary/<cat>/<id>.json` — realia notes
  - `../data/allusions/<cat>/<id>.json` — flagged allusions
  - `../data/crossrefs/<cat>/<id>.json` — internal cross-references
  - `../data/greek-phrases.json` — Greek catalogue
  - `../data/letter-network.json` — letter graph
  - `../data/translator-notes.jsonl` — rendering decisions
  - `../meta/works.yaml` — manifest, chronology, dates
  - `../headnotes/<cat>/<id>.tex` — per-work introductions (parsed for
    web rendering)
  - `../english/<cat>/<id>.tex` and `../latin/<cat>/<id>.tex` — the
    prose

## Page model

```
/                           — landing page; "About" + chronology summary
/works/<id>/                — per-work page, parallel Lat/Eng
/works/<id>/?lang=eng       — single-language English mode
/works/<id>/?lang=lat       — single-language Latin mode
/chronology/                — interactive timeline of Cicero's life
/letters/                   — letter-network graph + table
/letters/<correspondent>/   — filtered network for one correspondent
/glossary/                  — entity registry, browsable by type
/glossary/<entity-id>       — entity detail page (mentions back-linked)
/greek/                     — Greek-phrase catalogue, searchable
/concordance/               — cross-reference / allusion index
/notes/                     — translator's-notes appendix
/search/                    — full-text search (Lunr / MiniSearch)
```

## URL stability

Once the web edition ships, work IDs become canonical URL slugs and
must not change. If a work is renamed in `meta/works.yaml`, a redirect
should be emitted. This matters because external links (e.g. from the
Tier 3 AI companion or external citations) will use these URLs.

## Apparatus profiles

The web edition mirrors the print build's `reading` / `study` /
`scholar` profile system. Reader picks; preference stored in
`localStorage`. Reading mode hides backmatter-equivalent surfaces;
study and scholar progressively reveal more.

## Search index

A prebuilt search index (Lunr or MiniSearch) covers Latin and English.
Built at site-generate time, shipped as a static JSON file, queried
client-side. No backend required.

## Deployment

Static site, deployable to any static host. Default plan: GitHub
Pages, automatic on push to `main`. Cloudflare Pages is the alternate
if better CDN behaviour is wanted.

A GitHub Actions workflow at `.github/workflows/web-deploy.yml` will
trigger the build on push and publish the result. (Not yet created;
will be added in Phase 2.1.)

## Phasing

See `../PLAN.md` for the ten-phase build sequence (skeleton →
per-work pages → timeline → glossary → hover popups → letter network
→ search → catalogue indices → profile toggle → polish).

## Tier 3 readiness

The web edition's URL structure must be stable enough that the AI
companion can cite into it. The data files must remain URL-addressable
from the web edition's origin (or the worker can fetch them
separately) so the companion's runtime can read structured ground
truth without bundling.

Don't transform structured fields away when rendering; the same JSON
should be the AI's source of truth and the rendering layer's input.

## What this directory will contain

```
web/
├── README.md                — this file
├── package.json             — Astro / build dependencies
├── astro.config.mjs         — generator config
├── src/
│   ├── pages/               — route handlers (one per page in the URL map above)
│   ├── components/          — UI components (entity popup, network graph, etc.)
│   ├── layouts/             — page layouts (work, index, about)
│   └── lib/                 — data loaders that read from ../data/ and ../meta/
├── public/                  — static assets, fonts
└── dist/                    — generated output (gitignored)
```

(None of these exist yet; this is the target state.)
