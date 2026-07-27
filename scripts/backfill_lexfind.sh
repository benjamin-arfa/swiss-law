#!/usr/bin/env bash
# backfill_lexfind.sh — Import laws missing locally from LexFind (add-only),
# then rebuild + publish the website and send a Telegram summary.
#
# LexWork collections and ZH's capped catalog lack whole sections (notably
# intercantonal concordats). This imports only the missing laws; existing
# files are never overwritten, so the run is safe to interrupt and re-run —
# it resumes where it stopped.
#
# Usage:
#   ./scripts/backfill_lexfind.sh [--no-publish] [rate_limit] [canton ...]
#     --no-publish  skip the final stats/index/site-deploy/push/notify chain
#     rate_limit    seconds between API requests (default 1.5)
#     canton ...    canton codes (default: 14 LexWork cantons + zh)
#
# Recommended: run detached, it takes hours for a full pass:
#   mkdir -p data/logs
#   nohup ./scripts/backfill_lexfind.sh 1.5 > data/logs/backfill_$(date +%Y%m%d).out 2>&1 &
#   tail -f data/logs/backfill_*.out
#
# On completion (unless --no-publish): regenerates stats + search index +
# law index, deploys the site repo, pushes the law repo, and sends a
# Telegram notification.

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="${REPO_DIR}/.venv"
SITE_DIR="${SWISS_LAW_SITE_REPO:-/home/ubuntu/swiss-law-as-source}"
GITHUB_TOKEN_FILE="/home/ubuntu/.env"
START_TIME=$(date +%s)
ERRORS=""
PUSH_OK="true"

PUBLISH="true"
if [ "${1:-}" = "--no-publish" ]; then
    PUBLISH="false"
    shift
fi
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

exec > >(tee -a "$LOG_FILE") 2>&1

configure_remote() {
    if [ -f "$GITHUB_TOKEN_FILE" ]; then
        GITHUB_TOKEN=$(grep -oP 'GITHUB_TOKEN=\K.*' "$GITHUB_TOKEN_FILE" | tr -d '[:space:]')
        if [ -n "$GITHUB_TOKEN" ]; then
            git remote set-url origin "https://x-access-token:${GITHUB_TOKEN}@github.com/benjamin-arfa/swiss-law.git"
            echo "Remote URL updated from token file."
        else
            echo "WARNING: GITHUB_TOKEN is empty in ${GITHUB_TOKEN_FILE}"
        fi
    else
        echo "WARNING: Token file not found at ${GITHUB_TOKEN_FILE}"
    fi
}

push_to_github() {
    local max_retries=3 attempt=1
    while [ "$attempt" -le "$max_retries" ]; do
        echo "  Push attempt ${attempt}/${max_retries}..."
        if git push origin main 2>&1 | grep -v 'x-access-token'; then
            echo "  Push successful."
            return 0
        fi
        attempt=$((attempt + 1))
        [ "$attempt" -le "$max_retries" ] && sleep $((attempt * 5))
    done
    echo "ERROR: Push failed after ${max_retries} attempts."
    return 1
}

send_notification() {
    local new_commits="$1" unpushed="$2" push_ok="$3" errors="$4"
    local duration=$(( $(date +%s) - START_TIME ))
    echo ""
    echo "Sending Telegram notification..."
    "${VENV}/bin/python" -c "
import sys
sys.path.insert(0, '${REPO_DIR}/src')
from legalize_ch.notify import PipelineResult, send_telegram

errors = [e for e in '''${errors}'''.split('|||') if e.strip()]
result = PipelineResult(
    new_commits=${new_commits},
    laws_checked=0,
    errors=errors,
    push_ok=$([[ "$push_ok" == "true" ]] && echo "True" || echo "False"),
    unpushed=${unpushed},
    duration_seconds=${duration},
    mode='backfill',
)
ok = send_telegram(result)
sys.exit(0 if ok else 1)
" && echo "  Notification sent." || echo "  WARNING: Notification failed."
}

echo "=== LexFind Backfill ==="
echo "Started: $(date -Iseconds)"
echo "Cantons: ${CANTONS[*]} (rate limit ${RATE_LIMIT}s, publish=${PUBLISH})"
echo ""

COMMITS_BEFORE=$(git rev-list --count HEAD)

for canton in "${CANTONS[@]}"; do
    echo "--- Canton ${canton^^} ---"
    if ! "${VENV}/bin/legalize-ch" backfill-lexfind --repo "$REPO_DIR" \
            -c "$canton" --rate-limit "$RATE_LIMIT" 2>&1; then
        echo "WARNING: Canton ${canton^^} backfill failed, continuing..."
        ERRORS="${ERRORS:+${ERRORS}|||}Canton ${canton^^} backfill failed"
    fi
done

COMMITS_AFTER=$(git rev-list --count HEAD)
NEW_COMMITS=$((COMMITS_AFTER - COMMITS_BEFORE))

echo ""
echo "=== Backfill finished: $(date -Iseconds) — ${NEW_COMMITS} new commits ==="

if [ "$PUBLISH" != "true" ]; then
    echo ""
    echo "--no-publish: skipping stats/index/deploy/push/notify."
    echo "Manual next steps:"
    echo "  ${VENV}/bin/legalize-ch stats --repo . --site-repo ${SITE_DIR} --no-trees"
    echo "  ${VENV}/bin/legalize-ch index --repo . --site-repo ${SITE_DIR}"
    echo "  then publish via /publish-site (or ./scripts/deploy_site.sh)"
    exit 0
fi

# ─── Rebuild + publish chain (failures never abort — data is committed) ───
if [ -d "$SITE_DIR/.git" ]; then
    echo ""
    echo "Regenerating stats + indexes into site repo (${SITE_DIR})..."
    "${VENV}/bin/legalize-ch" stats --repo "$REPO_DIR" --site-repo "$SITE_DIR" --no-trees 2>&1 || {
        ERRORS="${ERRORS:+${ERRORS}|||}Stats generation failed"
    }
    "${VENV}/bin/legalize-ch" index --repo "$REPO_DIR" --site-repo "$SITE_DIR" 2>&1 || {
        ERRORS="${ERRORS:+${ERRORS}|||}Index generation failed"
    }

    echo "Deploying site repo..."
    "${REPO_DIR}/scripts/deploy_site.sh" "Backfill $(date +%Y-%m-%d): ${NEW_COMMITS} new law commits" 2>&1 || {
        echo "WARNING: Site deploy failed."
        ERRORS="${ERRORS:+${ERRORS}|||}Site deploy failed"
    }
else
    echo "Site repo not found at ${SITE_DIR} — skipping site rebuild."
    ERRORS="${ERRORS:+${ERRORS}|||}Site repo missing"
fi

echo "Configuring GitHub remote..."
configure_remote
UNPUSHED=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo "unknown")
echo "  Unpushed commits: ${UNPUSHED}"
if [ "$UNPUSHED" != "0" ] && [ "$UNPUSHED" != "unknown" ]; then
    push_to_github || {
        PUSH_OK="false"
        ERRORS="${ERRORS:+${ERRORS}|||}Law-repo push failed after retries"
    }
else
    echo "  Remote is up to date — skipping push."
fi

FINAL_UNPUSHED=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo "0")
send_notification "$NEW_COMMITS" "$FINAL_UNPUSHED" "$PUSH_OK" "$ERRORS"

echo ""
echo "=== Done: $(date -Iseconds) ==="
echo "Log: ${LOG_FILE}"
