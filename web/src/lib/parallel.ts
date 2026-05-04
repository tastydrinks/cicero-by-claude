// Parallel-corpus loader. Reads ../data/parallel/<category>/<basename>.json
// where basename is derived from the work's english_file path (e.g.
// english/letters/058bc-ad-atticum-03-15.tex → 058bc-ad-atticum-03-15).
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve, basename } from 'node:path';
import type { Work } from './works.ts';

const here = dirname(fileURLToPath(import.meta.url));
const dataRoot = resolve(here, '../../../data');

export interface ParallelSegment {
  loc: string;
  section: number | null;
  lat: string;
  eng: string;
  notes?: string | null;
}

export interface ParallelCorpus {
  schema_version: number;
  id: string;
  category: string;
  title_latin: string;
  title_english: string;
  date: string;
  source_latin: string;
  translator: string;
  license: string;
  alignment_grain: 'sentence' | 'section';
  segments: ParallelSegment[];
}

export function parallelPathFor(work: Work): string | null {
  if (!work.english_file) return null;
  const base = basename(work.english_file, '.tex');
  return resolve(dataRoot, 'parallel', work.category, `${base}.json`);
}

export function loadParallel(work: Work): ParallelCorpus | null {
  const path = parallelPathFor(work);
  if (!path || !existsSync(path)) return null;
  try {
    const raw = readFileSync(path, 'utf8');
    return JSON.parse(raw) as ParallelCorpus;
  } catch {
    return null;
  }
}
