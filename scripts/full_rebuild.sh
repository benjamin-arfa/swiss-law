#!/usr/bin/env bash
# full_rebuild.sh — Rebuild the ENTIRE data collection from scratch, then
# generate all site artifacts, publish, and notify.
#
# This is the "general routine for getting all the data": first run,
# backfill, enrichment, stats/index generation, site deploy — in the
# right order. Individual steps are idempotent/resumable, so re-running
# after an interruption continues rather than restarting.
#
# ⚠ RUNTIME: MULTIPLE DAYS at the default 1.5s rate limit — the federal
#   bootstrap fetches every consolidation version of ~9,000 laws in three
#   languages, plus 26 cantonal catalogs. Run it detached:
#     mkdir -p data/logs
#     nohup ./scripts/full_rebuild.sh > data/logs/full_rebuild_$(date +%Y%m%d).out 2>&1 &
#     tail -f data/logs/full_rebuild_*.out
#
# Prerequisites:
#   - .venv installed (pip install -e . / uv sync)
#   - /home/ubuntu/.env with GITHUB_TOKEN (for pushes)
#   - site repo cloned next door (or $SWISS_LAW_SITE_REPO)
#   - pdftotext installed (LexFind PDF extraction)
#
# If only the gitignored data/ state files were lost (machine rebuild),
# you do NOT need this — run `legalize-ch seed-state` instead.
#
# Usage: ./scripts/full_rebuild.sh [rate_limit]

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="${REPO_DIR}/.venv"
SITE_DIR="${SWISS_LAW_SITE_REPO:-/home/ubuntu/swiss-law-as-source}"
GITHUB_TOKEN_FILE="/home/ubuntu/.env"
RATE_LIMIT="${1:-0.1}"
START_TIME=$(date +%s)
ERRORS=""
PUSH_OK="true"

LOG_DIR="${REPO_DIR}/data/logs"
LOG_FILE="${LOG_DIR}/full_rebuild_$(date +%Y%m%d_%H%M%S).log"
mkdir -p "$LOG_DIR"

cd "$REPO_DIR"
exec > >(tee -a "$LOG_FILE") 2>&1

step() { echo ""; echo "════ $1 — $(date -Iseconds) ════"; }
fail() { echo "WARNING: $1"; ERRORS="${ERRORS:+${ERRORS}|||}$1"; }

configure_remote() {
    if [ -f "$GITHUB_TOKEN_FILE" ]; then
        GITHUB_TOKEN=$(grep -oP 'GITHUB_TOKEN=\K.*' "$GITHUB_TOKEN_FILE" | tr -d '[:space:]')
        [ -n "$GITHUB_TOKEN" ] && git remote set-url origin \
            "https://x-access-token:${GITHUB_TOKEN}@github.com/benjamin-arfa/swiss-law.git"
    fi
}

push_to_github() {
    local attempt=1
    while [ "$attempt" -le 3 ]; do
        git push origin main 2>&1 | grep -v 'x-access-token' && return 0
        attempt=$((attempt + 1)); sleep $((attempt * 5))
    done
    return 1
}

echo "=== Swiss Law FULL REBUILD ==="
echo "Started: $(date -Iseconds) (rate limit ${RATE_LIMIT}s)"
COMMITS_BEFORE=$(git rev-list --count HEAD)

step "[1/9] Bootstrap: federal (all versions) + all 26 cantons"
# Bootstrap resumes via data/ state: already-processed laws are skipped.
# Cantonal catalogs come from LexFind (full, incl. concordats) with
# LexWork/dedicated-fetcher text preferred and LexFind PDF fallback.
"${VENV}/bin/legalize-ch" bootstrap --repo "$REPO_DIR" --scope all \
    --rate-limit "$RATE_LIMIT" 2>&1 || fail "Bootstrap encountered errors"

step "[2/9] Backfill from LexFind (all catalog gaps)"
# Fetch anything the bootstrap missed across ALL 26 cantons (dedicated
# fetchers have partial catalogs; LexFind is authoritative). Add-only.
"${VENV}/bin/legalize-ch" backfill-lexfind --repo "$REPO_DIR" \
    --rate-limit "$RATE_LIMIT" 2>&1 || fail "LexFind backfill failed"

step "[3/9] Enrich categories (gap-fill, idempotent)"
"${VENV}/bin/legalize-ch" enrich-categories --repo "$REPO_DIR" --rate-limit 0.1 2>&1 \
    || fail "Category enrichment failed"

