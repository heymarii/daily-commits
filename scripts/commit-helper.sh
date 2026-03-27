#!/bin/bash
# commit-helper.sh — Quick commit + push
# Usage: ./scripts/commit-helper.sh "Your commit message"

if [ -z "$1" ]; then
  echo "Usage: ./scripts/commit-helper.sh 'commit message'"
  exit 1
fi

git add -A
git commit -m "$1"
git push

echo "✅ Committed and pushed: $1"
