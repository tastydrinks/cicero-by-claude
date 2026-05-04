// Headnote loader. Reads headnotes/<category>/<basename>.tex and returns
// the prose with LaTeX comments stripped and \textit{...} blocks unwrapped
// to plain text. Headnotes are 2--4 sentences for letters, fuller for
// major speeches; their LaTeX shape is one or more \textit{paragraphs}.
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import type { Work } from './works.ts';

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, '../../..');

export function loadHeadnote(work: Work): string | null {
  if (!work.headnote_file) return null;
  const path = resolve(repoRoot, work.headnote_file);
  if (!existsSync(path)) return null;
  let text = readFileSync(path, 'utf8');
  // Strip full-line comments
  text = text
    .split('\n')
    .filter((line) => !line.trimStart().startsWith('%'))
    .join('\n');
  // Unwrap \textit{...} (single-level, the convention from drafted
  // headnotes). For nested or complex cases we accept the inner text.
  text = text.replace(/\\textit\{([^}]*)\}/g, '$1');
  // Unwrap \emph and \textbf the same way
  text = text.replace(/\\(?:emph|textbf|textsc)\{([^}]*)\}/g, '$1');
  // Drop any remaining LaTeX commands with no argument
  text = text.replace(/\\[a-zA-Z]+(?:\[[^\]]*\])?/g, '');
  // Collapse whitespace
  text = text.trim().replace(/\n{3,}/g, '\n\n');
  return text || null;
}
