"""LexFind backfill — add-only import of laws missing from local collections.

LexWork-sourced cantons (and ZH's capped zh.ch catalog) lack whole sections
that LexFind's catalog covers — notably intercantonal concordats.  This module
imports only the laws that are missing locally:

- add-only: an existing ``ch/<canton>/<lang>/<nr>.md`` is never overwritten,
  which also makes an interrupted run trivially resumable (just re-run);
- catalog metadata (category_type, systematic/global category) is written into
  the frontmatter directly, so ``enrich-categories`` is not needed afterward;
- the pipeline state file is seeded for present files too, so future
  ``update`` runs version-compare instead of treating them as new.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from .cantonal import (
    ALL_CANTONS,
    CANTON_LANGUAGES,
    DEDICATED_FETCHER_CANTONS,
    CantonalFetcher,
    canton_to_path,
    cantonal_law_to_markdown,
)
from .cantonal_pipeline import CANTONAL_STATE_FILE
from .committer import GitCommitter

logger = logging.getLogger(__name__)

# All 26 — the LexFind-only cantons no-op in minutes when already complete;
# covering everything guarantees every law type is fetched without
# canton- or type-specific special cases.
DEFAULT_BACKFILL_CANTONS = list(ALL_CANTONS)

# LexFind serves de/fr/it only (no Romansh).
_LEXFIND_LANGUAGES = ("de", "fr", "it")

_STATE_SAVE_INTERVAL = 25


def _canton_languages(canton: str) -> list[str]:
    return [l for l in CANTON_LANGUAGES.get(canton, ["de"]) if l in _LEXFIND_LANGUAGES]


def _load_cantonal_state(repo_path: Path) -> dict:
    state_file = repo_path / CANTONAL_STATE_FILE
    if state_file.exists():
        return json.loads(state_file.read_text())
    return {"processed": {}, "last_run": None}


def _save_cantonal_state(repo_path: Path, state: dict):
    state_file = repo_path / CANTONAL_STATE_FILE
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, indent=2, default=str))


def backfill_canton(
    repo_path: Path,
    canton: str,
    fetcher: CantonalFetcher,
    committer: GitCommitter | None,
    state: dict,
    limit: int | None = None,
    dry_run: bool = False,
    commit: bool = True,
) -> dict:
    """Backfill one canton from the LexFind catalog. Returns a summary dict."""
    langs = _canton_languages(canton)
    summary = {
        "canton": canton, "langs": langs, "catalog": 0,
        "present": 0, "missing": 0, "fetched": 0, "failed": 0,
        "committed": False,
    }
    processed = state.setdefault("processed", {})
    unsaved = 0

    for lang in langs:
        catalog = fetcher._fetch_lexfind_catalog_by_systematics(canton, lang)
        summary["catalog"] += len(catalog)
        attempts = 0

        for entry in catalog:
            rel = canton_to_path(canton, entry.systematic_number, lang)
            abs_path = repo_path / rel
            key = f"{canton}/{entry.systematic_number}@{lang}"

            if abs_path.exists():
                summary["present"] += 1
                # Seed state for pre-existing files so `update` runs
                # version-compare instead of treating them as new.
                if key not in processed:
                    processed[key] = True
                    unsaved += 1
                continue

            summary["missing"] += 1
            if dry_run:
                continue
            if limit is not None and attempts >= limit:
                continue
            attempts += 1

            if canton in DEDICATED_FETCHER_CANTONS:
                # zh/ge/ne: bypass the dedicated fetchers — their catalogs
                # are partial and fetch_law_text expects their own ids,
                # not the LexFind tol id the catalog provides.
                text = fetcher._fetch_from_lexfind(
                    canton, entry.systematic_number, entry.lexfind_id, lang)
            else:
                # LexWork first (better text quality), LexFind PDF fallback.
                text = fetcher.fetch_law_text(
                    canton, entry.systematic_number, lang,
                    lexfind_id=entry.lexfind_id)

            if not text or not text.html_content:
                summary["failed"] += 1
                logger.warning("No text for %s/%s (%s)",
                               canton.upper(), entry.systematic_number, lang)
                continue

            text.abbreviation = text.abbreviation or entry.abbreviation
            md = cantonal_law_to_markdown(text, entry=entry)
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            abs_path.write_text(md, encoding="utf-8")
            processed[key] = True
            summary["fetched"] += 1
            unsaved += 1
            logger.info("Backfilled %s/%s (%s): %s",
                        canton.upper(), entry.systematic_number, lang,
                        entry.title[:60])

            if unsaved >= _STATE_SAVE_INTERVAL:
                _save_cantonal_state(repo_path, state)
                unsaved = 0

    if unsaved:
        _save_cantonal_state(repo_path, state)

    if not dry_run and commit and committer is not None:
        committer._run_git("add", f"ch/{canton}")
        staged = committer._run_git("diff", "--cached", "--name-only")
        n_staged = len([l for l in staged.stdout.splitlines() if l.strip()])
        if n_staged:
            committer._run_git(
                "commit", "-m",
                f"Backfill {canton.upper()}: {n_staged} law files from LexFind",
            )
            summary["committed"] = True

    return summary


def run_backfill(
    repo_path: str | Path,
    cantons: list[str] | None = None,
    rate_limit: float = 1.5,
    limit: int | None = None,
    dry_run: bool = False,
    commit: bool = True,
) -> list[dict]:
    """Backfill missing laws from LexFind for the given cantons (add-only)."""
    repo_path = Path(repo_path)
    cantons = [c.lower() for c in (cantons or DEFAULT_BACKFILL_CANTONS)]
    fetcher = CantonalFetcher(rate_limit=rate_limit)
    committer = GitCommitter(repo_path) if commit and not dry_run else None
    state = _load_cantonal_state(repo_path)

    summaries = []
    for canton in cantons:
        logger.info("=== Backfill %s ===", canton.upper())
        try:
            summary = backfill_canton(
                repo_path, canton, fetcher, committer, state,
                limit=limit, dry_run=dry_run, commit=commit,
            )
        except Exception:
            logger.exception("Backfill failed for %s, continuing", canton.upper())
            summary = {"canton": canton, "langs": _canton_languages(canton),
                       "catalog": 0, "present": 0, "missing": 0,
                       "fetched": 0, "failed": -1, "committed": False}
        summaries.append(summary)
        logger.info(
            "%s: catalog=%d present=%d missing=%d fetched=%d failed=%d",
            canton.upper(), summary["catalog"], summary["present"],
            summary["missing"], summary["fetched"], summary["failed"],
        )
    return summaries


# ─── Pipeline-state seeding (cron repair) ──────────────────────────────────────

def seed_federal_state(repo_path: str | Path, last_run: str = "2026-06-15") -> dict:
    """Reconstruct data/pipeline_state.json from existing federal law files.

    Seeds ``processed["{sr}@{version_date}"]`` for every federal file and sets
    ``last_run`` (only if unset) so incremental federal updates work again
    after the state file was lost.  Merges into an existing state file.
    """
    from .pipeline import STATE_FILE
    from .stats import collect_all_frontmatter

    repo_path = Path(repo_path)
    state_path = repo_path / STATE_FILE
    if state_path.exists():
        state = json.loads(state_path.read_text())
    else:
        state = {"processed": {}, "last_run": None}
    processed = state.setdefault("processed", {})

    added = 0
    for e in collect_all_frontmatter(repo_path):
        if e.get("_scope") != "federal":
            continue
        sr = str(e.get("sr_number", ""))
        vd = str(e.get("version_date", ""))
        if sr and len(vd) >= 10:
            key = f"{sr}@{vd[:10]}"
            if key not in processed:
                processed[key] = True
                added += 1

    if not state.get("last_run"):
        state["last_run"] = last_run

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, default=str))
    return {"added": added, "total": len(processed), "last_run": state["last_run"]}


def seed_cantonal_state(
    repo_path: str | Path,
    cantons: list[str] | None = None,
    rate_limit: float = 1.0,
) -> dict[str, int]:
    """Seed cantonal state keys for files that already exist locally.

    Fetches each canton's LexFind catalog (metadata only, no documents) and
    marks ``{canton}/{nr}@{lang}`` processed for every entry whose .md file is
    present.  This is the same seeding the backfill does — factored out so the
    cron can be repaired without the long document fetch.
    """
    repo_path = Path(repo_path)
    cantons = [c.lower() for c in (cantons or DEFAULT_BACKFILL_CANTONS)]
    fetcher = CantonalFetcher(rate_limit=rate_limit)
    state = _load_cantonal_state(repo_path)
    processed = state.setdefault("processed", {})

    added_per_canton: dict[str, int] = {}
    for canton in cantons:
        added = 0
        for lang in _canton_languages(canton):
            catalog = fetcher._fetch_lexfind_catalog_by_systematics(canton, lang)
            for entry in catalog:
                abs_path = repo_path / canton_to_path(canton, entry.systematic_number, lang)
                key = f"{canton}/{entry.systematic_number}@{lang}"
                if abs_path.exists() and key not in processed:
                    processed[key] = True
                    added += 1
        added_per_canton[canton] = added
        logger.info("Seeded %d state keys for %s", added, canton.upper())
        _save_cantonal_state(repo_path, state)

    return added_per_canton
