#!/usr/bin/env bash
# backfill_lexfind.sh — Import laws missing locally from LexFind (add-only).
#
# LexWork collections and ZH's capped catalog lack whole sections (notably
# intercantonal concordats). This imports only the missing laws; existing
# files are never overwritten, so the run is safe to interrupt and re-run —
# it resumes where it stopped.
#
# Usage:
#   ./scripts/backfill_lexfind.sh [rate_limit] [canton ...]
#     rate_limit  seconds between API requests (default 1.5)
#     canton ...  canton codes (default: 14 LexWork cantons + zh)
#
# Recommended: run detached, it takes hours for a full pass:
#   mkdir -p data/logs
#   nohup ./scripts/backfill_lexfind.sh 1.5 > data/logs/backfill_$(date +%Y%m%d).out 2>&1 &
#   tail -f data/logs/backfill_*.out
#
# Afterwards (see .claude/commands/backfill-lexfind.md):
#   .venv/bin/legalize-ch stats --repo . --site-repo ../swiss-law-as-source --no-trees
#   .venv/bin/legalize-ch index --repo . --site-repo ../swiss-law-as-source
#   then publish via /publish-site

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="${REPO_DIR}/.venv"
RATE_LIMIT="${1:-1.5}"
shift || true
CANTONS=("$@")
if [ ${#CANTONS[@]} -eq 0 ]; then
    CANTONS=(ag ar be bl bs fr gl gr lu sg so tg vs zg zh)
fi

LOG_DIR="${REPO_DIR}/data/logs"
LOG_FILE="${LOG_DIR}/backfill_$(date +%Y%m%d_%H%M%S).log"
mkdir -p "$LOG_DIR"

cd "$REPO_DIR"

echo "=== LexFind Backfill ===" | tee -a "$LOG_FILE"
echo "Started: $(date -Iseconds)" | tee -a "$LOG_FILE"
echo "Cantons: ${CANTONS[*]} (rate limit ${RATE_LIMIT}s)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

FAILED=""
for canton in "${CANTONS[@]}"; do
    echo "--- Canton ${canton^^} ---" | tee -a "$LOG_FILE"
    if ! "${VENV}/bin/legalize-ch" backfill-lexfind --repo "$REPO_DIR" \
            -c "$canton" --rate-limit "$RATE_LIMIT" 2>&1 | tee -a "$LOG_FILE"; then
        echo "WARNING: Canton ${canton^^} backfill failed, continuing..." | tee -a "$LOG_FILE"
        FAILED="${FAILED} ${canton^^}"
    fi
done

echo "" | tee -a "$LOG_FILE"
echo "=== Backfill finished: $(date -Iseconds) ===" | tee -a "$LOG_FILE"
[ -n "$FAILED" ] && echo "Failed cantons:${FAILED} (re-run to retry — resume is automatic)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "Next steps:" | tee -a "$LOG_FILE"
echo "  .venv/bin/legalize-ch stats --repo . --site-repo ../swiss-law-as-source --no-trees" | tee -a "$LOG_FILE"
echo "  .venv/bin/legalize-ch index --repo . --site-repo ../swiss-law-as-source" | tee -a "$LOG_FILE"
echo "  then publish via /publish-site (or ./scripts/deploy_site.sh)" | tee -a "$LOG_FILE"
