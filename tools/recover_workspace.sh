#!/usr/bin/env bash
# Recover the study workspace after the sandbox re-seeds from an old upload snapshot.
#
# Symptom: `git log --oneline` shows only "04b80df Initial commit", the
# Paperlords_Archive/IGCSE/ tree has disappeared, and everything shows as
# untracked (?? Business_Studies_Answer_Bank/, ?? uploads/, ...).
#
# Cause: the workspace is re-seeded from a newer upload of /home/user, which
# replaces the checkout. The repository itself is fine.
#
# Fix: our branch on the remote is authoritative. Fetch it and hard-reset to it.
#
# Usage:  bash tools/recover_workspace.sh
set -euo pipefail
cd "$(dirname "$0")/.."

BRANCH="arena/031beb1c-igcse-omega"

echo "== before =="
git log --oneline -1 || true
echo

echo "== fetching origin =="
git fetch origin "$BRANCH"

echo
echo "== resetting to origin/$BRANCH =="
git reset --hard "origin/$BRANCH"

echo
echo "== reinstalling the PDF libraries (a re-seed always loses them) =="
python3 -c "import pypdf" 2>/dev/null && echo "pypdf already present" \
  || pip install --break-system-packages -q pypdf pymupdf cryptography
python3 -c "import pypdf, pymupdf; print('pypdf + pymupdf OK')"

echo
echo "== after =="
git log --oneline -3
echo
printf 'Perfect_Answers files: %s\n' "$(ls Business_Studies_Answer_Bank/Perfect_Answers 2>/dev/null | wc -l)"
printf 'External exemplars:    %s\n' "$(ls Business_Studies_Answer_Bank/Perfect_Answers/External_Exemplars 2>/dev/null | wc -l)"
printf '4BS1 sessions:         %s\n' "$(ls Paperlords_Archive/IGCSE/4BS1_Business_Studies 2>/dev/null | wc -l)"
echo
echo "Any file the upload added that is newer than this commit must be re-added manually:"
git status --short
