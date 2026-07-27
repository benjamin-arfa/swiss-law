Backfill laws that exist in LexFind's catalog but are missing from the local collection (add-only — never overwrites existing files).

Background: LexWork-sourced cantons (ag ar be bl bs fr gl gr lu sg so tg vs zg) and ZH (capped zh.ch catalog, ~150 laws vs 1,343 in LexFind) are missing whole sections — notably intercantonal concordats (GR had 0 of LexFind's 52; FR 2 of 126; ZH 13 of 150). Backfilled files get their category metadata (category_type, systematic_category, global_category) straight from the LexFind catalog, so `enrich-categories` is NOT needed afterward.

If `$ARGUMENTS` contains canton codes or `--limit N`, forward them to the commands below.

## Steps

1. **Preflight — gap report (fast, writes nothing)**
   Run: `.venv/bin/legalize-ch backfill-lexfind --repo . --dry-run`
   Shows per-canton Catalog / Present / Missing counts.

2. **Launch the backfill (long-running — run detached)**
   ```
   mkdir -p data/logs
   nohup ./scripts/backfill_lexfind.sh 0.1 > data/logs/backfill_$(date +%Y%m%d).out 2>&1 &
   ```
   Expected runtime: ~3-5s per missing law (≈2 API requests at the 0.1s rate limit). GR alone ≈ 45-60 min; a full 15-canton pass ≈ 4-10 hours. One batch git commit per canton.

3. **Monitor / resume**
   `tail -f data/logs/backfill_*.out`. Safe to interrupt any time; re-running skips files that already exist and sweeps uncommitted leftovers into the next canton commit.

4. **Post-steps — automatic.** On completion the script regenerates stats + search index + law index, deploys the site repo, pushes the law repo, and sends a Telegram notification (`mode: backfill`). Pass `--no-publish` as the FIRST argument to skip this chain (then publish manually via `/publish-site`).

5. **Report summary**: per-canton fetched/failed counts, total new laws, push/deploy status from the log tail.

## Caveats
- ZH: backfilled laws come from LexFind PDFs and won't receive version updates from the capped zh.ch catalog until the ZH fetcher is extended.
- GR: LexFind serves de/it only (no Romansh).
- Pipeline state (`data/cantonal_pipeline_state.json`) is seeded for both new and pre-existing files, so weekly `update` runs stay consistent. If state files were lost (machine rebuild), run `.venv/bin/legalize-ch seed-state` first — see README "Pipeline state repair".
