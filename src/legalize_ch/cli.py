"""CLI interface for the Swiss law pipeline."""
from __future__ import annotations

import logging
import sys
from pathlib import Path

import click

from .pipeline import Pipeline


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable debug logging")
def main(verbose: bool):
    """Swiss law pipeline — fetch, transform, commit."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


@main.command()
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--limit", "-n", type=int, default=None, help="Max laws to process")
@click.option("--lang", "-l", multiple=True, default=["de", "fr", "it"], help="Languages")
@click.option("--sr", type=str, default=None, help="SR number prefix filter")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between requests")
@click.option("--latest-only", is_flag=True, help="Only fetch the latest version per law")
@click.option("--no-chronological", is_flag=True,
              help="Disable chronological sorting (commits grouped by law instead)")
@click.option("--scope", type=click.Choice(["federal", "cantonal", "all"]),
              default="federal", help="Scope: federal, cantonal, or all (default: federal)")
@click.option("--canton", "-c", multiple=True, default=None,
              help="Canton(s) to process when scope includes cantonal (default: all 26)")
def bootstrap(repo: str, limit: int | None, lang: tuple, sr: str | None, rate_limit: float,
              latest_only: bool, no_chronological: bool, scope: str, canton: tuple):
    """Full pipeline: fetch all laws and commit to git.

    By default, all revisions are sorted by date before committing so that
    the git history reflects the actual legal timeline (chronological order).
    Use --no-chronological to revert to the old behavior (grouped by law).

    Use --scope to control what is fetched:
      --scope federal   (default) Only federal laws from Fedlex
      --scope cantonal  Only cantonal laws from LexWork/LexFind
      --scope all       Both federal and cantonal laws
    """
    total = 0

    if scope in ("federal", "all"):
        pipeline = Pipeline(repo_path=repo, rate_limit=rate_limit)
        federal_total = pipeline.run(limit=limit, languages=list(lang), sr_filter=sr,
                                     latest_only=latest_only,
                                     chronological=not no_chronological)
        total += federal_total
        click.echo(f"Federal: {federal_total} commits created.")

    if scope in ("cantonal", "all"):
        from .cantonal_pipeline import CantonalPipeline
        cantons_list = list(canton) if canton else None
        cantonal_pipe = CantonalPipeline(repo_path=repo, rate_limit=rate_limit)
        cantonal_total = cantonal_pipe.run(
            cantons=cantons_list, languages=list(lang), limit=limit,
        )
        total += cantonal_total
        click.echo(f"Cantonal: {cantonal_total} commits created.")

    click.echo(f"Done. {total} total commits created.")


@main.command()
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--limit", "-n", type=int, default=None, help="Max laws to process")
@click.option("--lang", "-l", multiple=True, default=["de", "fr", "it"], help="Languages")
@click.option("--sr", type=str, default=None, help="SR number prefix filter")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between requests")
@click.option("--since", type=click.DateTime(formats=["%Y-%m-%d"]), default=None,
              help="Override last_run: only fetch versions since this date (YYYY-MM-DD)")
@click.option("--no-chronological", is_flag=True,
              help="Disable chronological sorting of commits")
@click.option("--scope", type=click.Choice(["federal", "cantonal", "all"]),
              default="federal", help="Scope: federal, cantonal, or all (default: federal)")
@click.option("--canton", "-c", multiple=True, default=None,
              help="Canton(s) to update when scope includes cantonal (default: all 26)")
def update(repo: str, limit: int | None, lang: tuple, sr: str | None, rate_limit: float,
           since, no_chronological: bool, scope: str, canton: tuple):
    """Incremental update: only fetch laws with new consolidation versions.

    Detects new versions by comparing Fedlex consolidation dates against
    the pipeline state. Only versions with dateApplicability >= since are
    fetched, and already-processed versions are skipped automatically.

    By default uses last_run from pipeline state. Use --since to override.
    Commits are sorted chronologically by default.

    Use --scope to control what is updated:
      --scope federal   (default) Only federal laws from Fedlex
      --scope cantonal  Only cantonal laws (re-scans catalogs, skips known)
      --scope all       Both federal and cantonal laws
    """
    total = 0

    if scope in ("federal", "all"):
        from datetime import date as date_type
        pipeline = Pipeline(repo_path=repo, rate_limit=rate_limit)
        since_date = since.date() if since else None
        federal_total = pipeline.update(limit=limit, languages=list(lang), sr_filter=sr,
                                        since_override=since_date,
                                        chronological=not no_chronological)
        total += federal_total
        click.echo(f"Federal: {federal_total} commits created.")

    if scope in ("cantonal", "all"):
        from .cantonal_pipeline import CantonalPipeline
        cantons_list = list(canton) if canton else None
        cantonal_pipe = CantonalPipeline(repo_path=repo, rate_limit=rate_limit)
        cantonal_total = cantonal_pipe.update(
            cantons=cantons_list, languages=list(lang), limit=limit,
        )
        total += cantonal_total
        click.echo(f"Cantonal: {cantonal_total} commits created.")

    click.echo(f"Done. {total} total commits created.")


@main.command()
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--limit", "-n", type=int, default=None, help="Max laws to fetch")
def catalog(repo: str, limit: int | None):
    """Fetch and display the law catalog."""
    from .fetcher import FedlexFetcher
    fetcher = FedlexFetcher()
    entries = fetcher.fetch_catalog(limit=limit)
    for e in entries:
        title = e.title_de or e.title_fr or e.title_it or "(no title)"
        click.echo(f"SR {e.sr_number:>12s}  {title[:80]}")
    click.echo(f"\nTotal: {len(entries)} laws")


@main.command("cantonal")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", type=str, required=True, help="Canton abbreviation (e.g. bs, zh)")
@click.option("--number", "-n", type=str, default=None, help="Specific systematic number")
@click.option("--lang", "-l", default="de", help="Language (de/fr/it)")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between requests")
@click.option("--all-versions", is_flag=True, help="Fetch all versions (not just current)")
def cantonal(repo: str, canton: str, number: str | None, lang: str, rate_limit: float,
             all_versions: bool):
    """Fetch cantonal law: LexWork direct + LexFind fallback.

    Uses the LexWork JSON API for 14 cantons with direct portal access,
    falls back to LexFind for the remaining 12 cantons.
    """
    from pathlib import Path
    from .cantonal import (
        CantonalFetcher, LEXWORK_CANTONS, ALL_CANTONS,
        canton_to_path, cantonal_law_to_markdown,
    )
    from .committer import GitCommitter

    canton = canton.lower()
    if canton not in ALL_CANTONS:
        click.echo(f"Unknown canton: {canton}. Valid: {', '.join(ALL_CANTONS)}", err=True)
        raise SystemExit(1)

    fetcher = CantonalFetcher(rate_limit=rate_limit)
    committer = GitCommitter(repo)
    repo_path = Path(repo)
    commits = 0

    if number:
        # Fetch a specific law
        text = fetcher.fetch_law_text(canton, number, lang)
        if not text:
            click.echo(f"No text found for {canton.upper()} {number}")
            raise SystemExit(1)

        md = cantonal_law_to_markdown(text)
        rel_path = canton_to_path(canton, number, lang)
        abs_path = repo_path / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(md, encoding="utf-8")
        click.echo(f"Written: {rel_path}")

        if all_versions:
            versions = fetcher.fetch_versions(canton, number)
            for v in versions:
                vtext = fetcher.fetch_version_text(canton, number, v.version_id, lang)
                if vtext:
                    vmd = cantonal_law_to_markdown(vtext)
                    abs_path.write_text(vmd, encoding="utf-8")
                    click.echo(f"  Version {v.version_id}: {v.date_in_force or '?'}")
                    commits += 1
    else:
        # Fetch catalog and process all laws
        click.echo(f"Fetching catalog for {canton.upper()}...")
        click.echo(f"  Source: LexFind (systematics)")

        catalog = fetcher.fetch_catalog(canton, lang)
        if not catalog:
            click.echo("No laws found in catalog. Try --number for specific law.")
            raise SystemExit(1)

        click.echo(f"  Found {len(catalog)} laws")
        for i, entry in enumerate(catalog):
            text = fetcher.fetch_law_text(canton, entry.systematic_number, lang,
                                          lexfind_id=entry.lexfind_id)
            if text:
                md = cantonal_law_to_markdown(text, entry=entry)
                rel_path = canton_to_path(canton, entry.systematic_number, lang)
                abs_path = repo_path / rel_path
                abs_path.parent.mkdir(parents=True, exist_ok=True)
                abs_path.write_text(md, encoding="utf-8")
                commits += 1
            if (i + 1) % 10 == 0:
                click.echo(f"  [{i+1}/{len(catalog)}] processed...")

    click.echo(f"Done. {commits} laws written.")


@main.command("cantonal-list")
@click.option("--canton", "-c", type=str, default=None, help="Specific canton")
def cantonal_list(canton: str | None):
    """List cantons and their data source (LexWork/LexFind)."""
    from .cantonal import LEXWORK_CANTONS, LEXFIND_ONLY_CANTONS

    click.echo("LexWork (direct API):")
    for c in sorted(LEXWORK_CANTONS.keys()):
        if canton and c != canton.lower():
            continue
        click.echo(f"  {c.upper():3s}  https://{LEXWORK_CANTONS[c]}/api/texts_of_law/")
    click.echo(f"\nLexFind (fallback):")
    for c in sorted(LEXFIND_ONLY_CANTONS):
        if canton and c != canton.lower():
            continue
        click.echo(f"  {c.upper():3s}  https://www.lexfind.ch/")
    click.echo(f"\nTotal: {len(LEXWORK_CANTONS)} LexWork + {len(LEXFIND_ONLY_CANTONS)} LexFind = 26 cantons")


@main.command("cantonal-rollout")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--batch-size", "-b", type=int, default=3,
              help="Number of cantons to process per batch (default: 3)")
@click.option("--limit", "-n", type=int, default=None,
              help="Max laws per canton (None = all)")
@click.option("--lang", "-l", multiple=True, default=["de"], help="Languages to fetch")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between requests")
@click.option("--dry-run", is_flag=True, help="Show what would be done without fetching")
@click.option("--status", "show_status", is_flag=True, help="Show rollout progress and exit")
@click.option("--reset", type=str, default=None,
              help="Reset a failed canton to pending (canton abbreviation)")
def cantonal_rollout(repo: str, batch_size: int, limit: int | None, lang: tuple,
                     rate_limit: float, dry_run: bool, show_status: bool, reset: str | None):
    """Incrementally roll out cantonal law fetching, prioritized by data availability.

    Cantons are processed in priority tiers:
      Tier 1: Dedicated API (ZH) — best data quality
      Tier 2: LexWork API (14 cantons) — direct JSON access
      Tier 3: LexFind fallback (11 cantons) — less structured

    Each invocation processes the next --batch-size cantons. State is persisted
    between runs, so you can call this repeatedly (e.g. via cron) to gradually
    roll out all cantons.

    Examples:
      legalize-ch cantonal-rollout --status           # Check progress
      legalize-ch cantonal-rollout --batch-size 5     # Process next 5
      legalize-ch cantonal-rollout --dry-run          # Preview next batch
      legalize-ch cantonal-rollout --reset ge         # Retry failed canton
    """
    from .canton_rollout import (
        load_rollout_state, save_rollout_state, run_rollout,
        reset_canton, get_tier, tier_label, ROLLOUT_ORDER,
    )

    if reset:
        reset_canton(repo, reset.lower())
        click.echo(f"Reset {reset.upper()} to pending.")
        return

    if show_status:
        state = load_rollout_state(repo)
        summary = state.summary()
        click.echo(f"Canton Rollout Progress: {summary['completed']}/{summary['total_cantons']} "
                   f"({summary['progress_pct']}%)")
        click.echo(f"  Total laws fetched: {summary['total_laws_fetched']}")
        click.echo(f"\n  Completed ({summary['completed']}): "
                   f"{', '.join(c.upper() for c in summary['completed_list']) or 'none'}")
        if summary['in_progress_list']:
            click.echo(f"  In progress: {', '.join(c.upper() for c in summary['in_progress_list'])}")
        if summary['failed_list']:
            click.echo(f"  Failed: {', '.join(c.upper() for c in summary['failed_list'])}")
        if summary['next_up']:
            click.echo(f"  Next up: {', '.join(c.upper() for c in summary['next_up'])}")

        click.echo(f"\nPriority order ({len(ROLLOUT_ORDER)} cantons):")
        for canton in ROLLOUT_ORDER:
            tier = get_tier(canton)
            status = state.get_status(canton)
            marker = {"completed": "[x]", "in_progress": "[~]", "failed": "[!]"}.get(status, "[ ]")
            click.echo(f"  {marker} {canton.upper():3s}  Tier {tier} ({tier_label(tier)}) — {status}")
        return

    result = run_rollout(
        repo_path=repo,
        batch_size=batch_size,
        limit_per_canton=limit,
        languages=list(lang),
        rate_limit=rate_limit,
        dry_run=dry_run,
    )

    if dry_run:
        click.echo("Dry run — next batch would be:")
        for canton, info in result.get("results", {}).items():
            click.echo(f"  {canton.upper():3s}  Tier {info['tier']} ({info['tier_label']}) "
                       f"[currently: {info['status']}]")
        return

    if result.get("status") == "all_complete":
        click.echo("All 26 cantons have been rolled out!")
        return

    click.echo(f"Batch complete: {', '.join(c.upper() for c in result['batch'])}")
    click.echo(f"Total commits this batch: {result['total_commits']}")
    for canton, info in result.get("results", {}).items():
        status = info["status"]
        if status == "completed":
            click.echo(f"  {canton.upper()}: {info['commits']} commits")
        else:
            click.echo(f"  {canton.upper()}: FAILED — {info.get('error', 'unknown')}")

    summary = result.get("summary", {})
    if summary:
        click.echo(f"\nOverall: {summary['completed']}/{summary['total_cantons']} cantons "
                   f"({summary['progress_pct']}%)")


@main.command("codify")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--lang", "-l", default="de", help="Source language (default: de)")
@click.option("--sr", type=str, default=None, help="SR number prefix filter")
@click.option("--limit", "-n", type=int, default=None, help="Max law groups to process")
@click.option("--dry-run", is_flag=True, help="Only log, don't generate")
def codify(repo: str, lang: str, sr: str | None, limit: int | None, dry_run: bool):
    """Convert law texts to executable OpenFisca code using Claude CLI.

    Reads articles from ch/{number}/{lang}/*.md, generates OpenFisca
    Variable classes, and writes to ch/{number}/executable/*.py.
    """
    from .law_to_openfisca import run_pipeline

    count = run_pipeline(
        repo_path=repo,
        lang=lang,
        sr_filter=sr,
        limit=limit,
        dry_run=dry_run,
    )
    click.echo(f"Done. {count} OpenFisca variables generated.")


@main.command("translate")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--sr", type=str, default=None, help="Specific SR number to translate")
@click.option("--source-lang", "-s", default="de", help="Source language (default: de)")
@click.option("--limit", "-n", type=int, default=None, help="Max files to translate")
@click.option("--sr-filter", type=str, default=None, help="SR number prefix filter")
@click.option("--model", default="claude-sonnet-4-20250514", help="Claude model for translation")
@click.option("--api-key", envvar="ANTHROPIC_API_KEY", default=None,
              help="Anthropic API key (or set ANTHROPIC_API_KEY)")
def translate(repo: str, sr: str | None, source_lang: str, limit: int | None,
              sr_filter: str | None, model: str, api_key: str | None):
    """Translate law texts to English using the Anthropic API.

    Translates Swiss law texts from the source language (default: German)
    to English. Translated files are written to ch/{number}/en/{sr}.md.

    Uses Claude for high-quality legal translation that preserves
    structure and terminology.
    """
    from .translator import Translator

    if not api_key:
        click.echo("Error: ANTHROPIC_API_KEY not set. Provide via --api-key or env var.", err=True)
        raise SystemExit(1)

    translator = Translator(api_key=api_key, model=model)

    if sr:
        # Translate a single law
        ok = translator.translate_sr(repo, sr, source_lang)
        if ok:
            click.echo(f"Translated SR {sr} to English.")
        else:
            click.echo(f"Failed to translate SR {sr}.", err=True)
            raise SystemExit(1)
    else:
        # Batch translation
        count = translator.translate_directory(
            repo, sr_filter=sr_filter, source_lang=source_lang, limit=limit
        )
        click.echo(f"Done. {count} files translated to English.")


@main.command("index")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--site-repo", default=None, envvar="SWISS_LAW_SITE_REPO",
              help="Path to the site repo for laws.json output (default: ../swiss-law-as-source)")
@click.option("--lang", "-l", default="de", help="Language for titles (default: de)")
@click.option("--json/--no-json", "write_json", default=True,
              help="Also write laws.json for the site (default: yes)")
def index(repo: str, site_repo: str | None, lang: str, write_json: bool):
    """Generate INDEX.md and laws.json (federal + cantonal)."""
    from .index_generator import write_index, generate_laws_json

    out = write_index(repo_path=repo, lang=lang)
    click.echo(f"Generated: {out}")
    if write_json:
        from pathlib import Path
        import json
        repo_path = Path(repo).resolve()
        site_path = Path(site_repo).resolve() if site_repo else (repo_path.parent / "swiss-law-as-source")
        if not site_path.exists():
            site_path = repo_path / "docs"
        laws = generate_laws_json(repo_path=repo, lang=lang)
        out_path = site_path / "laws.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(laws, ensure_ascii=False), encoding="utf-8")
        click.echo(f"Generated: {out_path} ({len(laws)} entries)")


@main.command("health-check")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--days", "-d", type=int, default=30,
              help="Alert if no commits for this many days (default: 30)")
@click.option("--always-notify", is_flag=True,
              help="Send notification even when healthy")
def health_check(repo: str, days: int, always_notify: bool):
    """Check repo health and alert if no new commits for N days.

    Sends a Telegram notification if the most recent commit is older
    than --days (default 30). Use --always-notify to send a message
    regardless of health status.
    """
    from .health_check import check_health, send_health_alert

    is_healthy, message = check_health(repo, stale_days=days)
    click.echo(message)

    if not is_healthy or always_notify:
        ok = send_health_alert(
            repo_path=repo,
            stale_days=days,
            always_notify=always_notify,
        )
        if ok:
            click.echo("Telegram alert sent.")
        else:
            click.echo("Failed to send Telegram alert.", err=True)
            if not is_healthy:
                raise SystemExit(1)
    else:
        click.echo("No alert needed.")


@main.command("stats")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--site-repo", default=None, envvar="SWISS_LAW_SITE_REPO",
              help="Path to the site repo for stats/API output (default: ../swiss-law-as-source)")
@click.option("--no-trees", is_flag=True, help="Skip fetching category trees from LexFind API")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between API requests")
def stats(repo: str, site_repo: str | None, no_trees: bool, rate_limit: float):
    """Generate statistics, tags, and category trees.

    Writes tagging data (tags.json, trees/) to the law repo (--repo).
    Writes website data (stats.json, API, publications) to the site repo (--site-repo).
    """
    from pathlib import Path
    from .stats import (
        collect_all_frontmatter, generate_stats, generate_tags,
        generate_publications, write_publications,
        generate_yearly_canton_stats, write_yearly_canton_stats,
        generate_concordats_by_domain,
        write_stats_json, write_tags_json, fetch_and_write_trees,
    )

    repo_path = Path(repo).resolve()
    site_path = Path(site_repo).resolve() if site_repo else (repo_path.parent / "swiss-law-as-source")

    if not site_path.exists():
        click.echo(f"Site repo not found at {site_path} — falling back to {repo_path / 'docs'}", err=True)
        site_path = repo_path / "docs"

    click.echo(f"Law repo:  {repo_path}")
    click.echo(f"Site repo: {site_path}")

    click.echo("Scanning frontmatter...")
    entries = collect_all_frontmatter(repo_path)
    click.echo(f"  {len(entries)} law files found")

    click.echo("Generating stats...")
    s = generate_stats(repo_path)

    click.echo("Generating harmonized categories (federal + cantonal)...")
    from .stats import generate_harmonized_categories
    harm = generate_harmonized_categories(entries, repo_path)
    write_stats_json(harm, site_path / "api" / "v1" / "stats" / "harmonized_categories.json")
    s["by_harmonized_domain"] = {
        f"{n['identifier']} {n['title'].get('de', '')}".strip(): {
            "total": n["total"], "federal": n["federal"], "cantonal": n["cantonal"]}
        for n in harm["top_level"]
    }
    click.echo(f"  {len(harm['top_level'])} top-level domains, "
               f"federal mapped: {harm['counts']['federal_lexfind']} lexfind "
               f"+ {harm['counts']['federal_fallback']} fallback")

    click.echo("Generating harmonized-by-year cube...")
    from .stats import generate_harmonized_by_year
    harm_by_year = generate_harmonized_by_year(entries, repo_path)
    write_stats_json(harm_by_year,
                     site_path / "api" / "v1" / "stats" / "harmonized_by_year.json")
    click.echo(f"  {len(harm_by_year['years'])} year buckets")

    write_stats_json(s, site_path / "stats.json")
    click.echo(f"  stats.json: {s['total_laws']} laws ({s['federal_laws']} federal, {s['cantonal_laws']} cantonal)")

    click.echo("Generating tags...")
    tags = generate_tags(entries)
    write_tags_json(tags, repo_path / "docs" / "tags.json")
    click.echo(f"  tags.json: {tags['total']} entries")

    click.echo("Generating publications by year...")
    pubs = generate_publications(entries)
    write_publications(pubs, site_path / "api" / "v1" / "publications")
    click.echo(f"  {len(pubs)} year files written")

    click.echo("Generating per-year per-canton stats...")
    yc_stats = generate_yearly_canton_stats(entries, repo_path / "docs" / "trees")
    write_yearly_canton_stats(yc_stats, site_path / "api" / "v1" / "stats")
    click.echo(f"  {sum(len(e) for e in yc_stats.values())} files across {len(yc_stats)} years")

    click.echo("Generating concordats-by-domain table...")
    conc = generate_concordats_by_domain(entries)
    write_stats_json(conc, site_path / "api" / "v1" / "stats" / "concordats_by_domain.json")
    click.echo(f"  {conc['total_concordats']} concordats across {len(conc['cantons'])} cantons")

    click.echo("Generating signatory-weighted concordats table (the computed statistic)...")
    from .stats import generate_concordats_by_domain_signatories
    conc_sig = generate_concordats_by_domain_signatories(entries)
    write_stats_json(conc_sig, site_path / "api" / "v1" / "stats"
                     / "concordats_by_domain_signatories.json")
    click.echo(f"  {conc_sig['total_memberships']} memberships across "
               f"{conc_sig['total_agreements']} agreements; "
               f"<=2003: {conc_sig['memberships_until_2003']} "
               f"(chstat reference: {conc_sig['chstat_2003_reference']}; "
               f"+{conc_sig['memberships_added_by_title_evidence']} from title evidence)")

    click.echo("Generating per-type domain tables...")
    from .stats import generate_types_by_domain
    type_tables = generate_types_by_domain(entries, concordat_override={
        "total": conc_sig["total_memberships"],
        "path": "api/v1/stats/concordats_by_domain_signatories.json",
    })
    for slug, tbl in type_tables["files"].items():
        write_stats_json(tbl, site_path / "api" / "v1" / "stats" / "types"
                         / f"{slug}_by_domain.json")
    write_stats_json(type_tables["index"],
                     site_path / "api" / "v1" / "stats" / "types" / "index.json")
    click.echo(f"  {len(type_tables['files'])} instrument types written")

    click.echo("Generating concordat signatories...")
    from .stats import generate_concordat_signatories
    sig = generate_concordat_signatories(entries)
    write_stats_json(sig, site_path / "api" / "v1" / "stats" / "concordats_signatories.json")
    click.echo(f"  {sig['total_agreements']} distinct agreements")

    click.echo("Generating concordat size distribution (BADAC G1 baseline)...")
    from .stats import generate_concordat_size_distribution
    dist = generate_concordat_size_distribution(entries)
    write_stats_json(dist, site_path / "api" / "v1" / "stats"
                     / "concordats_size_distribution.json")
    click.echo(f"  {dist['ours']['concordats']} concordats / "
               f"{dist['ours']['memberships']} memberships "
               f"(baseline {dist['baseline']['total_concordats']} / "
               f"{dist['baseline']['total_memberships']})")

    click.echo("Generating undated-laws review list...")
    from .stats import generate_undated_laws
    und = generate_undated_laws(entries)
    write_stats_json(und, site_path / "api" / "v1" / "quality" / "undated_laws.json")
    click.echo(f"  {und['total']} undated laws ({und['by_reason']})")

    click.echo("Generating CSV + SDMX data exports...")
    from .data_exports import generate_csv_exports, write_csv_exports
    from .sdmx import generate_sdmx_files, write_sdmx_files
    csv_files = generate_csv_exports(type_tables, conc_sig, und)
    write_csv_exports(csv_files, site_path / "api" / "v1" / "csv")
    sdmx_files = generate_sdmx_files(type_tables, conc_sig)
    write_sdmx_files(sdmx_files, site_path / "api" / "sdmx")
    click.echo(f"  {len(csv_files)} CSV files, {len(sdmx_files)} SDMX artefacts")

    click.echo("Generating chstat-2003 verification comparison...")
    from .stats import (generate_chstat_comparison,
                        generate_concordat_membership_evidence)
    comparison = generate_chstat_comparison(entries, repo_path)
    write_stats_json(comparison, site_path / "api" / "v1" / "stats" / "concordats_chstat_comparison.json")
    evidence = generate_concordat_membership_evidence(entries, repo_path)
    write_stats_json(evidence, site_path / "api" / "v1" / "quality"
                     / "concordat_membership_evidence.json")
    click.echo(f"  published<=2003: {comparison['ours_enacted_until_2003_total']}"
               f" + accession {comparison['accession_evidence_total']}"
               f" + intlex-named {comparison['intlex_named_evidence_total']}"
               f" = {comparison['explained_total']}"
               f" vs chstat {comparison['chstat_total']}"
               f" (unexplained: {comparison['unexplained_total']})")

    click.echo("Generating per-entity law index...")
    from .law_index import generate_law_index, write_law_index
    law_idx = generate_law_index(entries)
    write_law_index(law_idx, site_path / "api" / "v1" / "laws")
    click.echo(f"  {sum(v['laws'] for v in law_idx.values())} laws across {len(law_idx)} entities")

    click.echo("Generating unclassified-types review list...")
    from .stats import generate_unclassified_types
    unc = generate_unclassified_types(entries)
    write_stats_json(unc, site_path / "api" / "v1" / "quality" / "unclassified_types.json")
    click.echo(f"  {unc['total']} 'Other' laws: {unc['classified']} rule-classified, "
               f"{unc['residual']} residual")

    click.echo("Generating categories API...")
    from .categories import generate_categories_api
    generate_categories_api(repo_path / "docs" / "trees",
                            site_path / "api" / "v1" / "categories")
    click.echo("  api/v1/categories/ written")

    # Ship the public reproduction script alongside the data it reproduces —
    # copied, never edited in place on the site, so the download can never
    # drift from the version in this repo.
    repro = repo_path / "scripts" / "reproduce_concordats.py"
    if repro.exists():
        (site_path / "reproduce_concordats.py").write_bytes(repro.read_bytes())
        click.echo("  reproduce_concordats.py synced to the site")

    if not no_trees:
        click.echo("Fetching category trees from LexFind...")
        fetch_and_write_trees(repo_path / "docs" / "trees", rate_limit=rate_limit)
        click.echo("  Trees written to docs/trees/")

    click.echo("Done.")


@main.command("enrich-categories")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", default=None,
              help="Canton code(s), comma-separated (default: all missing)")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between LexFind API requests")
@click.option("--dry-run", is_flag=True, help="Report what would change without modifying files")
def enrich_categories(repo: str, canton: str | None, rate_limit: float, dry_run: bool):
    """Back-fill category metadata from LexFind into cantonal law files.

    For each canton, fetches the LexFind catalog (which includes category_type,
    systematic_category, global_category) and injects those fields into the
    YAML frontmatter of existing .md files.  Laws not found in LexFind get
    category_type inferred from their title.
    """
    from pathlib import Path
    from .category_enricher import enrich_all

    repo_path = Path(repo).resolve()
    cantons = [c.strip().lower() for c in canton.split(",")] if canton else None

    if dry_run:
        click.echo("DRY RUN — no files will be modified")

    results = enrich_all(repo_path, cantons=cantons, rate_limit=rate_limit, dry_run=dry_run)

    click.echo("")
    click.echo(f"{'Canton':<8} {'Total':>6} {'LexFind':>8} {'Title':>8} {'Already':>8} {'Skip':>6}")
    click.echo("-" * 50)
    for r in results:
        if r.get("error"):
            click.echo(f"{r['canton']:<8} ERROR")
            continue
        click.echo(
            f"{r['canton']:<8} {r['total_files']:>6} {r['lexfind_matched']:>8} "
            f"{r['title_classified']:>8} {r['already_enriched']:>8} {r['skipped']:>6}"
        )
    total_matched = sum(r.get("lexfind_matched", 0) for r in results)
    total_classified = sum(r.get("title_classified", 0) for r in results)
    click.echo("-" * 50)
    click.echo(f"{'TOTAL':<8} {'':>6} {total_matched:>8} {total_classified:>8}")
    click.echo("Done.")


@main.command("backfill-lexfind")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", multiple=True, default=None,
              help="Canton code(s) (default: 14 LexWork cantons + ZH)")
@click.option("--limit", "-n", type=int, default=None,
              help="Max missing laws to fetch per canton per language")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between API requests")
@click.option("--dry-run", is_flag=True, help="Report gaps only, write nothing")
@click.option("--no-commit", is_flag=True, help="Write files but skip git commit")
def backfill_lexfind(repo: str, canton: tuple, limit: int | None,
                     rate_limit: float, dry_run: bool, no_commit: bool):
    """Import laws present in LexFind's catalog but missing locally (add-only).

    LexWork collections and ZH's capped catalog lack whole sections (notably
    intercantonal concordats) that LexFind covers.  Existing files are never
    overwritten; re-running resumes where an interrupted run stopped.
    Category metadata comes from the catalog, so enrich-categories is not
    needed for backfilled files.
    """
    from pathlib import Path
    from .lexfind_backfill import run_backfill

    repo_path = Path(repo).resolve()
    cantons = [c.strip().lower() for c in canton] if canton else None

    if dry_run:
        click.echo("DRY RUN — no files will be written")

    summaries = run_backfill(
        repo_path, cantons=cantons, rate_limit=rate_limit,
        limit=limit, dry_run=dry_run, commit=not no_commit,
    )

    click.echo("")
    click.echo(f"{'Canton':<8} {'Catalog':>8} {'Present':>8} {'Missing':>8} {'Fetched':>8} {'Failed':>7}")
    click.echo("-" * 52)
    for s in summaries:
        click.echo(
            f"{s['canton'].upper():<8} {s['catalog']:>8} {s['present']:>8} "
            f"{s['missing']:>8} {s['fetched']:>8} {s['failed']:>7}"
        )
    click.echo("-" * 52)
    click.echo(
        f"{'TOTAL':<8} {sum(s['catalog'] for s in summaries):>8} "
        f"{sum(s['present'] for s in summaries):>8} "
        f"{sum(s['missing'] for s in summaries):>8} "
        f"{sum(s['fetched'] for s in summaries):>8} "
        f"{sum(max(s['failed'], 0) for s in summaries):>7}"
    )
    if not dry_run:
        click.echo("")
        click.echo("Next: .venv/bin/legalize-ch stats --repo . --site-repo ../swiss-law-as-source --no-trees")
        click.echo("      .venv/bin/legalize-ch index --repo . --site-repo ../swiss-law-as-source")
        click.echo("      then publish via /publish-site")


@main.command("enrich-dates")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", multiple=True, default=None,
              help="Canton code(s) for the LexWork pass (default: all LexWork cantons)")
@click.option("--lexwork-versions", is_flag=True,
              help="Run the LexWork API pass (authoritative enactment + full version "
                   "dates; ~5-6h for all cantons — run detached). Default: cheap local pass.")
@click.option("--siblings", is_flag=True,
              help="Propagate authoritative concordat dates between member cantons "
                   "(run AFTER the LexWork pass; local, seconds).")
@click.option("--lexfind-families", is_flag=True,
              help="LexFind frontend API pass: family (original) dates + version "
                   "histories for ALL 26 cantons — the highest provenance tier.")
@click.option("--repeals", is_flag=True,
              help="LexFind frontend API pass dating the REPEALS: for laws marked "
                   "is_active: false, write repealed_date (the last version's "
                   "inactive date). Combine with --concordats-only.")
@click.option("--concordats-only", is_flag=True,
              help="Restrict the API pass to concordats (minutes instead of hours)")
@click.option("--rate-limit", type=float, default=0.1,
              help="Seconds between API requests (hosts declare no limits; 429 backoff governs)")
@click.option("--limit", "-n", type=int, default=None, help="Max laws per canton (API pass) / files (local)")
@click.option("--dry-run", is_flag=True, help="Report what would change, write nothing")
def enrich_dates(repo: str, canton: tuple, lexwork_versions: bool, siblings: bool,
                 lexfind_families: bool, repeals: bool, concordats_only: bool,
                 rate_limit: float, limit: int | None, dry_run: bool):
    """Back-fill enactment dates + version-date lists (laws are law+version).

    Local pass (default): parses the original "vom/du/del D. Month YYYY"
    from stored texts and derives federal version histories from git —
    no network. --lexwork-versions upgrades LexWork cantons + ZH from
    their APIs (date_of_decision + full version lists).
    """
    from pathlib import Path
    from .date_enricher import (enrich_dates_local, enrich_dates_lexwork,
                                propagate_concordat_dates)

    repo_path = Path(repo).resolve()
    if siblings:
        stats = propagate_concordat_dates(repo_path, dry_run=dry_run)
    elif repeals:
        from .date_enricher import enrich_repeal_dates
        cantons = [c.strip().lower() for c in canton] if canton else None
        stats = enrich_repeal_dates(repo_path, cantons=cantons,
                                    rate_limit=rate_limit, limit=limit,
                                    concordats_only=concordats_only)
    elif lexfind_families:
        from .date_enricher import enrich_dates_lexfind_families
        cantons = [c.strip().lower() for c in canton] if canton else None
        stats = enrich_dates_lexfind_families(repo_path, cantons=cantons,
                                              rate_limit=rate_limit, limit=limit,
                                              concordats_only=concordats_only)
    elif lexwork_versions:
        cantons = [c.strip().lower() for c in canton] if canton else None
        stats = enrich_dates_lexwork(repo_path, cantons=cantons,
                                     rate_limit=rate_limit, limit=limit,
                                     concordats_only=concordats_only)
    else:
        stats = enrich_dates_local(repo_path, limit=limit, dry_run=dry_run)
    for k, v in stats.items():
        click.echo(f"  {k}: {v}")
    click.echo("Done.")


@main.command("enrich-domains")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", multiple=True, default=None, help="Canton code(s)")
@click.option("--dry-run", is_flag=True, help="Report what would change, write nothing")
def enrich_domains_cmd(repo: str, canton: tuple, dry_run: bool):
    """Infer harmonized domains for laws LexFind leaves unclassified.

    Offline (uses canton trees on disk + title keywords). Writes
    global_category_inferred + inference_source only — the LexFind
    field is never touched.
    """
    from pathlib import Path
    from .domain_inference import enrich_domains

    repo_path = Path(repo).resolve()
    cantons = [c.strip().lower() for c in canton] if canton else None
    stats = enrich_domains(repo_path, cantons=cantons, dry_run=dry_run)
    for k, v in stats.items():
        click.echo(f"  {k}: {v}")
    click.echo("Done.")


@main.command("enrich-types")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", multiple=True, default=None, help="Canton code(s)")
@click.option("--dry-run", is_flag=True, help="Report what would change, write nothing")
def enrich_types_cmd(repo: str, canton: tuple, dry_run: bool):
    """Infer instrument types for laws LexFind files under 'Other'.

    Title-leading-word rules (Beschluss families, arrêtés, décrets, ...)
    mapped into LexFind's own 9-type taxonomy. Writes
    category_type_inferred + type_inference_rule only — LexFind's value
    is never touched. Review list: api/v1/quality/unclassified_types.json.
    """
    from pathlib import Path
    from .domain_inference import enrich_types

    repo_path = Path(repo).resolve()
    cantons = [c.strip().lower() for c in canton] if canton else None
    stats = enrich_types(repo_path, cantons=cantons, dry_run=dry_run)
    per_rule = stats.pop("per_rule", {})
    for k, v in stats.items():
        click.echo(f"  {k}: {v}")
    for rule, n in sorted(per_rule.items(), key=lambda kv: -kv[1]):
        click.echo(f"    rule {rule}: {n}")
    click.echo("Done.")


@main.command("enrich-status")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--canton", "-c", multiple=True, default=None, help="Canton code(s) (default: all 26)")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between API requests")
@click.option("--dry-run", is_flag=True, help="Report what would change, write nothing")
def enrich_status(repo: str, canton: tuple, rate_limit: float, dry_run: bool):
    """Mark laws LexFind lists as repealed (is_active: false in frontmatter).

    Active laws stay untouched; the flag enables active-vs-repealed splits
    in the concordat tables and the chstat reconciliation.
    """
    from pathlib import Path
    from .lexfind_backfill import enrich_status as _enrich_status

    repo_path = Path(repo).resolve()
    cantons = [c.strip().lower() for c in canton] if canton else None
    stats = _enrich_status(repo_path, cantons=cantons, rate_limit=rate_limit,
                           dry_run=dry_run)
    for k, v in stats.items():
        click.echo(f"  {k}: {v}")
    click.echo("Done.")


@main.command("coverage")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--site-repo", default=None, envvar="SWISS_LAW_SITE_REPO",
              help="Site repo — writes api/v1/coverage.json there (default: ../swiss-law-as-source)")
@click.option("--canton", "-c", multiple=True, default=None,
              help="Canton code(s) (default: all 26)")
@click.option("--no-federal", is_flag=True, help="Skip the Fedlex comparison")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between API requests")
def coverage(repo: str, site_repo: str | None, canton: tuple,
             no_federal: bool, rate_limit: float):
    """Audit collection completeness against the source catalogs.

    Compares every canton's local files with the LexFind catalog (ALL
    instrument types) and local federal SRs with the Fedlex catalog.
    Writes api/v1/coverage.json to the site repo and exits non-zero if
    anything is missing — run backfill-lexfind (cantonal) or update
    (federal) to close reported gaps.
    """
    from pathlib import Path
    from .coverage import run_coverage, write_coverage

    repo_path = Path(repo).resolve()
    site_path = Path(site_repo).resolve() if site_repo else (repo_path.parent / "swiss-law-as-source")
    cantons = [c.strip().lower() for c in canton] if canton else None

    report = run_coverage(repo_path, cantons=cantons, rate_limit=rate_limit,
                          include_federal=not no_federal)

    click.echo("")
    click.echo(f"{'Entity':<8} {'Catalog':>8} {'Present':>8} {'Missing':>8}")
    click.echo("-" * 36)
    fed = report.get("federal")
    if fed:
        click.echo(f"{'CH':<8} {str(fed.get('catalog', '?')):>8} "
                   f"{fed['present']:>8} {str(fed.get('missing', '?')):>8}")
    for code, cov in report["cantons"].items():
        click.echo(f"{code:<8} {cov['catalog']:>8} {cov['present']:>8} {cov['missing']:>8}")
    click.echo("-" * 36)
    click.echo(f"Total missing: {report['total_missing']}")

    if site_path.exists():
        write_coverage(report, site_path / "api" / "v1" / "coverage.json")
        click.echo(f"Report written to {site_path / 'api' / 'v1' / 'coverage.json'}")

    if report["total_missing"] > 0:
        click.echo("Gaps found — run backfill-lexfind (cantonal) / update (federal).", err=True)
        raise SystemExit(1)
    click.echo("Coverage complete — nothing missing.")


@main.command("seed-state")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--rate-limit", type=float, default=0.1, help="Seconds between API requests")
@click.option("--last-run", default="2026-06-15",
              help="last_run date to seed for the federal pipeline (default: last data commit)")
@click.option("--skip-cantonal", is_flag=True, help="Only seed the federal state file")
def seed_state(repo: str, rate_limit: float, last_run: str, skip_cantonal: bool):
    """Rebuild lost pipeline state files from existing law files.

    data/ is gitignored, so pipeline state does not survive a machine rebuild.
    Without it the federal update aborts ("No last_run date in state") and a
    cantonal update would treat every known law as new.  This reconstructs
    both state files without fetching any documents (cantonal seeding only
    fetches LexFind catalogs).  Idempotent — merges into existing state.
    """
    from pathlib import Path
    from .lexfind_backfill import seed_federal_state, seed_cantonal_state

    repo_path = Path(repo).resolve()

    click.echo("Seeding federal pipeline state...")
    fed = seed_federal_state(repo_path, last_run=last_run)
    click.echo(f"  {fed['added']} keys added ({fed['total']} total), last_run={fed['last_run']}")

    if not skip_cantonal:
        click.echo("Seeding cantonal pipeline state (fetching LexFind catalogs)...")
        per_canton = seed_cantonal_state(repo_path, rate_limit=rate_limit)
        for c, n in per_canton.items():
            click.echo(f"  {c.upper()}: {n} keys added")
        click.echo(f"  Total: {sum(per_canton.values())} cantonal keys added")

    click.echo("Done.")


@main.command("import-dates")
@click.argument("csv_file", type=click.Path(exists=True))
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--dry-run", is_flag=True, help="Report what would change without writing")
@click.option("--force", is_flag=True,
              help="Also overwrite laws that already have a plausible date")
def import_dates_cmd(csv_file: str, repo: str, dry_run: bool, force: bool):
    """Apply corrected enactment dates from a filled undated_laws.csv.

    Download api/v1/csv/undated_laws.csv from the site, fill the
    corrected_enactment_date (YYYY-MM-DD) and correction_note columns,
    then run this command. Corrections are written to every language
    version of the law (enactment_date_source: manual_import) and picked
    up by the next `legalize-ch stats` run.
    """
    from .date_import import import_dates
    res = import_dates(csv_file, repo, dry_run=dry_run, force=force)
    click.echo(f"{res['rows']} rows read; {res['applied']} corrections "
               f"{'would be ' if dry_run else ''}applied "
               f"({res['files']} language files)")
    if res["skipped"]:
        click.echo(f"{len(res['skipped'])} skipped:")
        for label, reason in res["skipped"][:20]:
            click.echo(f"  {label}: {reason}")
        if len(res["skipped"]) > 20:
            click.echo(f"  … and {len(res['skipped']) - 20} more")
    if res["applied"] and not dry_run:
        click.echo("Run `legalize-ch stats` to refresh the statistics.")


@main.command("export")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--format", "-f", "fmt", type=click.Choice(["all", "csv", "jsonld"]),
              default="all", help="Export format (default: all)")
@click.option("--lang", "-l", multiple=True, default=["de", "fr", "it"], help="Languages")
@click.option("--sr", type=str, default=None, help="SR number prefix filter")
def export(repo: str, fmt: str, lang: tuple, sr: str | None):
    """Export structured metadata as JSON-LD and/or CSV.

    Scans all law markdown files, extracts frontmatter metadata,
    and writes structured exports to data/laws_metadata.{csv,jsonld}.
    """
    from .exporter import write_all, write_csv, write_jsonld

    languages = list(lang)
    if fmt == "csv":
        path = write_csv(repo, languages, sr)
        click.echo(f"CSV written: {path}")
    elif fmt == "jsonld":
        path = write_jsonld(repo, languages, sr)
        click.echo(f"JSON-LD written: {path}")
    else:
        csv_path, jsonld_path = write_all(repo, languages, sr)
        click.echo(f"CSV written: {csv_path}")
        click.echo(f"JSON-LD written: {jsonld_path}")


@main.command("notify-test")
@click.option("--commits", type=int, default=0, help="Simulated commit count")
@click.option("--errors", type=int, default=0, help="Simulated error count")
def notify_test(commits: int, errors: int):
    """Send a test Telegram notification."""
    from .notify import PipelineResult, send_telegram

    result = PipelineResult(
        new_commits=commits,
        laws_checked=42,
        errors=[f"Test error #{i+1}" for i in range(errors)],
        mode="test",
    )
    ok = send_telegram(result)
    if ok:
        click.echo("Telegram notification sent.")
    else:
        click.echo("Failed to send notification — check logs.", err=True)
        raise SystemExit(1)


@main.command("feed")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--site-repo", default=None, envvar="SWISS_LAW_SITE_REPO",
              help="Path to the site repo for feed output (default: ../swiss-law-as-source)")
@click.option("--output", "-o", default=None, help="Output directory (overrides --site-repo)")
@click.option("--sr", type=str, default=None, help="SR number prefix filter")
@click.option("--lang", "-l", default=None, help="Language filter (de/fr/it/en)")
@click.option("--limit", "-n", type=int, default=50, help="Max entries per feed (default: 50)")
@click.option("--since-days", type=int, default=90,
              help="Look back this many days (default: 90)")
def feed(repo: str, site_repo: str | None, output: str | None, sr: str | None,
         lang: str | None, limit: int, since_days: int):
    """Generate RSS and Atom feeds of law changes (diffs).

    Creates feeds that allow subscribing to changes in specific laws.
    Feeds include unified diffs showing what changed in each revision.

    Filter by SR number prefix to track specific areas of law:
      legalize-ch feed --sr 210    # Track civil code changes
      legalize-ch feed --sr 311    # Track criminal code changes
      legalize-ch feed --lang de   # German changes only
    """
    from pathlib import Path
    from .rss_feed import write_feeds

    if not output:
        repo_path = Path(repo).resolve()
        site_path = Path(site_repo).resolve() if site_repo else (repo_path.parent / "swiss-law-as-source")
        if not site_path.exists():
            site_path = repo_path / "docs"
        output = str(site_path / "feeds")

    rss_path, atom_path = write_feeds(
        repo_path=repo,
        output_dir=output,
        sr_filter=sr,
        lang=lang,
        limit=limit,
        since_days=since_days,
    )
    click.echo(f"RSS feed:  {rss_path}")
    click.echo(f"Atom feed: {atom_path}")


@main.command("serve")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0)")
@click.option("--port", "-p", type=int, default=8000, help="Bind port (default: 8000)")
@click.option("--reload", "do_reload", is_flag=True, help="Enable auto-reload for development")
def serve(repo: str, host: str, port: int, do_reload: bool):
    """Start the REST API server for querying law texts.

    Provides endpoints:
      GET /api/v1/laws/{sr_number}?lang=de&date=YYYY-MM-DD
      GET /api/v1/laws/{sr_number}/versions?lang=de
      GET /api/v1/search?q=...&lang=de
      GET /api/v1/health
    """
    import uvicorn
    from .api import create_app

    create_app(repo_path=repo)
    uvicorn.run(
        "legalize_ch.api:app",
        host=host,
        port=port,
        reload=do_reload,
    )


@main.command("cross-level-refs")
@click.option("--repo", "-r", default=".", help="Path to the git repo")
@click.option("--site-repo", default=None, envvar="SWISS_LAW_SITE_REPO",
              help="Path to the site repo for JSON/HTML output (default: ../swiss-law-as-source)")
@click.option("--html/--no-html", "write_html", default=True,
              help="Also write HTML viewer page (default: yes)")
@click.option("--inject/--no-inject", "inject_links", default=True,
              help="Inject cross-level link sections into law markdown files (default: yes)")
def cross_level_refs(repo: str, site_repo: str | None, write_html: bool, inject_links: bool):
    """Detect and export cross-level references (federal ↔ cantonal).

    Scans cantonal law files for references to federal SR numbers and
    abbreviations, and federal files for references to cantonal laws.

    Writes cross_level_refs.json to the site repo and optionally
    cross_level_refs.html for visual exploration.

    With --inject (default), also adds cross-level reference link sections
    directly into the law markdown files.
    """
    from pathlib import Path
    from .cross_level_refs import (
        write_cross_level_json, write_cross_level_html, inject_cross_level_links,
    )

    repo_path = Path(repo).resolve()
    site_path = Path(site_repo).resolve() if site_repo else (repo_path.parent / "swiss-law-as-source")
    if not site_path.exists():
        site_path = repo_path / "docs"

    json_path = write_cross_level_json(repo_path=repo, output_dir=site_path)
    click.echo(f"Cross-level refs JSON: {json_path}")

    if write_html:
        html_path = write_cross_level_html(repo_path=repo, output_dir=site_path)
        click.echo(f"Cross-level refs HTML: {html_path}")

    if inject_links:
        counts = inject_cross_level_links(repo_path=repo)
        click.echo(
            f"Injected links: {counts['cantonal_files_updated']} cantonal, "
            f"{counts['federal_files_updated']} federal files updated"
        )


if __name__ == "__main__":
    main()
