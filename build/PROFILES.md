# Build profiles

The bound volume can be built in three reader-selectable profiles. The
translation source — Latin files, English files, headnotes — is identical
across profiles; what changes is the apparatus that surrounds the prose,
generated from the structured sidecars in `data/`.

## The three profiles

### `reading` (default)

The clean reading edition. STYLE.md governs: no inline footnotes,
context goes in the headnote, the prose carries no apparatus markers.

- Frontmatter: title, dedication, "Why this exists" note, chronology.
- Body: translations + headnotes, in chronological order.
- Backmatter: the hand-edited "A note on the text."

This is the volume Alexander reads. It is the artifact of the project.

### `study`

Same body as `reading`. Adds backmatter chapters that an interested
reader might want to consult without breaking the flow of the prose.

- Glossary of names (people, places, institutions, laws, etc.).
- Cicero's Greek — every Greek phrase in the corpus, with locus,
  meaning where recoverable, and source where suspected.
- Letter network — every letter as a row in a chronological table:
  recipient, place written, date, length, mood.

The body is unchanged from `reading`; the apparatus is opt-in by
flipping to the back of the book.

### `scholar`

Adds further apparatus on top of `study`:

- Cross-references — every place where Cicero refers explicitly or
  implicitly to one of his own earlier works or passages.
- Allusions and quotations — suspected references to Homer, Ennius,
  Plautus, the Twelve Tables, Plato, etc., with certainty levels.
- Translator's notes — selected non-obvious rendering choices, with
  the alternatives considered and the reasoning, logged at the time
  of translation.

Future polish (not yet implemented): inline marginal section markers
linked to the apparatus indices for quick lookup.

## How to build

```
python scripts/assemble_book.py --profile reading
python scripts/assemble_book.py --profile study
python scripts/assemble_book.py --profile scholar
```

Each invocation regenerates `build/body.tex` (identical across profiles)
and `build/backmatter-generated.tex` (varies by profile). Then compile:

```
cd build
xelatex cicero.tex   # twice for cross-references / TOC
```

The same source produces all three editions; only the backmatter
differs. There is no need to maintain three copies of anything.

## Where the apparatus comes from

| Backmatter chapter | Source sidecar |
|---|---|
| Glossary of names | `data/entities.json` + `data/glossary/<cat>/<id>.json` |
| Cicero's Greek | `data/greek-phrases.json` |
| Letter network | `data/letter-network.json` |
| Cross-references | `data/crossrefs/<cat>/<id>.json` |
| Allusions and quotations | `data/allusions/<cat>/<id>.json` |
| Translator's notes | `data/translator-notes.jsonl` |

See `data/SCHEMA.md` for the full schemas.

## Why this design

The single artifact of *cicero-by-claude* is the bound volume, set in
EB Garamond on India paper. STYLE.md asks for clean prose: no
footnotes, no bracketed translator's notes, no in-line apparatus.
That gives the reading edition.

But the project also produces a tagged corpus as a side effect of
translation. A reader who wants apparatus should be able to get it
without forcing it on the reader who wants prose. The profile system
splits these audiences cleanly: same prose, three editions, one
source of truth.
