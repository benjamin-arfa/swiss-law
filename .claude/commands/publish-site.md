Regenerate and publish the swiss-law-as-source website from the current law data.

This does NOT re-fetch laws from external sources — it only rebuilds stats, index, and API files from existing markdown files, then deploys to GitHub Pages.

If the user passed `--no-push` in $ARGUMENTS, skip the final push step.

## Steps

1. **Verify prerequisites**
   - Confirm we're in the swiss-law repo (check `src/legalize_ch/` exists)
   - Check the site repo exists at `../swiss-law-as-source` (or `$SWISS_LAW_SITE_REPO`)
   - Check `.venv/bin/legalize-ch` is available

2. **Regenerate statistics**
   Run: `.venv/bin/legalize-ch stats --repo . --site-repo ../swiss-law-as-source --no-trees`
   This scans all `ch/**/*.md` files and writes to the site repo:
   - `stats.json` (aggregate counts)
   - `api/v1/stats/{year}/{entity}.json` (per-year per-canton breakdowns)
   - `api/v1/publications/{year}.json` (per-year law lists)
   - `docs/tags.json` (in this repo)

3. **Regenerate search index**
   Run: `.venv/bin/legalize-ch index --repo . --site-repo ../swiss-law-as-source`
   This writes:
   - `laws.json` to site repo (frontend search index)
   - `INDEX.md` to this repo

4. **Deploy site** (skip if `--no-push` was passed)
   Run: `./scripts/deploy_site.sh "Rebuild site $(date +%Y-%m-%d)"`
   This does `git add -A && git commit && git push` in the site repo.

5. **Report summary**
   Show: files changed in site repo, new commit hash, and the GitHub Pages URL.
   If any step failed, report the error clearly.