step "[4/9] Enrich dates: local parse + git history, then authoritative LexWork API, then sibling propagation"
"${VENV}/bin/legalize-ch" enrich-dates --repo "$REPO_DIR" 2>&1 || fail "Local date pass failed"
"${VENV}/bin/legalize-ch" enrich-dates --repo "$REPO_DIR" --lexwork-versions --rate-limit 0.1 2>&1 \
    || fail "LexWork date pass failed"
"${VENV}/bin/legalize-ch" enrich-dates --repo "$REPO_DIR" --siblings 2>&1 || fail "Sibling propagation failed"

step "[5/9] Enrich domains (inference for unclassified) + repeal status"
"${VENV}/bin/legalize-ch" enrich-domains --repo "$REPO_DIR" 2>&1 || fail "Domain inference failed"
"${VENV}/bin/legalize-ch" enrich-types --repo "$REPO_DIR" 2>&1 || fail "Type inference failed"
"${VENV}/bin/legalize-ch" enrich-status --repo "$REPO_DIR" --rate-limit 0.1 2>&1 || fail "Status enrichment failed"
git add ch/ && git diff --cached --quiet || git commit -q -m "Full rebuild: enrichment passes (dates, domains, status)"

step "[6/9] Stats (with category trees) + tags + publications + law index"
"${VENV}/bin/legalize-ch" stats --repo "$REPO_DIR" --site-repo "$SITE_DIR" \
    --rate-limit 0.1 2>&1 || fail "Stats generation failed"

step "[7/9] Search index (laws.json + INDEX.md)"
"${VENV}/bin/legalize-ch" index --repo "$REPO_DIR" --site-repo "$SITE_DIR" 2>&1 \
    || fail "Index generation failed"

step "[8/9] Supplementary artifacts (cross-refs, feeds)"
"${VENV}/bin/legalize-ch" cross-level-refs --repo "$REPO_DIR" 2>&1 || fail "cross-level-refs failed"
"${VENV}/bin/legalize-ch" feed --repo "$REPO_DIR" 2>&1 || fail "feed generation failed"

# The generated pages carry their own navbar; re-normalise the whole site so the
# header and nav stay identical everywhere (see scripts/sync_site_nav.py).
SWISS_LAW_SITE_REPO="$SITE_DIR" "${VENV}/bin/python" "${REPO_DIR}/scripts/sync_site_nav.py" 2>&1 \
    || fail "navbar sync failed"

step "[9/9] Publish: site deploy + law-repo push"
COMMITS_AFTER=$(git rev-list --count HEAD)
NEW_COMMITS=$((COMMITS_AFTER - COMMITS_BEFORE))
if [ -d "$SITE_DIR/.git" ]; then
    "${REPO_DIR}/scripts/deploy_site.sh" "Full rebuild $(date +%Y-%m-%d)" 2>&1 \
        || fail "Site deploy failed"
else
    fail "Site repo not found at ${SITE_DIR}"
fi
configure_remote
UNPUSHED=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo "unknown")
if [ "$UNPUSHED" != "0" ] && [ "$UNPUSHED" != "unknown" ]; then
    push_to_github || { PUSH_OK="false"; fail "Law-repo push failed after retries"; }
fi

FINAL_UNPUSHED=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo "0")
DURATION=$(( $(date +%s) - START_TIME ))
echo ""
echo "Sending Telegram notification..."
"${VENV}/bin/python" -c "
import sys
sys.path.insert(0, '${REPO_DIR}/src')
from legalize_ch.notify import PipelineResult, send_telegram
errors = [e for e in '''${ERRORS}'''.split('|||') if e.strip()]
result = PipelineResult(
    new_commits=${NEW_COMMITS}, laws_checked=0, errors=errors,
    push_ok=$([[ "$PUSH_OK" == "true" ]] && echo "True" || echo "False"),
    unpushed=${FINAL_UNPUSHED}, duration_seconds=${DURATION}, mode='full-rebuild',
)
sys.exit(0 if send_telegram(result) else 1)
" && echo "  Notification sent." || echo "  WARNING: Notification failed."

echo ""
echo "=== Full rebuild done: $(date -Iseconds) (${NEW_COMMITS} new commits) ==="
echo "Log: ${LOG_FILE}"
