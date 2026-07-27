"""Tests for enactment-date enrichment and version parsing."""
from __future__ import annotations

import subprocess
from datetime import date
from pathlib import Path

import pytest

from legalize_ch.cantonal import _parse_version_dates_str
from legalize_ch.date_enricher import (
    federal_dates_from_git,
    parse_enactment,
    update_file_dates,
)


class TestParseEnactment:
    def test_german_spelled(self):
        assert parse_enactment("", "Bundesgesetz vom 20. Dezember 1968 über X") \
            == date(1968, 12, 20)

    def test_french(self):
        assert parse_enactment("Loi du 25 juin 1980 sur les impôts", "", "fr") \
            == date(1980, 6, 25)

    def test_italian(self):
        assert parse_enactment("Legge del 3 luglio 1951", "", "it") == date(1951, 7, 3)

    def test_numeric(self):
        assert parse_enactment("Verordnung vom 01.05.2024", "") == date(2024, 5, 1)

    def test_stand_date_not_captured(self):
        assert parse_enactment("(Stand am 1. Januar 2024)\nkein Datum", "") is None

    def test_cross_language_month_fallback(self):
        # de file quoting a French date still parses via the merged tables
        assert parse_enactment("Konkordat du 9 mars 1978", "", "de") == date(1978, 3, 9)


class TestParseVersionDatesStr:
    def test_seit(self):
        assert _parse_version_dates_str("Version in Kraft seit: 01.05.2024") \
            == (date(2024, 5, 1), None)

    def test_von_bis(self):
        assert _parse_version_dates_str("Version in Kraft von: 01.05.2024 bis: 29.06.2024") \
            == (date(2024, 5, 1), date(2024, 6, 29))

    def test_vom_in_kraft_seit(self):
        assert _parse_version_dates_str("vom 25.06.1980, in Kraft seit: 01.01.1982") \
            == (date(1982, 1, 1), None)

    def test_french_depuis(self):
        assert _parse_version_dates_str("Version en vigueur depuis le: 01.01.2010") \
            == (date(2010, 1, 1), None)

    def test_empty(self):
        assert _parse_version_dates_str("") == (None, None)


def _law_file(path: Path, version_date="2015-04-26", extra=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\ncanton: GR\nsystematic_number: '1.1'\ntitle: Konkordat\n"
        f"language: de\nversion_date: '{version_date}'\n{extra}---\n\n# T\n",
        encoding="utf-8")


class TestUpdateFileDates:
    def test_fills_missing(self, tmp_path):
        p = tmp_path / "ch" / "gr" / "de" / "1.1.md"
        _law_file(p)
        assert update_file_dates(p, date(1970, 1, 1), "text",
                                 ["1970-01-01", "2015-04-26"], "lexwork_api")
        s = p.read_text()
        assert "enactment_date: '1970-01-01'" in s
        assert "enactment_date_source: text" in s
        assert "version_dates:" in s

    def test_idempotent_no_overwrite(self, tmp_path):
        p = tmp_path / "ch" / "gr" / "de" / "1.1.md"
        _law_file(p, extra="enactment_date: '1960-01-01'\nenactment_date_source: lexwork_api\n")
        assert not update_file_dates(p, date(1970, 1, 1), "text")
        assert "1960-01-01" in p.read_text()

    def test_clamp_rejects_future_enactment(self, tmp_path):
        p = tmp_path / "ch" / "gr" / "de" / "1.1.md"
        _law_file(p, version_date="2000-01-01")
        assert not update_file_dates(p, date(2020, 1, 1), "text")


class TestFederalDatesFromGit:
    def test_walk_collects_per_file_dates(self, tmp_path):
        env = {"GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "T", "GIT_COMMITTER_EMAIL": "t@t",
               "HOME": str(tmp_path), "PATH": "/usr/bin:/bin"}
        def git(*a, **kw):
            subprocess.run(["git", "-C", str(tmp_path), *a], env={**env, **kw},
                           capture_output=True, check=True)
        git("init")
        f = tmp_path / "ch" / "1" / "de" / "101.md"
        f.parent.mkdir(parents=True)
        for i, d in enumerate(("1999-01-01", "2005-06-30")):
            f.write_text(f"---\nsr_number: '101'\n---\nv{i}\n")
            git("add", "ch")
            git("commit", "-m", f"rev {i}",
                GIT_AUTHOR_DATE=f"{d}T12:00:00", GIT_COMMITTER_DATE=f"{d}T12:00:00")
        dates = federal_dates_from_git(tmp_path)
        assert dates["ch/1/de/101.md"] == ["1999-01-01", "2005-06-30"]
