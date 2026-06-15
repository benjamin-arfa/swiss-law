#!/usr/bin/env bash
# deploy_site.sh — Commit and push the swiss-law-as-source site repo.
#
# The site repo lives at ../swiss-law-as-source (relative to this script's
# parent repo).  The pipeline writes HTML/JSON/API files there directly;
# this script just commits and pushes.
#
# Usage: ./scripts/deploy_site.sh [commit message]

set -euo pipefail

SITE_DIR="${SWISS_LAW_SITE_REPO:-/home/ubuntu/swiss-law-as-source}"
COMMIT_MSG="${1:-Deploy site}"

if [ ! -d "$SITE_DIR/.git" ]; then
    echo "Site repo not found at $SITE_DIR"
    echo "Clone it first: git clone git@github.com:swiss-law-as-source/swiss-law-as-source.github.io.git $SITE_DIR"
    exit 1
fi

cd "$SITE_DIR"

if git diff --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "No changes to deploy."
    exit 0
fi

git add -A
CHANGED=$(git diff --cached --stat | tail -1)
echo "Changes: $CHANGED"

git commit -m "$COMMIT_MSG" --quiet
git push origin main --quiet

echo "Deployed successfully."
