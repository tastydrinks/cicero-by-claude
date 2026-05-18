# OPERATING_PLAN.md — getting cicero-by-claude done

This is the binding operating plan for Claude Cowork (the project's PM agent)
when running translation sessions against this repo. Read it after `STYLE.md`,
`BRIEF.md`, `CLAUDE.md`, and `PROGRESS.md`'s "Where to resume now" section.

The plan is concrete: it tells the PM what to do each session, what order to
do the corpus in, and how to leave a clean handoff so the human collaborator
(Alexander) can land the work with one shell command.

## Scope of completion

"Project complete" means:

1. All translatable surviving works of Cicero (952 entries; 958 - 6 deferred
   fragments) translated end-to-end with headnotes and parallel sidecars.
2. Apparatus sidecars (entities-mentions, glossary, allusions, crossrefs)
   present on every drafted work.
3. The `data/entities.json` registry filled out (no placeholder stubs).
4. The four surfaces shipped: bound book (PDF + bookbinder handoff), Tier 2
   web edition, hyperlinked digital PDF, agent-discoverable corpus.

Of these, items 1-3 are agent work. Item 4 mostly already shipped (Tier 1
PDF, Tier 4 corpus done; Tier 2 has phases 2.1-2.4, 2.6, 2.7, 2.8a, 2.11
shipped; remaining Tier 2 phases are agent work). The actual bookbinder
handoff is Alexander's, not an agent's.

## Total session estimate

| Phase | Sessions | What |
|---|---|---|
| 0. Foundation | 1 (this one) | Fix fetch script, write handoff helper, save this plan, update CLAUDE.md |
| 1. Bulk letters | ~18 | ~520 short letters batched 30/session |
| 2. Substantial letters + minor speeches | ~15 | 3–5/session for substantial; 1/session for minor speeches |
| 3. Major works | ~30 | 1 substantial work per session (De Oratore, Tusculans, De Officiis, Philippics, etc.) |
| 4. Apparatus enrichment | ~8 | Entity stub enrichment, judgment-sidecar backfill |
| 5. Tier 2 web finish | ~4 | Phases 2.5, 2.9, 2.10, 2.12 |
| 6. Final assembly | 1 + bookbinder | Generate final PDF; Alexander runs bookbinder handoff |
| **Total** | **~80 sessions** | At 1/day: 3 months. At 1/week: ~1.5 years. |

These are loose estimates. Substantial works often want two sessions (long
treatises, long speeches). Apparatus passes can be batched more aggressively
than translation because they're per-entity, not per-work.

## The per-session loop (what every Cowork session looks like)

1. **Read at session start:** `CLAUDE.md`, `STYLE.md`, `PROGRESS.md`'s "Where
   to resume now," and this file. No other input required from Alexander.
2. **Pick the next batch.** Default: read PROGRESS.md's suggested next batch.
   If the session is opening for translation, pick letters in chronological
   order from the pending set. If for apparatus, pick the next ~50 entity
   stubs or the next ~10 drafted works lacking judgment sidecars.
3. **Pre-fetch the batch's Latin** via `scripts/fetch_latin.py` so worker
   sub-agents don't deal with fetch issues.
4. **Dispatch worker sub-agents in parallel.** Standard pattern:
   - 3–5 agents in one parallel batch.
   - Each agent translates **3–5 short letters end-to-end** (or 1 substantial
     letter, or 1 medium speech).
   - Each agent reads `STYLE.md`, `CLAUDE.md` (selected sections), one finished
     adjacent letter as a register template, and the parallel-sidecar schema
     example. The PM gives every agent the same binding-reading list.
   - Worker scope: english/, headnotes/, data/parallel/<id>.json files only.
     **Workers do not touch** shared sidecars (letter-network, entities,
     greek-phrases), do not flip status in works.yaml, do not git anything.
5. **PM consolidates after the batch returns:**
   - Flip status: pending → drafted in `meta/works.yaml` for each finished work
     (using the anchor block discipline in CLAUDE.md §Status-flip discipline).
   - Correct any date discrepancies discovered by the workers (Perseus
     dateline often more precise than the year-precision placeholders in
     works.yaml).
   - Run `python scripts/backfill_structural.py` to regenerate the
     parallel/letter-network/greek-phrases corpus aggregates from the new
     per-work files.
   - Run `python scripts/build_manifest.py` to regenerate MANIFEST.md and
     `build/chronology.tex`.
   - Run `python scripts/validate.py`. Should return clean except for the
     pre-existing chronological-gap warning.
6. **Optionally dispatch another batch** if context budget allows.
7. **Update PROGRESS.md's "Where to resume now"** with: new drafted count;
   latest chronological pointer; date corrections committed; translator-notes
   worth carrying forward; next batch suggestion. This is the resume pointer
   the next Cowork session reads first.
8. **Stop on a clean batch boundary.** Tell Alexander: "Run
   `bash scripts/cowork_handoff.sh \"session N: brief\"` to land. Next
   session continues from <work-id>."

## Sub-agent prompt skeleton (multi-letter version)

When a worker handles 3–5 short letters:

```
You are a translation worker for the cicero-by-claude project.

ASSIGNED WORKS (translate in order, end-to-end each):
  - <id-1>: <date>, <one-line context>
  - <id-2>: ...
  - <id-3>: ...

INPUT FILES (already fetched, do NOT re-fetch):
  /Users/axwoods/Projects/cicero/latin/letters/<NNNbc>-<id-1>.tex
  /Users/axwoods/Projects/cicero/latin/letters/<NNNbc>-<id-2>.tex
  /Users/axwoods/Projects/cicero/latin/letters/<NNNbc>-<id-3>.tex

OUTPUT PER WORK (three files each):
  /Users/axwoods/Projects/cicero/english/letters/<NNNbc>-<id>.tex
  /Users/axwoods/Projects/cicero/headnotes/letters/<NNNbc>-<id>.tex
  /Users/axwoods/Projects/cicero/data/parallel/letters/<NNNbc>-<id>.json

BINDING READING (read once at the start, in order):
  1. /Users/axwoods/Projects/cicero/STYLE.md
  2. /Users/axwoods/Projects/cicero/CLAUDE.md (Translation conventions,
     File-header conventions, "What 'done' looks like" steps 2-3 and 4-parallel)
  3. /Users/axwoods/Projects/cicero/english/letters/<adjacent-drafted>.tex
  4. /Users/axwoods/Projects/cicero/headnotes/letters/<adjacent-drafted>.tex
  5. /Users/axwoods/Projects/cicero/data/parallel/letters/<adjacent>.json

JOB FOR EACH ASSIGNED WORK:
  Per STYLE.md: file header, \ciceroLetterOpener{LATIN SALUTATION},
  \ciceroSection{N}, Greek phrases as English + \textit{[Greek: trans]}.
  2-paragraph \textit{...} headnote.
  Parallel sidecar JSON schema_version:1 alignment_grain:"section",
  segments one per section, date from Perseus dateline if more precise
  than works.yaml.

HARD CONSTRAINTS — DO NOT:
  - Flip status in meta/works.yaml.
  - Touch data/letter-network.json, data/entities.json, data/greek-phrases.json,
    data/translator-notes.jsonl, MANIFEST.md, build/* .
  - Emit entities-mentions / glossary / allusions / crossrefs sidecars
    (deferred to a separate enrichment pass).
  - git commit / push / any git write commands (sandbox has a stuck index.lock).
  - Re-fetch the Latin.

Report once at the end, per work:
  - paths created
  - English word count
  - date used and any meta-entry discrepancy
  - Greek phrases handled
  - notable cruxes worth a translator-notes entry
```

## Sandbox constraints (what Cowork can't do)

Cowork runs in a sandbox with two relevant limits:

1. **No SSH access to `origin`.** `git fetch origin` and `git push` both fail.
   Cowork can stage changes locally but not push. Alexander's machine has the
   keys; pushing is part of the post-session handoff.
2. **No file deletion.** `rm`, `git clean -f`, `chmod` all return "Operation
   not permitted." If a fetch produces wrong content, Cowork can overwrite
   the file (with a placeholder stub explaining the issue) but not delete it.
   `git clean -f` on the user side handles cleanup.

A subtle consequence: any `git status` Cowork runs creates a `.git/index.lock`
which the sandbox then can't unlink. Until the lock is removed (by
`cowork_handoff.sh`), further git writes fail. So the PM should avoid running
`git status` mid-session; rely on the file system and validate.py instead.

