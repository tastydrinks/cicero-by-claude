// /works/<id>.json — machine-readable mirror of the per-work page,
// for third-party agents (Claude, GPT, etc.) consuming the corpus
// without crawling HTML. Returns the parallel corpus alongside
// per-work sidecars (entity mentions, glossary, allusions, crossrefs)
// in a single JSON envelope.
import type { APIRoute } from 'astro';
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve, basename } from 'node:path';
import { loadWorks, type Work } from '../../lib/works.ts';
import { isDrafted } from '../../lib/chronology.ts';
import { loadParallel } from '../../lib/parallel.ts';
import { loadHeadnote } from '../../lib/headnote.ts';

const here = dirname(fileURLToPath(import.meta.url));
const dataRoot = resolve(here, '../../../../data');

function loadOptionalSidecar(work: Work, sub: string, key: string): unknown[] {
  if (!work.english_file) return [];
  const base = basename(work.english_file, '.tex');
  const path = resolve(dataRoot, sub, work.category, `${base}.json`);
  if (!existsSync(path)) return [];
  try {
    const blob = JSON.parse(readFileSync(path, 'utf8'));
    const list = blob[key];
    return Array.isArray(list) ? list : [];
  } catch {
    return [];
  }
}

export function getStaticPaths() {
  const works = loadWorks();
  return works.filter(isDrafted).map((w) => ({
    params: { id: w.id },
    props: { work: w },
  }));
}

interface Props {
  work: Work;
}

export const GET: APIRoute<Props> = ({ props }) => {
  const { work } = props;
  const parallel = loadParallel(work);
  const headnote = loadHeadnote(work);

  const envelope = {
    schema_version: 1,
    id: work.id,
    title_english: work.title_english,
    title_latin: work.title_latin,
    category: work.category,
    date: work.date,
    date_precision: work.date_precision,
    location_written: work.location_written,
    headnote,
    parallel: parallel ? {
      alignment_grain: parallel.alignment_grain,
      source_latin: parallel.source_latin,
      translator: parallel.translator,
      license: parallel.license,
      segments: parallel.segments,
    } : null,
    sidecars: {
      entities_mentions: loadOptionalSidecar(work, 'entities-mentions', 'mentions'),
      glossary: loadOptionalSidecar(work, 'glossary', 'notes'),
      allusions: loadOptionalSidecar(work, 'allusions', 'allusions'),
      crossrefs: loadOptionalSidecar(work, 'crossrefs', 'refs'),
    },
  };

  return new Response(JSON.stringify(envelope, null, 2), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
