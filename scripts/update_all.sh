#!/usr/bin/env bash
# update_all.sh — Incremental update of all Swiss law sources.
#
# Safe to run daily or weekly. Only fetches new or changed laws:
# - Federal: Fedlex SPARQL date-filtered query (fast)
# - Cantonal: re-fetches catalog per canton, compares version_date,
#   only downloads text for new or updated laws
#
# Usage:
#   ./scripts/update_all.sh              # default rate limit 0.1s
#   ./scripts/update_all.sh 0.5          # faster (0.5s between requests)
#   ./scripts/update_all.sh 2.0 --push   # slower + auto-push both repos

set -euo pipefail

RATE_LIMIT="${1:-0.1}"
PUSH="${2:-}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
VENV="${REPO}/.venv"
SITE_REPO="${SWISS_LAW_SITE_REPO:-${REPO}/../swiss-law-as-source}"

cd "$REPO"

echo "=== Swiss Law Incremental Update ==="
echo "Started: $(date -Iseconds)"
echo "Rate limit: ${RATE_LIMIT}s"
echo ""

COMMITS_BEFORE=$(git rev-list --count HEAD)

# ── 1. Federal laws (Fedlex SPARQL — date-filtered) ──────────────────────
echo "[1/5] Federal update..."
"${VENV}/bin/legalize-ch" update --repo "$REPO" --scope federal --rate-limit "$RATE_LIMIT" 2>&1

# ── 2. Cantonal laws (all 26, sequential to avoid git lock) ──────────────
echo ""
echo "[2/5] Cantonal update (26 cantons)..."
for canton in ag ai ar be bl bs fr ge gl gr ju lu ne nw ow sg sh so sz tg ti ur vd vs zg zh; do
    "${VENV}/bin/legalize-ch" update --repo "$REPO" --scope cantonal \
        -c "$canton" --rate-limit "$RATE_LIMIT" 2>&1 || {
        echo "WARNING: ${canton^^} failed, continuing..."
    }
done

# ── 3. Enrich categories for any new laws ─────────────────────────────────
echo ""
echo "[3/5] Enriching categories..."
"${VENV}/bin/legalize-ch" enrich-categories --repo "$REPO" --rate-limit 0.1 2>&1

COMMITS_AFTER=$(git rev-list --count HEAD)
NEW_COMMITS=$((COMMITS_AFTER - COMMITS_BEFORE))

echo ""
echo "[4/5] New commits: ${NEW_COMMITS}"

# ── 4. Regenerate stats + index ───────────────────────────────────────────
if [ -d "$SITE_REPO/.git" ]; then
    echo "Regenerating stats..."
    "${VENV}/bin/legalize-ch" stats --repo "$REPO" --site-repo "$SITE_REPO" --no-trees 2>&1
    "${VENV}/bin/legalize-ch" index --repo "$REPO" 2>&1
else
    echo "Site repo not found at ${SITE_REPO} — skipping stats."
fi

# ── 5. Push (if --push flag) ─────────────────────────────────────────────
if [ "$PUSH" = "--push" ]; then
    echo ""
    echo "[5/5] Pushing..."
    git push origin main 2>&1 && echo "  swiss-law pushed." || echo "  WARNING: swiss-law push failed."

    if [ -d "$SITE_REPO/.git" ]; then
        cd "$SITE_REPO"
        git add -A
        git diff --cached --quiet || {
            git commit -m "Update $(date +%Y-%m-%d): ${NEW_COMMITS} new law commits"
            git push origin main 2>&1 && echo "  swiss-law-as-source pushed." || echo "  WARNING: site push failed."
        }
    fi
else
    echo ""
    echo "[5/5] Skipping push (use --push to auto-push)."
fi

echo ""
echo "=== Done ==="
echo "New commits: ${NEW_COMMITS}"
echo "Finished: $(date -Iseconds)"
