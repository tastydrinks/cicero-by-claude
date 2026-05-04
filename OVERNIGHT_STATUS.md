# Overnight status — 2026-05-04

This file is the wake-up note Alexander finds when he opens GitHub.
Auto-deleted once read; not part of the project's permanent docs.

## Two things you need to do (5 minutes total when you wake up)

### 1. Reset the OAuth secret (described in detail below)

### 2. Delete 12 merged session branches

The harness's git server refuses branch deletions, so they accumulate
on `origin`. All of the branches below are strict ancestors of `main`
(their work is already merged) and safe to delete. **Bulk-delete via
the GitHub web UI**: repo → **Branches** → trash icon next to each.
GitHub mobile shows the same trash icon.

Safe to delete (12):

- `claude/add-internal-hyperlinks-7O761`
- `claude/astro-github-pages-setup-oSdgK`
- `claude/research-similar-projects-Y60aO`
- `claude/translate-ad-familiares-13-nVJvr`
- `claude/translate-cicero-letters-4KyOj`
- `claude/translate-cicero-letters-ki3FG`
- `claude/translate-cicero-works-krtUO`
- `claude/translate-cicero-works-kv81y`
- `claude/translate-latin-letters-6xISV`
- `claude/translate-latin-letters-TznHk`
- `claude/translate-latin-works-VBQT5`
- `claude/verrines-actio-secunda-sidecars-GO9V2`

Keep: `main` only.

I cannot delete these myself — confirmed: harness git refuses
deletions (HTTP 403), no `delete_branch` tool exists in my GitHub
MCP, no API token with `repo` scope is available in my environment.
You're the only path to a clean branch list.

---

## What you need to do (5 minutes when you wake up)

**Reset the `CLAUDE_CODE_OAUTH_TOKEN` secret in GitHub.** The PM-Claude
orchestration workflow is wired correctly but the OAuth token in repo
secrets is malformed — three test attempts on issue #1 have failed:

1. Attempt 1: missing `id-token: write` permission. Fixed (commit `359bca6`).
2. Attempt 2: wrong parameter name (`anthropic_api_key` instead of
   `claude_code_oauth_token`). Fixed (commit `8f7605d`).
3. Attempt 3: error `API Error: Header '14' has invalid value: '***'`.
   The `***` is GitHub's redaction of the secret value in logs —
   confirming the secret IS being read, but the HTTP library is
   rejecting it as a malformed header value. Almost always means the
   secret has invalid characters: trailing newline, leading whitespace,
   or got truncated in the paste.

**Steps:**

1. GitHub repo → **Settings** → **Secrets and variables** → **Actions**.
2. Click **Update** next to `CLAUDE_CODE_OAUTH_TOKEN`.
3. Re-paste the OAuth token from `claude setup-token`. Make sure
   there's no trailing whitespace or newline. Most clipboard tools
   include them on copy — paste, then arrow-right to end-of-field
   and verify there's nothing after the last character.
4. Save.
5. Re-comment `@claude please retry the test task on this issue` on
   issue [#1](https://github.com/tastydrinks/cicero-by-claude/issues/1).
6. If a fresh paste doesn't work, run `claude setup-token` again to
   generate a new token; that flow shouldn't produce malformed output.

Once a test attempt succeeds, the orchestration is unblocked and I can
dispatch real translation/infrastructure batches via `@claude` mentions
on issues. Until then, your manual launches are the only path for
parallel translation work.

## What I did overnight

**Merged work to main:**
- Agent D's hyperlinked scholar PDF: `build/output/cicero-v0.3-scholar.pdf`
  is on `main`. 198 works × hyperlinked entities + cross-references.
- Agent B's and Agent C's recommendation letters (Fam 13.x cluster,
  Q.fr. 2.7, Att 4.9–4.11, Tiro 16.13). Already merged before I ran
  finalizer; counted in the 198 total.

**Status numbers** (post-finalization):
- Drafted: 198 / 958 (~20%)
- Latest drafted: ad-familiares-01-10 (Dec 54 BC)
- Earliest pending: ad-familiares-13-49 + the year-precision July 54 BC cluster
- Validator: 7 warnings (chronological gap only); 0 errors.

**Infrastructure:**
- `.github/workflows/claude.yml` — PM-Claude orchestration workflow
  (waiting on the OAuth secret fix above).
- `.github/workflows/web-deploy.yml` — Tier 2 deploy (working;
  rebuilds site automatically on every push touching `web/`,
  `meta/`, `data/`, or prose dirs).
- `README.md` rewritten for the multi-surface vision (bound book,
  hyperlinked PDF, web edition, agent-discoverable corpus).
- `PROGRESS.md` "Where to resume now" updated with current state.
- `PLAN.md` status table updated (Tier 1 + Tier 2 Phase 2.1 shipped).

**Continuing work for the rest of the night:** Tier 2 Phase 2.2
(per-work pages with Latin/English toggle) — doable from this session
without the orchestration. If I get further (Phase 2.3 timeline,
Phase 2.4 glossary), I'll keep going.

## Where to find what I did

- All commits on `main` since `b71a4c6`: `git log --oneline b71a4c6..HEAD`
- This file, `OVERNIGHT_STATUS.md`, was written at session start; updates
  appear at the top as the night progresses.
- `PROGRESS.md` is current.

## Quick verification when you wake

```bash
git log --oneline -10                                # see what landed
python scripts/validate.py                           # confirm clean
python scripts/assemble_book.py --profile scholar    # rebuild PDF
ls -la build/output/                                 # see milestone PDFs
```

The web edition should be live at:
https://tastydrinks.github.io/cicero-by-claude/
(once GitHub has rebuilt after the README + PROGRESS push.)
