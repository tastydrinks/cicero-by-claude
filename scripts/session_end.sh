#!/usr/bin/env bash
# session_end.sh --- the canonical last action of every Claude session
# working on this project.
#
# Pushes the current session branch to origin and, if main is behind,
# fast-forwards origin/main to the session branch's tip. This makes
# `main` the always-correct durable tip so the next session (which
# may be assigned a freshly-named session branch by the harness) can
# start from `main` and not have to hunt for the latest work.
#
# Run: bash scripts/session_end.sh
set -euo pipefail

cd "$(dirname "$0")/.."

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
LOCAL_TIP="$(git rev-parse HEAD)"

if [ -n "$(git status --porcelain)" ]; then
  echo "ERROR: working tree is not clean. Commit or stash before running this script."
  git status --short
  exit 1
fi

echo "Current branch: $CURRENT_BRANCH"
echo "Local tip:      $LOCAL_TIP"
echo

# 1. Push the session branch to its own ref on origin.
echo "--- git push origin $CURRENT_BRANCH ---"
git push -u origin "$CURRENT_BRANCH"
echo

# 2. Fast-forward origin/main to the same tip.
# This is the durable handoff: every future session starts from origin/main.
echo "--- git push origin HEAD:main ---"
if git push origin "HEAD:main"; then
  echo "✓ origin/main now at $LOCAL_TIP"
else
  echo
  echo "WARNING: push to main was rejected. Either branch protection is on,"
  echo "or main has commits that the session branch does not. In either case"
  echo "the session branch is safe; reconcile by hand or open a PR."
  exit 1
fi
