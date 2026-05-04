// Entity registry loader. Reads ../data/entities.json (the corpus-wide
// registry) and exposes the entities grouped by type.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const entitiesPath = resolve(here, '../../../data/entities.json');

export type EntityType =
  | 'person' | 'place' | 'office' | 'institution'
  | 'law' | 'event' | 'festival' | 'unit' | 'god' | 'text';

export interface Entity {
  id: string;
  type: EntityType | string;
  canonical_name: string;
  short_name?: string;
  aliases?: string[];
  external_ids?: Record<string, string>;
  summary?: string;
  first_appearance?: string;
  categories?: string[];
}

interface EntitiesBlob {
  schema_version: number;
  entities: Entity[];
}

let cache: Entity[] | null = null;

export function loadEntities(): Entity[] {
  if (cache) return cache;
  const raw = readFileSync(entitiesPath, 'utf8');
  const parsed = JSON.parse(raw) as EntitiesBlob;
  cache = parsed.entities;
  return cache;
}

export function entitiesByType(entities: Entity[]): Map<string, Entity[]> {
  const grouped = new Map<string, Entity[]>();
  for (const e of entities) {
    const t = e.type || 'other';
    if (!grouped.has(t)) grouped.set(t, []);
    grouped.get(t)!.push(e);
  }
  // Sort each group by canonical_name
  for (const list of grouped.values()) {
    list.sort((a, b) =>
      (a.canonical_name ?? a.id).localeCompare(b.canonical_name ?? b.id),
    );
  }
  return grouped;
}

export function isStub(e: Entity): boolean {
  return (e.summary ?? '').includes('(stub');
}
