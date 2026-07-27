"""Tests for the LexFind backfill (add-only import + state seeding)."""
from __future__ import annotations

import json
import subprocess
from datetime import date
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from legalize_ch.cantonal import (
    CantonalLawEntry,
    CantonalLawText,
    cantonal_law_to_markdown,
)
from legalize_ch.committer import GitCommitter
from legalize_ch.lexfind_backfill import (
    DEFAULT_BACKFILL_CANTONS,
    backfill_canton,
    run_backfill,
    seed_federal_state,
)


@pytest.fixture
def tmp_repo(tmp_path):
    subprocess.run(["git", "init"], cwd=tmp_path, capture_output=True)
    subprocess.run(["git", "checkout", "-b", "main"], cwd=tmp_path, capture_output=True)
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "init"],
        cwd=tmp_path, capture_output=True,
        env={"GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "t@t.com",
             "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "t@t.com",
             "HOME": str(tmp_path), "PATH": "/usr/bin:/bin"},
    )
    (tmp_path / "data").mkdir()
    return tmp_path


def _entry(canton="gr", nr="900.1", **kw):
    defaults = dict(
        canton=canton, systematic_number=nr, title="Konkordat X",
        lexfind_id="12345", category_type="Interkantonale Vereinbarung",
        systematic_category="900 Konkordate",
        global_category="1.10 Staat",
    )
    defaults.update(kw)
    return CantonalLawEntry(**defaults)


def _text(canton="gr", nr="900.1", origin="lexfind_pdf"):
    return CantonalLawText(
        canton=canton, systematic_number=nr, title="Konkordat X",
        html_content="Konkordat X\n\nArt. 1 Zweck\nEin Text mit Inhalt.",
        language="de", version_date=date(2020, 1, 1), origin=origin,
    )


def _mock_fetcher(catalog, text=None):
    fetcher = MagicMock()
    fetcher._fetch_lexfind_catalog_by_systematics.return_value = catalog
    fetcher.fetch_law_text.return_value = text
    fetcher._fetch_from_lexfind.return_value = text
    return fetcher


def _state(repo):
    return json.loads((repo / "data" / "cantonal_pipeline_state.json").read_text())


class TestBackfillCanton:
    def test_writes_missing_law_with_metadata(self, tmp_repo):
        fetcher = _mock_fetcher([_entry(canton="so")], _text(canton="so"))
        state = {"processed": {}}
        summary = backfill_canton(
            tmp_repo, "so", fetcher, GitCommitter(tmp_repo), state)

        path = tmp_repo / "ch" / "so" / "de" / "900.1.md"
        assert path.exists()
        content = path.read_text()
        assert "source: LexFind\n" in content
        assert "category_type: Interkantonale Vereinbarung" in content
        assert "global_category: 1.10 Staat" in content
        assert "Ein Text mit Inhalt" in content
        assert summary["fetched"] == 1 and summary["failed"] == 0
        assert state["processed"]["so/900.1@de"] is True
        assert _state(tmp_repo)["processed"]["so/900.1@de"] is True

    def test_never_overwrites_existing_file(self, tmp_repo):
        path = tmp_repo / "ch" / "so" / "de" / "900.1.md"
        path.parent.mkdir(parents=True)
        path.write_text("ORIGINAL LEXWORK CONTENT")

        fetcher = _mock_fetcher([_entry(canton="so")], _text(canton="so"))
        state = {"processed": {}}
        summary = backfill_canton(tmp_repo, "so", fetcher, None, state, commit=False)

        assert path.read_text() == "ORIGINAL LEXWORK CONTENT"
        assert summary["present"] == 1 and summary["fetched"] == 0
        # pre-existing file gets its state key seeded
        assert state["processed"]["so/900.1@de"] is True
        fetcher.fetch_law_text.assert_not_called()

    def test_failed_fetch_not_marked(self, tmp_repo):
        fetcher = _mock_fetcher([_entry(canton="so")], None)
        state = {"processed": {}}
        summary = backfill_canton(tmp_repo, "so", fetcher, None, state, commit=False)
        assert summary["failed"] == 1 and summary["fetched"] == 0
        assert "so/900.1@de" not in state["processed"]

    def test_limit_respected(self, tmp_repo):
        catalog = [_entry(canton="so", nr=f"900.{i}") for i in range(5)]
        fetcher = _mock_fetcher(catalog, _text(canton="so"))
        summary = backfill_canton(
            tmp_repo, "so", fetcher, None, {"processed": {}},
            limit=2, commit=False)
        assert summary["fetched"] == 2
        assert summary["missing"] == 5

    def test_dry_run_writes_nothing(self, tmp_repo):
        fetcher = _mock_fetcher([_entry(canton="so")], _text(canton="so"))
        summary = backfill_canton(
            tmp_repo, "so", fetcher, None, {"processed": {}}, dry_run=True)
        assert summary["missing"] == 1
        assert not (tmp_repo / "ch").exists()
        fetcher.fetch_law_text.assert_not_called()

    def test_one_commit_per_canton(self, tmp_repo):
        catalog = [_entry(canton="so", nr="900.1"), _entry(canton="so", nr="900.2")]
        fetcher = _mock_fetcher(catalog, _text(canton="so"))
        backfill_canton(
            tmp_repo, "so", fetcher, GitCommitter(tmp_repo), {"processed": {}})
        log = subprocess.run(
            ["git", "log", "--oneline"], cwd=tmp_repo,
            capture_output=True, text=True).stdout.strip().splitlines()
        assert len(log) == 2  # init + one backfill commit
        assert "Backfill SO" in log[0]

    def test_dedicated_fetcher_cantons_bypass_to_lexfind(self, tmp_repo):
        # zh/ge/ne must fetch via LexFind PDFs — their dedicated fetchers
        # have partial catalogs and expect their own ids, not tol ids.
        for canton in ("zh", "ge", "ne"):
            fetcher = _mock_fetcher([_entry(canton=canton)], _text(canton=canton))
            backfill_canton(tmp_repo, canton, fetcher, None, {"processed": {}},
                            commit=False)
            fetcher._fetch_from_lexfind.assert_called()
            fetcher.fetch_law_text.assert_not_called()


