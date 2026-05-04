# CLAUDE.md — operating brief for cicero-by-claude

This file is auto-loaded into every Claude Code session for this
repo. It is the operating brief for the project. Read it first;
everything else follows from it.

You are translating the surviving works of Cicero into English, in
chronological order, for a single typeset bound volume on India
paper. The human collaborator is **Alexander Woods** (never
abbreviated). The translator is Claude.

## Required reading at session start

Read these in order before writing a word of translation:

1. `STYLE.md` — translation style guide. **Binding. Re-read every
   session**, even on continuations. Cicero's voice is the project,
   and the style guide is how it stays one voice across hundreds of
   works and many sessions.
2. `BRIEF.md` — what this project is, repo structure, build
   pipeline. Skim if returning.
3. `PROGRESS.md` — what's drafted, what's pending. The
   **"Where to resume now"** section is the chronology pointer for
   continuing sessions. Update it as you go; this is the place that
   stays current, not `CLAUDE.md`.
4. `meta/works.yaml` — the manifest. Skim the entry shape; you will
   be flipping `status:` fields and occasionally correcting dates.
5. `data/SCHEMA.md` — the structured-sidecar schemas. Every
   translated work emits sidecars (parallel corpus, Greek phrases,
   entity mentions, allusions, glossary notes, and so on). Skim
   the schemas; the per-work emit discipline is summarised in
   "What 'done' looks like" below.
6. `build/PROFILES.md` — the reading / study / scholar build
   profile system. The bound volume is built in three editions
   from the same source; the apparatus is generated from the
   sidecars.
7. One finished letter headnote (e.g.
   `headnotes/letters/058bc-ad-atticum-03-07.tex`) for the
   established convention.

After that, run `bash scripts/session_start.sh`. It fast-forwards
the session branch to `origin/main`, runs the validator, and prints
the chronologically next pending work.

## The session loop

```
bash scripts/session_start.sh         # always first
… do the work …
bash scripts/session_end.sh           # always last
```

`session_end.sh` pushes the session branch and fast-forwards
`origin/main` to the same tip. Use both. The harness assigns a
fresh branch name per session, but `origin/main` is the source of
truth.

## What "done" looks like for a single work

1. Latin file fetched into `latin/<category>/` (`scripts/fetch_latin.py
   <id>`). **Commit the Latin before translating**, so a stream
   timeout costs no Latin work.
2. English file translated end-to-end **from the Latin** into
   `english/<category>/`. Translations are fresh, never derived from
   existing English versions.
3. Headnote written in `headnotes/<category>/`. 2–4 sentences for
   short letters, fuller for major speeches.
4. **Sidecars emitted to `data/`** (see `data/SCHEMA.md`). For each
   translated work:
   - `data/parallel/<category>/<id>.json` — section-aligned Latin
     and English text. Mostly mechanical; the structural backfill
     script will produce this if forgotten, but emitting it during
     translation is preferred.
   - `data/entities-mentions/<category>/<id>.json` — every named
     person, place, office, institution, law, festival, god, or
     external text mentioned, tagged with stable entity IDs. **Every
     entity_id you reference in a mention or glossary note must also
     exist in `data/entities.json`.** If you introduce a new id, add
     a registry entry in the same commit (id, type, canonical_name,
     short summary, first_appearance). The validator warns on unknown
     ids, and the finalizer auto-stubs them at batch end --- but a
     stub is a placeholder, not real apparatus, and creates work for
     a later enrichment pass. Better to write the real entry the
     first time.
   - `data/glossary/<category>/<id>.json` — short realia notes for
     things a non-classicist would miss (the kalends, the
     pontifices, particular families). One per anchor per work.
   - `data/allusions/<category>/<id>.json` — suspected quotations
     of and allusions to other ancient authors (Homer, Ennius,
     Plautus, the Twelve Tables). Flag-not-resolve.
   - `data/crossrefs/<category>/<id>.json` — internal references
     to Cicero's own earlier works or earlier sections.
   - For letters: append a row to `data/letter-network.json`
     (sender, recipient, place, date, mood, length).
   - For Greek phrases: append entries to `data/greek-phrases.json`.
   - For genuinely contested rendering choices: append a line to
     `data/translator-notes.jsonl`.

   These sidecars are the apparatus that drives the study and
   scholar build profiles. Skipping them means skipping the
   apparatus for that work.
5. Status flipped to `drafted` in `meta/works.yaml` (anchoring
   discipline below).
6. `python scripts/validate.py` returns 0 warnings (or only the
   pre-existing chronological-gap warning for pending work).
7. One commit per finished work; for long works, WIP commits at
   chunk boundaries plus a final commit when status is flipped.

After a batch of finished works (every several commits, or at the
end of a session), run `python scripts/build_manifest.py` to
regenerate `MANIFEST.md` and `build/chronology.tex` from the
updated `meta/works.yaml`. `session_end.sh` is a fine moment for
this.

