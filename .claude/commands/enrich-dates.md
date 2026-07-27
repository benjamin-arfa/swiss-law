Back-fill enactment dates and version-date lists — laws are (law, version) pairs, and all site analytics use the ORIGINAL enactment date (a 1970 concordat amended in 2015 counts as 1970).

## Passes

1. **Local pass (fast, no network — run anytime, also in the weekly cron):**
   ```
   .venv/bin/legalize-ch enrich-dates --repo .
   ```
   Parses "vom/du/del D. Month YYYY" from stored law texts (~93% hit rate) and derives federal version histories from git commits. Idempotent, fill-missing-only.

2. **LexWork API pass (authoritative; ~5-6 h for all 14 cantons — run detached):**
   ```
   mkdir -p data/logs
   nohup ./scripts/enrich_dates_lexwork.sh 1.0 > data/logs/enrich_dates_$(date +%Y%m%d).out 2>&1 &
   ```
   One API call per law → `date_of_decision` (original enactment) + the full version-date list. Resumable (state in `data/state/`); on completion it commits per canton, regenerates stats + indexes, deploys the site, pushes, and sends a Telegram summary (`mode: enrich-dates`). Do not run concurrently with a backfill (git contention).

## Fields written (fill-missing-only, sources never overwritten)
`enactment_date` + `enactment_date_source` (lexwork_api | text | git_history), `version_dates` + `version_dates_source`. Inspect per law in `api/v1/laws/{ENTITY}.json`.

3. **Sibling propagation (AFTER the LexWork pass; local, seconds):**
   ```
   .venv/bin/legalize-ch enrich-dates --repo . --siblings
   ```
   A concordat is the same act in every member canton — propagates the authoritative `date_of_decision` from LexWork cantons to LexFind-only siblings (matched by normalized title; skipped when authoritative dates conflict; writes `enactment_date_source: sibling:<CANTON>`).

## Related
- `legalize-ch enrich-domains` infers harmonized domains for laws LexFind leaves unclassified (offline; writes `global_category_inferred` + `inference_source` only).
- `legalize-ch enrich-status` marks LexFind-repealed laws (`is_active: false`) — enables the active/repealed split in the chstat reconciliation (`api/v1/stats/concordats_chstat_comparison.json`).