class TestRunBackfill:
    def test_canton_failure_is_isolated(self, tmp_repo, monkeypatch):
        calls = []

        def fake_backfill(repo, canton, *a, **kw):
            calls.append(canton)
            if canton == "gr":
                raise RuntimeError("boom")
            return {"canton": canton, "langs": ["de"], "catalog": 1,
                    "present": 1, "missing": 0, "fetched": 0, "failed": 0,
                    "committed": False}

        monkeypatch.setattr(
            "legalize_ch.lexfind_backfill.backfill_canton", fake_backfill)
        monkeypatch.setattr(
            "legalize_ch.lexfind_backfill.CantonalFetcher", MagicMock())
        summaries = run_backfill(tmp_repo, cantons=["gr", "so"], commit=False)
        assert calls == ["gr", "so"]
        assert summaries[0]["failed"] == -1
        assert summaries[1]["canton"] == "so"

    def test_default_cantons_all_26(self):
        assert len(DEFAULT_BACKFILL_CANTONS) == 26
        for c in ("zh", "ge", "ne", "gr", "ai"):
            assert c in DEFAULT_BACKFILL_CANTONS


class TestOriginAttribution:
    def test_lexwork_canton_pdf_fallback_gets_lexfind_label(self):
        # The bug this fixes: GR (LexWork canton) text from the LexFind PDF
        # fallback must be labeled LexFind and use the PDF transformer.
        md = cantonal_law_to_markdown(_text(origin="lexfind_pdf"), entry=_entry())
        assert "source: LexFind\n" in md
        assert "LexFind+LexWork" not in md

    def test_lexwork_origin_keeps_lexwork_label(self):
        md = cantonal_law_to_markdown(_text(origin="lexwork"))
        assert "source: LexFind+LexWork" in md

    def test_no_origin_falls_back_to_canton_inference(self):
        md = cantonal_law_to_markdown(_text(origin=""))
        assert "source: LexFind+LexWork" in md  # gr is a LexWork canton
        md_zh = cantonal_law_to_markdown(_text(canton="zh", origin=""))
        assert "source: LexFind+ZHLex" in md_zh


class TestSeedFederalState:
    def test_seeds_from_frontmatter(self, tmp_repo):
        law_dir = tmp_repo / "ch" / "1" / "de"
        law_dir.mkdir(parents=True)
        (law_dir / "101.md").write_text(
            "---\nsr_number: '101'\ntitle: BV\nlanguage: de\n"
            "version_date: '2024-01-01'\n---\n\n# BV\n")
        result = seed_federal_state(tmp_repo, last_run="2026-06-15")
        assert result["added"] == 1
        assert result["last_run"] == "2026-06-15"
        state = json.loads((tmp_repo / "data" / "pipeline_state.json").read_text())
        assert state["processed"]["101@2024-01-01"] is True

    def test_merge_preserves_existing(self, tmp_repo):
        state_path = tmp_repo / "data" / "pipeline_state.json"
        state_path.write_text(json.dumps(
            {"processed": {"999@2020-01-01": True}, "last_run": "2026-07-01"}))
        result = seed_federal_state(tmp_repo, last_run="2026-06-15")
        state = json.loads(state_path.read_text())
        assert state["processed"]["999@2020-01-01"] is True
        assert state["last_run"] == "2026-07-01"  # existing last_run kept
        assert result["last_run"] == "2026-07-01"


class TestEnrichStatus:
    def test_marks_only_inactive(self, tmp_repo, monkeypatch):
        from legalize_ch.lexfind_backfill import enrich_status
        active = tmp_repo / "ch" / "so" / "de" / "1.1.md"
        inactive = tmp_repo / "ch" / "so" / "de" / "2.2.md"
        for p, nr in ((active, "1.1"), (inactive, "2.2")):
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(f"---\ncanton: SO\nsystematic_number: '{nr}'\n"
                         f"title: T\nlanguage: de\n---\n\n# T\n")
        fetcher = MagicMock()
        fetcher._fetch_lexfind_catalog_by_systematics.return_value = [
            _entry(canton="so", nr="1.1", is_active=True),
            _entry(canton="so", nr="2.2", is_active=False),
        ]
        monkeypatch.setattr("legalize_ch.lexfind_backfill.CantonalFetcher",
                            MagicMock(return_value=fetcher))
        stats = enrich_status(tmp_repo, cantons=["so"])
        assert stats["marked"] == 1
        assert "is_active: false" in inactive.read_text()
        assert "is_active" not in active.read_text()
        # idempotent
        stats2 = enrich_status(tmp_repo, cantons=["so"])
        assert stats2["already_marked"] == 1 and stats2["marked"] == 0