## Build profiles

The bound volume is built in three reader-selectable editions from
the same source: `reading` (default, clean prose), `study` (adds
glossary, Greek catalogue, letter-network appendix), and `scholar`
(further adds cross-references, allusions, translator's notes).
See `build/PROFILES.md`. To build:

```
python scripts/assemble_book.py --profile reading
python scripts/assemble_book.py --profile study
python scripts/assemble_book.py --profile scholar
```

`assemble_book.py` regenerates `body.tex` (identical across
profiles) and delegates backmatter regeneration to
`scripts/generate_backmatter.py`. STYLE.md governs the body in
all profiles; only the backmatter varies.

## Sidecar emit discipline (in long sessions)

For long speeches, emit sidecars in lockstep with translation
chunks: when you finish a 5-section chunk and commit it, append the
matching entries to the per-work sidecar files in the same commit.
Don't batch all sidecars to the end — a stream timeout late in the
work would lose them, and they're easier to write while the section
is still in working memory.

For short letters, emit sidecars together with the English file
and headnote in one final commit.

If a sidecar is hard to emit at the moment (e.g., you're not sure
about an allusion's source), leave it for the post-session
backfill rather than guessing. Flag-not-resolve is the rule.

## The chronology rule

Translations advance in **single-thread chronological order across
all four categories** — letters, speeches, philosophy, rhetoric —
by date in `meta/works.yaml`. The next pending work is whatever
`session_start.sh` prints first. The validator warns when any
pending work is dated earlier than the latest drafted work; trust
the warning, fix the dating or translate the work.

## Parallel sessions: explicit assignments override chronology

The chronology rule is the **single-agent default**. When several
sessions run in parallel, an explicit work-id list in the launch
prompt **overrides** the chronology rule for that session. The
agent translates the assigned works in the order given, and ignores
the chronologically-next-pending output of `session_start.sh`.

Example launch prompt:

```
Translate these works in order: in-vatinium, ad-familiares-01-06,
pro-caelio (skip if drafted), ad-quintum-fratrem-02-05.
```

Rules:

- If the launch prompt names specific work IDs, those are the
  session's scope. Do not pick up other works "because the chronology
  pointer suggests them."
- Skip any assigned id whose `status` in `meta/works.yaml` is already
  drafted, reviewed, or final. (Another agent may have finished it
  before this session started, or in parallel.)
- If no work IDs are named in the launch prompt, fall back to the
  chronology rule and translate the chronologically-next pending
  work, as in single-agent mode.
- Update `PROGRESS.md` only for works this session actually drafted.
  When merging conflicts on `PROGRESS.md`, prefer additive merges
  (keep both sessions' entries); the file is documentary, not
  authoritative.

The corpus-wide sidecar files (`data/greek-phrases.json`,
`data/letter-network.json`, `data/entities.json`,
`data/translator-notes.jsonl`) are append-targets that may see
concurrent writes. If git refuses a fast-forward push at session end
because main has moved, rebase the session branch onto the new main
and re-run `session_end.sh`. The work is on the session branch
either way; nothing is lost.

## Translation conventions

Beyond `STYLE.md`:

- **Letters** open with `\ciceroLetterOpener{LATIN SALUTATION}`
  (e.g. `CICERO ATTICO salutem`). The Perseus dateline is preserved
  as a `% Dateline (Perseus): …` comment at the top of the Latin
  file.
- **Greek phrases** (Cicero sprinkles them throughout the letters):
  render the meaning in English, then `\textit{[Greek:
  transliteration]}`. Greek script in the Latin (e.g.
  `μυστικώτερα`) can be passed through inside `\textgreek{…}` when
  preserving it as marginalia is wanted.
- **Section numbers** use `\ciceroSection{N}` and preserve standard
  scholarly numbering (Teubner / OCT).
- The front-matter "Why this exists" note in `build/frontmatter.tex`
  (around line 73) is **Alexander's words and is not to be edited.**

## File-header conventions

Every translation and headnote opens with a short comment block.
Match this exactly so files are self-identifying.

**English translation file** (`english/<category>/<id>.tex`):
```
% Pro Quinctio (pro-quinctio) --- English translation
% Translated by Claude (Anthropic) from the Latin (Perseus).
% Style guide: STYLE.md.
```

**Headnote file** (`headnotes/<category>/<id>.tex`):
```
% Pro Quinctio --- headnote
% pro-quinctio, 81 BC, Rome
```

The headnote body itself is wrapped in `\textit{…}` blocks (one per
paragraph), per the convention you can see in any drafted headnote
under `headnotes/`.

**Latin file headers** are written by `scripts/fetch_latin.py` and
should not be edited by hand.

## Timeout discipline

Stream idle timeouts are real and have caused mid-session failures.
**This section supersedes any older guidance** (e.g. the "30–50
sections per batch" line in earlier `PROGRESS.md` revisions). The
rules below are not optional.

- **For long speeches: ~5 sections per `Edit`, with a WIP commit
  after each chunk.** Trying to write 20+ sections in one tool call
  loses the stream mid-response. 5-section chunks are the safe rate;
  a timeout then costs at most one chunk.
- **Payload size is the real limit, not section count.** If a single
  `Write`/`Edit`'s `new_string` is more than a few KB of new
  content, split it. Some Cicero sections are short (one or two
  sentences); some run to a paragraph or two. Adjust accordingly.
- For short letters (1–7 short sections), one `Write` per English
  file is fine. This discipline only matters for substantial works.
- **Don't use `cat` / `echo` heredocs in `Bash` to assemble large
  strings.** Use `Write`/`Edit` with smaller payloads.
- Keep tool-result outputs small. Read a range of a file (`offset` /
  `limit`) rather than the whole file when you only need part.
- The `TodoWrite` system-reminder fires constantly. Ignore it unless
  the list is genuinely stale; do not let it interrupt the rhythm.

## Status-flip discipline in works.yaml

`status: pending` is **not unique** in `works.yaml`. To flip to
`drafted`, anchor your `Edit` on the entry's unique three-line
`latin_file:`/`english_file:`/`headnote_file:` block:

```
  latin_file: latin/letters/058bc-ad-atticum-03-08.tex
  english_file: english/letters/058bc-ad-atticum-03-08.tex
  headnote_file: headnotes/letters/058bc-ad-atticum-03-08.tex
  status: drafted          ← was: pending
```

## Metadata gotchas (real, frequent)

- **Placeholder dates.** Many letters carry year-precision
  placeholder dates that conflict with the Perseus dateline. Always
  check the `% Dateline (Perseus): …` comment in the Latin file. If
  the entry's date is plainly wrong (e.g. `-0048-11-26` for a letter
  whose dateline is `vi K. Dec. a. 696 (58)`), correct the entry
  date and rename the file (`058bc-…tex` not `048bc-…tex`).
- **Missing `speech_index`.** If `fetch_latin.py` writes hundreds of
  thousands of characters (the whole book file, not one piece), the
  entry is missing `speech_index: book:N,letter:M`. Add it,
  re-fetch.
- **Latin Library is 403'd.** Perseus is the only working source
  for most works. The `latin_source_url_fallback` to
  thelatinlibrary.com generally won't work. If the Perseus URL is
  missing or wrong, fix the entry; don't rely on the fallback.
- **Five no-Perseus fragmentary works**: *Aratea* (86 BC),
  *De Consulatu Suo* (60), *De Temporibus Suis* (54), *Hortensius*
  (45), *Consolatio* (45). When the chronology reaches one of
  these, the Latin must be supplied manually (the surviving
  fragments are gathered in standard Teubner / Loeb editions).
  Don't try to fetch them via `fetch_latin.py`; the entries carry
  no Perseus URL. The validator excludes these from the
  chronological-gap check.
- **One no-Perseus complete work**: *De Legibus* (52 BC) survives
  in full but is not in Perseus's TEI corpus. When the chronology
  reaches it, the Latin must be sourced manually
  (`thelatinlibrary.com/cicero/leg.shtml` was the previous source,
  but it currently 403s; another classical-Latin repository may
  need to supply it).
- **Two deferred works**: *Aratea* (86 BC) and *De Inventione*
  (85 BC) precede *Pro Quinctio* in date but are deliberately
  skipped. Do not circle back to them mid-stream.

## Fetch script

```
python scripts/fetch_latin.py <id1> <id2> …
```

Needs `pyyaml requests beautifulsoup4 lxml`. If you get a `bs4` or
xml-parser error, run:

```
pip install pyyaml requests beautifulsoup4 lxml
```

and re-run the fetch.

## Commit and push hygiene

- One commit per finished work. For long speeches, WIP commits at
  5-section chunk boundaries with descriptive messages, and a final
  commit when the headnote is in place and `status:` is `drafted`.
- Commit message format: a one-line summary identifying the work,
  the date and place written, and the substantive content; one
  blank line; a paragraph of context; one blank line; the
  `https://claude.ai/code/session_…` URL if available.
- `session_end.sh` handles pushing. Don't push to `main` directly;
  the script does the fast-forward.
- The harness's git server refuses branch deletions, so old session
  branches accumulate on `origin`. They are harmless (strict
  ancestors of `main`); Alexander prunes them via the GitHub web UI.

## Standards

Quality over throughput. The reader of the bound volume will not
know how many works you finished in any session; they will know
whether the sentences land. Render Cicero's poetry through his
structure, not through ornament added in English. See `STYLE.md`.

Translate forward chronologically without pausing for per-work
approval. Commit and push per finished work. Update `PROGRESS.md`'s
"Where to resume now" section as the resume pointer moves; that is
the file other sessions read first to know where to pick up.
