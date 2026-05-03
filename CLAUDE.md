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
5. One finished letter headnote (e.g.
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
4. Status flipped to `drafted` in `meta/works.yaml` (anchoring
   discipline below).
5. `python scripts/validate.py` returns 0 warnings.
6. One commit per finished work; for long works, WIP commits at
   chunk boundaries plus a final commit when status is flipped.

## The chronology rule

Translations advance in **single-thread chronological order across
all four categories** — letters, speeches, philosophy, rhetoric —
by date in `meta/works.yaml`. The next pending work is whatever
`session_start.sh` prints first. The validator warns when any
pending work is dated earlier than the latest drafted work; trust
the warning, fix the dating or translate the work.

## Translation conventions

Beyond `STYLE.md`:

- **Letters** open with `\ciceroLetterOpener{LATIN SALUTATION}`
  (e.g. `CICERO ATTICO salutem`). The Perseus dateline is preserved
  as a `% Dateline (Perseus): …` comment at the top of the Latin
  file.
- **Greek phrases** (Cicero sprinkles them throughout the letters):
  render the meaning in English, then `\textit{[Greek:
  transliteration]}`.
- **Section numbers** use `\ciceroSection{N}` and preserve standard
  scholarly numbering (Teubner / OCT).
- The front-matter "Why this exists" note in `build/frontmatter.tex`
  (around line 73) is **Alexander's words and is not to be edited.**

## Timeout discipline

Stream idle timeouts are real and have caused mid-session failures.
The rules below are not optional.

- **For long speeches: 5 sections per `Edit`, with a WIP commit
  after each chunk.** Trying to write 30+ sections in one tool call
  loses the stream mid-response. 5-section chunks are the safe rate;
  a timeout then costs at most one chunk.
- **Payload size is the real limit, not section count.** If a single
  `Write`/`Edit`'s `new_string` is more than a few KB, split it.
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
- **Five no-Perseus works**: *Aratea* (86 BC), *De Consulatu Suo*
  (60), *De Temporibus Suis* (54), *Hortensius* (45), *Consolatio*
  (45). Latin must be supplied manually when the chronology reaches
  one of these. The validator excludes them from the
  chronological-gap check.
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
