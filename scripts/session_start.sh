#!/usr/bin/env bash
# session_start.sh --- the canonical first action of every Claude session
# working on this project.
#
# Why this exists: the harness assigns a fresh branch name per session
# (claude/setup-cicero-project-fLUZH-<random>), and `main` is the durable
# tip that every session merges back into at session end. This script
# (a) makes sure your session branch starts at origin/main's tip, and
# (b) prints the resume pointer (the chronologically next pending work)
# so the agent isn't reading STYLE.md or PROGRESS.md to figure out where
# to begin.
#
# Run: bash scripts/session_start.sh
set -euo pipefail

cd "$(dirname "$0")/.."

# 1. Make sure we have the latest origin/main.
git fetch origin --quiet

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
LOCAL_TIP="$(git rev-parse HEAD)"
MAIN_TIP="$(git rev-parse origin/main 2>/dev/null || echo MISSING)"

echo "Current branch: $CURRENT_BRANCH"
echo "Local tip:      $LOCAL_TIP"
echo "origin/main:    $MAIN_TIP"
echo

# 2. If the current branch's tip is not equal to and not ahead of origin/main,
# we need to fast-forward the session branch up to main before continuing.
if [ "$MAIN_TIP" = "MISSING" ]; then
  echo "WARNING: origin/main not found. Skipping fast-forward check."
elif git merge-base --is-ancestor "$MAIN_TIP" "$LOCAL_TIP"; then
  echo "✓ Branch is at-or-ahead-of origin/main. Continuing."
else
  echo "↻ Branch is behind origin/main; fast-forwarding."
  git reset --hard "origin/main"
  echo "  Now at $(git rev-parse HEAD)"
fi
echo

# 3. Run the validator. Chronological-gap warnings tell the agent if a
# previous session skipped past anything.
echo "--- scripts/validate.py ---"
python3 scripts/validate.py || true
echo

# 4. Print the chronologically-next pending work.
echo "--- next pending work (chronological) ---"
python3 - <<'PY'
import yaml
works = yaml.safe_load(open('meta/works.yaml').read())
def key(w):
    s = w['date']
    if s.startswith('-'):
        y, rest = s[1:].split('-', 1); y = -int(y)
    else:
        y, rest = s.split('-', 1); y = int(y)
    m, d = rest.split('-')
    return (y, int(m), int(d), w['id'])
DEFERRED = {'aratea', 'de-inventione'}
pending = [w for w in works if w.get('status') == 'pending' and w['id'] not in DEFERRED]
pending.sort(key=key)
print(f'{len(pending)} pending entries. The next 5 chronologically:')
for w in pending[:5]:
    print(f'  {w["date"]} ({w["date_precision"]:10s}) {w["category"]:9s} {w["id"]:30s} {w["title_english"][:50]}')
PY
