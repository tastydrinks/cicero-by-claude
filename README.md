# Cicero by Claude

A fresh, chronological English translation of the complete surviving works of
Marcus Tullius Cicero, rendered from the Latin.

The end product is a single typeset volume in which speeches, philosophical
treatises, rhetorical works, and letters are interleaved in strict
chronological order, with letters given a distinct visual treatment. The book
is designed for printing on India paper and finishing by a specialty
bookbinder.

The translator is Claude (Anthropic). The human collaborator is Alexander
Woods. The project is named in the tradition of attributed classical
translations — Lattimore's *Iliad*, Fagles' *Odyssey*.

This is a multi-year effort. Translations are added one work at a time, in
chronological order, with human review between works. Progress is tracked in
`PROGRESS.md`.

## Repository layout

```
latin/        Source Latin texts, one file per work
english/      Fresh English translations, mirroring latin/
headnotes/    Short contextual note for each work (date, circumstance, ~3 sentences)
meta/         works.yaml — the chronological master index
build/        LaTeX preamble, master document, generated body.tex, output PDFs
scripts/      Python tooling (fetch, manifest, assembly, validation)
```

The single source of truth for the corpus and its ordering is
`meta/works.yaml`. Every work has an entry with date, category, paths, and
status. The book's chronological order is derived from sorting that file by
date.

## Building the book

Requirements: Python 3.9+ with `pyyaml`, `requests`, `beautifulsoup4`. A TeX
distribution with `xelatex` (or `lualatex`) and the packages `memoir`,
`fontspec`, `lettrine`. EB Garamond as the body font.

```bash
# 1. Validate the manifest
python scripts/validate.py

# 2. Fetch Latin sources for any newly-added works
python scripts/fetch_latin.py <work-id>

# 3. Regenerate MANIFEST.md and build/chronology.tex
python scripts/build_manifest.py

# 4. Assemble the body in chronological order
python scripts/assemble_book.py

# 5. Compile the PDF (run twice for cross-references)
xelatex -output-directory=build -interaction=nonstopmode build/cicero.tex
xelatex -output-directory=build -interaction=nonstopmode build/cicero.tex

# Final PDF lands in build/output/
```

## Translation philosophy

See `STYLE.md`.

In short: render Cicero in clear, confident modern English at a high register,
faithful to the meaning above all. Preserve the shape of his thought, the
rhythm of his clauses, and the architecture of his rhetorical figures. The
poetry comes through his structure — not through ornament added in English.

## License

The translations are released under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — share
and adapt with attribution, non-commercial use only, derivatives must use the
same license. See `LICENSE`.

The Latin source texts are in the public domain. The Python tooling and LaTeX
configuration are under the same license as the translations.

## Status

See `PROGRESS.md`.
