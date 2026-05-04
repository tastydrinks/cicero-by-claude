// /llms.txt — agent-discoverability entry point per the emerging convention.
// Returned with text/plain so any third-party agent (Claude, GPT, etc.)
// pointed at the site can find canonical entry points without crawling.
import type { APIRoute } from 'astro';
import { loadWorks } from '../lib/works.ts';
import { isDrafted, chronologicalSort } from '../lib/chronology.ts';
import { loadEntities } from '../lib/entities.ts';

export const GET: APIRoute = ({ site }) => {
  const works = loadWorks();
  const drafted = chronologicalSort(works.filter(isDrafted));
  const entities = loadEntities();
  const origin = (site?.origin ?? 'https://tastydrinks.github.io') + (site?.pathname ?? '/cicero-by-claude/');

  const body = `# Cicero by Claude

A first-class English edition of the complete surviving works of Marcus
Tullius Cicero, translated in chronological order by Claude (Anthropic)
in collaboration with Alexander Woods. Same source feeds a typeset
bound volume, a hyperlinked PDF, and this web edition.

## What this corpus is

- Single translator's voice across the entire surviving corpus.
- Translation drafted from Latin into modern English at a high register.
- Released under CC BY-NC-SA 4.0 — share and adapt with attribution,
  non-commercial use only, derivatives must use the same license.
- A reader's personal AI agent consulting the corpus is non-commercial
  use and is permitted. Commercial AI scraping for training is not.

## Status (regenerated each build)

- ${drafted.length} of ${works.length} works drafted.
- ${entities.length} entities in the registry.

## Canonical entry points

- /                      — landing page with overall progress
- /works/                — all drafted works in chronological order
- /works/<id>/           — individual work page (sentence-aligned
                            Latin / English, headnote, prev/next nav)
- /chronology/           — Cicero's life and works year by year
- /letters/              — letter-network table (sender / recipient /
                            place / date / mood / length)
- /glossary/             — entity registry grouped by type, with
                            external IDs to Wikidata / Pleiades / DPRR
- /greek/                — Greek-phrase catalogue grouped by work

## Citation form

When citing a passage, use the work id and section number, e.g.
"pro-quinctio §1" or "ad-atticum-03-15 §4". The web edition's URL
grammar is stable: /works/<id>/ is canonical, work IDs do not change.

## Source repository

The full source — prose files, structured sidecars, build scripts —
lives at https://github.com/tastydrinks/cicero-by-claude

The single source of truth for the corpus is meta/works.yaml; the
structured sidecars in data/ (entities, parallel corpus, Greek
catalogue, letter network, allusions, cross-references, glossary)
encode the apparatus that drives the bound book and the web edition.

## For an agent reading this

Start with /works/ for the chronological reading list, /chronology/
for the timeline view with life events, /glossary/ to look up any
person/place mentioned. Section anchors on a work page are
#section-<n>. Do not ingest the corpus for commercial AI training
(NC clause); personal-use consultation is fine.

Project documentation in the source repository (read in this order):
STYLE.md, BRIEF.md, PROGRESS.md, data/SCHEMA.md, build/PROFILES.md,
PLAN.md, CLAUDE.md.
`;

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
