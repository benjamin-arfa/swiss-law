#!/usr/bin/env bash
# enrich_dates_lexwork.sh — Authoritative enactment + version dates from the
# LexWork portals (+ ZH), one API call per law. LONG-RUNNING (~5-6 h for all
# cantons at 1.0 s rate limit); resumable (state in data/state/), safe to
# interrupt and re-run.
#
# Usage:
#   ./scripts/enrich_dates_lexwork.sh [rate_limit] [canton ...]
# Recommended:
#   mkdir -p data/logs
#   nohup ./scripts/enrich_dates_lexwork.sh 1.0 > data/logs/enrich_dates_$(date +%Y%m%d).out 2>&1 &
#
# On completion: commits, regenerates stats + indexes, deploys the site,
# pushes the law repo, and sends a Telegram summary (mode: enrich-dates).

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="${REPO_DIR}/.venv"
SITE_DIR="${SWISS_LAW_SITE_REPO:-/home/ubuntu/swiss-law-as-source}"
GITHUB_TOKEN_FILE="/home/ubuntu/.env"
RATE_LIMIT="${1:-0.2}"
shift || true
CANTONS=("$@")
if [ ${#CANTONS[@]} -eq 0 ]; then
    CANTONS=(ag ar be bl bs fr gl gr lu sg so tg vs zg)
fi
START_TIME=$(date +%s)
ERRORS=""
PUSH_OK="true"

LOG_DIR="${REPO_DIR}/data/logs"
mkdir -p "$LOG_DIR"
cd "$REPO_DIR"
exec > >(tee -a "${LOG_DIR}/enrich_dates_$(date +%Y%m%d_%H%M%S).log") 2>&1

echo "=== LexWork date enrichment ==="
echo "Started: $(date -Iseconds) — cantons: ${CANTONS[*]} (rate ${RATE_LIMIT}s)"
COMMITS_BEFORE=$(git rev-list --count HEAD)

for canton in "${CANTONS[@]}"; do
    echo "--- Canton ${canton^^} ---"
    if ! "${VENV}/bin/legalize-ch" enrich-dates --repo "$REPO_DIR" --lexwork-versions \
            -c "$canton" --rate-limit "$RATE_LIMIT" 2>&1; then
        echo "WARNING: ${canton^^} failed, continuing..."
        ERRORS="${ERRORS:+${ERRORS}|||}${canton^^} date enrichment failed"
    fi
    git add "ch/${canton}" 2>/dev/null
    if ! git diff --cached --quiet; then
        git commit -q -m "Enrich ${canton^^}: enactment + version dates from LexWork API"
    fi
done

NEW_COMMITS=$(( $(git rev-list --count HEAD) - COMMITS_BEFORE ))
echo "=== Enrichment finished: ${NEW_COMMITS} commits ==="

echo "Regenerating stats + indexes..."
"${VENV}/bin/legalize-ch" stats --repo "$REPO_DIR" --site-repo "$SITE_DIR" --no-trees 2>&1 \
    || ERRORS="${ERRORS:+${ERRORS}|||}Stats generation failed"
"${VENV}/bin/legalize-ch" index --repo "$REPO_DIR" --site-repo "$SITE_DIR" 2>&1 \
    || ERRORS="${ERRORS:+${ERRORS}|||}Index generation failed"
"${REPO_DIR}/scripts/deploy_site.sh" "Date enrichment $(date +%F): authoritative enactment + version dates" 2>&1 \
    || ERRORS="${ERRORS:+${ERRORS}|||}Site deploy failed"

if [ -f "$GITHUB_TOKEN_FILE" ]; then
    GITHUB_TOKEN=$(grep -oP 'GITHUB_TOKEN=\K.*' "$GITHUB_TOKEN_FILE" | tr -d '[:space:]')
    [ -n "$GITHUB_TOKEN" ] && git remote set-url origin \
        "https://x-access-token:${GITHUB_TOKEN}@github.com/benjamin-arfa/swiss-law.git"
fi
UNPUSHED=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo 0)
if [ "$UNPUSHED" != "0" ]; then
    git push origin main 2>&1 | grep -v 'x-access-token' || {
        PUSH_OK="false"; ERRORS="${ERRORS:+${ERRORS}|||}Push failed"; }
fi

DURATION=$(( $(date +%s) - START_TIME ))
"${VENV}/bin/python" -c "
import sys
sys.path.insert(0, '${REPO_DIR}/src')
from legalize_ch.notify import PipelineResult, send_telegram
errors = [e for e in '''${ERRORS}'''.split('|||') if e.strip()]
result = PipelineResult(new_commits=${NEW_COMMITS}, laws_checked=0, errors=errors,
    push_ok=$([[ "$PUSH_OK" == "true" ]] && echo "True" || echo "False"),
    unpushed=0, duration_seconds=${DURATION}, mode='enrich-dates')
sys.exit(0 if send_telegram(result) else 1)
" && echo "Notification sent." || echo "WARNING: notification failed."
echo "=== Done: $(date -Iseconds) ==="
