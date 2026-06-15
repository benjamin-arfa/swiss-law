#!/bin/bash
# Fetch all missing cantonal law texts sequentially.
# Cantons are fetched via LexFind PDF extraction (pdftotext).
set -e

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

RATE_LIMIT="${1:-0.3}"

# ZH uses dedicated fetcher (zh.ch API), rest use LexFind PDF
CANTONS="zh ai ju nw ow sh sz ti ur vd"

for canton in $CANTONS; do
    echo ""
    echo "=== Fetching ${canton^^} ==="
    echo ""
    python3 -m legalize_ch.cli bootstrap \
        --repo . \
        --scope cantonal \
        -c "$canton" \
        --rate-limit "$RATE_LIMIT" || {
        echo "WARNING: ${canton^^} fetch failed, continuing..."
        continue
    }
    echo "${canton^^} done."
done

echo ""
echo "=== All cantons fetched ==="
find ch/ -name "*.md" | cut -d/ -f2 | sort | uniq -c | sort -rn
