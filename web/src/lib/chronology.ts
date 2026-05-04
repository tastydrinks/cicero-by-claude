// Chronology helpers: parse the project's date strings (-YYYY-MM-DD or
// YYYY-MM-DD), produce sortable tuples and human-readable labels, and
// give prev/next siblings for any work.
import type { Work } from './works.ts';

export type DateTuple = [number, number, number];

export function parseDate(s: string): DateTuple {
  if (s.startsWith('-')) {
    const [ys, rest] = s.slice(1).split('-', 2);
    const after = s.slice(1 + ys.length + 1);
    const [m, d] = after.split('-');
    return [-parseInt(ys, 10), parseInt(m, 10), parseInt(d, 10)];
  }
  const [ys, m, d] = s.split('-');
  return [parseInt(ys, 10), parseInt(m, 10), parseInt(d, 10)];
}

export function compareDates(a: DateTuple, b: DateTuple): number {
  for (let i = 0; i < 3; i++) {
    if (a[i] !== b[i]) return a[i] - b[i];
  }
  return 0;
}

export function chronologicalSort(works: Work[]): Work[] {
  const decorated = works.map((w) => ({ w, key: parseDate(w.date) }));
  decorated.sort((a, b) => compareDates(a.key, b.key) || a.w.id.localeCompare(b.w.id));
  return decorated.map((d) => d.w);
}

export function isDrafted(w: Work): boolean {
  return w.status === 'drafted' || w.status === 'reviewed' || w.status === 'final';
}

const MONTHS = [
  '', 'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December',
];

export function shortDate(s: string, precision?: string): string {
  const [y, m, d] = parseDate(s);
  const era = y < 0 ? 'BC' : 'AD';
  const yearStr = `${Math.abs(y)} ${era}`;
  if (precision === 'year' || precision === 'year_range') return yearStr;
  if (precision === 'month') return `${MONTHS[m]} ${yearStr}`;
  return `${d} ${MONTHS[m]} ${yearStr}`;
}

export interface NeighbourLinks {
  prev: Work | null;
  next: Work | null;
}

export function neighboursDrafted(works: Work[], work: Work): NeighbourLinks {
  const drafted = chronologicalSort(works.filter(isDrafted));
  const idx = drafted.findIndex((w) => w.id === work.id);
  if (idx === -1) return { prev: null, next: null };
  return {
    prev: idx > 0 ? drafted[idx - 1] : null,
    next: idx < drafted.length - 1 ? drafted[idx + 1] : null,
  };
}
