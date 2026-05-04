// Works data loader. Reads ../meta/works.yaml at build time and exposes
// the manifest plus a few summary helpers for the index page.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import yaml from 'js-yaml';

const here = dirname(fileURLToPath(import.meta.url));
const worksYamlPath = resolve(here, '../../../meta/works.yaml');

export type WorkStatus = 'pending' | 'drafted' | 'reviewed' | 'final';

export interface Work {
  id: string;
  title_latin: string;
  title_english: string;
  category: 'letters' | 'speeches' | 'philosophy' | 'rhetoric';
  date: string;
  date_precision?: string;
  date_range_end?: string;
  location_written?: string | null;
  latin_source_url?: string | null;
  latin_source_url_fallback?: string | null;
  latin_file?: string;
  english_file?: string;
  headnote_file?: string;
  status: WorkStatus;
  notes?: string;
  speech_index?: string;
}

let cache: Work[] | null = null;

export function loadWorks(): Work[] {
  if (cache) return cache;
  const raw = readFileSync(worksYamlPath, 'utf8');
  const parsed = yaml.load(raw) as Work[];
  if (!Array.isArray(parsed)) {
    throw new Error('meta/works.yaml did not parse to an array');
  }
  cache = parsed;
  return cache;
}

export interface WorksSummary {
  total: number;
  drafted: number;
  pending: number;
  draftedByCategory: Record<string, number>;
  totalByCategory: Record<string, number>;
}

export function summarize(works: Work[]): WorksSummary {
  const summary: WorksSummary = {
    total: works.length,
    drafted: 0,
    pending: 0,
    draftedByCategory: {},
    totalByCategory: {},
  };
  for (const w of works) {
    summary.totalByCategory[w.category] =
      (summary.totalByCategory[w.category] ?? 0) + 1;
    if (w.status === 'drafted' || w.status === 'reviewed' || w.status === 'final') {
      summary.drafted += 1;
      summary.draftedByCategory[w.category] =
        (summary.draftedByCategory[w.category] ?? 0) + 1;
    } else {
      summary.pending += 1;
    }
  }
  return summary;
}