## The handoff (what Alexander does after each session)

```bash
cd ~/Projects/cicero
bash scripts/cowork_handoff.sh "session N: brief description"
```

That single command:
- Removes any leftover `.git/index.lock`
- Removes the placeholder stub on `054bc-ad-familiares-13-49.tex` if present
- Stages all changes
- Commits with a project-PM message format
- Pushes to `origin/main`

If there's nothing to commit, the script exits cleanly.

## Phase 0 (this foundation session) — what got done

1. **Fixed `meta/works.yaml` for ad-familiares-13-49**: corrected the
   `speech_index` from `book:13,letter:49` to `book:13,letter:159` because
   Perseus's TEI mislabels this letter as n="159" (upstream typo). Corrected
   the date from the placeholder `-0054-07-01` to `-0047-10-15` per the
   Perseus dateline (`a. 707 (47)`). Renamed the file paths from `054bc-…`
   to `047bc-…`.
2. **Marked `ad-quintum-fratrem-03-06` as no_perseus**: Perseus TEI book 3
   contains letters 1,2,3,4,5,7,8,9 — no separate letter 6. Modern editions
   combine 3.6 with 3.5 (Shackleton Bailey numbers it 3.5b). When translating
   Q.fr 3.5, include 3.6 material in the same translation; mark this entry
   drafted in the same commit.
3. **Created `scripts/cowork_handoff.sh`** — one-command session landing.
4. **Wrote this file** (`OPERATING_PLAN.md`).
5. **Updated `CLAUDE.md`** with a "Cowork operating model" section pointing
   to this plan.
6. **Registered a daily scheduled Cowork session** (Alexander can disable
   from the Cowork UI if undesired).

## Known issues / followups

- **Other Perseus TEI numbering anomalies?** Only Fam 13.49 was found in the
   pending set. If other letters fail to fetch with `textpart letter=N not
   found`, check whether the letter exists in Perseus's TEI under a different
   `n` value (or is combined with an adjacent letter per modern editions).
- **`scripts/fetch_latin.py` enhancement candidates:** add an explicit
   `n_override` field in works.yaml that wins over the natural `n`, so future
   upstream typos can be patched without renaming `book:N,letter:M` to a
   misleading value. Not blocking; the current `speech_index` override path
   works.
- **Apparatus enrichment** still has 472 entity stubs and ~160 drafted works
   without entity-mention/glossary sidecars (see PROGRESS.md). These can be
   batched aggressively (parallel, ~50 entities per worker, no inter-batch
   conflicts).

## When the plan changes

Update this file. PROGRESS.md is the per-session resume pointer; this file
is the multi-session strategy. If the bound-volume scope changes, the
session estimate changes, or the per-session loop pattern improves, edit
here so the change is inherited by every subsequent Cowork session.
