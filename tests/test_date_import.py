"""Tests for the undated-laws correction import (legalize-ch import-dates)."""
from __future__ import annotations

from legalize_ch.date_import import import_dates


def _repo(tmp_path, enactment_line=""):
    d = tmp_path / "ch" / "be" / "de"
    d.mkdir(parents=True)
    (d / "669.1.md").write_text(
        "---\n"
        "title: Konkordat X\n"
        "canton: be\n"
        "language: de\n"
        "systematic_number: '669.1'\n"
        f"{enactment_line}"
        "---\n\nBody.\n", encoding="utf-8")
    fr = tmp_path / "ch" / "be" / "fr"
    fr.mkdir(parents=True)
    (fr / "669.1.md").write_text(
        "---\n"
        "title: Concordat X\n"
        "canton: be\n"
        "language: fr\n"
        "systematic_number: '669.1'\n"
        f"{enactment_line}"
        "---\n\nCorps.\n", encoding="utf-8")
    return tmp_path


def _csv(tmp_path, date, note="AS 1970 p. 12"):
    p = tmp_path / "undated_laws.csv"
    p.write_text(
        "# comment header\n"
        "entity,id,title,category_type,languages,raw_dates,"
        "enactment_date_source,reason,link,"
        "corrected_enactment_date,correction_note\n"
        f'BE,669.1,"Konkordat X",Interkantonale Vereinbarung,de|fr,"{{}}",'
        f',implausible_date,https://x/ch/be/de/669.1.md,{date},{note}\n',
        encoding="utf-8")
    return p


class TestImportDates:
    def test_applies_to_all_language_files(self, tmp_path):
        repo = _repo(tmp_path)
        res = import_dates(_csv(tmp_path, "1970-05-01"), repo)
        assert res["applied"] == 1 and res["files"] == 2
        for lang in ("de", "fr"):
            text = (repo / "ch" / "be" / lang / "669.1.md").read_text()
            assert "enactment_date: '1970-05-01'" in text
            assert "enactment_date_source: manual_import" in text
            assert "AS 1970 p. 12" in text

    def test_dry_run_writes_nothing(self, tmp_path):
        repo = _repo(tmp_path)
        res = import_dates(_csv(tmp_path, "1970-05-01"), repo, dry_run=True)
        assert res["applied"] == 1 and res["dry_run"]
        assert "manual_import" not in (repo / "ch" / "be" / "de" / "669.1.md").read_text()

    def test_rejects_implausible_and_malformed(self, tmp_path):
        repo = _repo(tmp_path)
        for bad in ("1970", "05.01.1970", "1000-01-01", "2150-01-01"):
            res = import_dates(_csv(tmp_path, bad), repo)
            assert res["applied"] == 0
            assert res["skipped"], bad

    def test_never_overwrites_dated_law_without_force(self, tmp_path):
        repo = _repo(tmp_path, enactment_line="enactment_date: '1960-01-01'\n")
        res = import_dates(_csv(tmp_path, "1970-05-01"), repo)
        assert res["applied"] == 0
        assert any("already dated" in r for _, r in res["skipped"])
        res = import_dates(_csv(tmp_path, "1970-05-01"), repo, force=True)
        assert res["applied"] == 1
