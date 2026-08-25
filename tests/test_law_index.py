"""Tests for the per-entity law index and article-count heuristic."""
from __future__ import annotations

import json

import pytest

from legalize_ch.law_index import (
    build_all_payload,
    generate_law_index,
    write_law_index,
)
from legalize_ch.stats import count_articles


def _entry(scope="cantonal", canton="GR", nr="900.1", lang="de",
           path=None, chars=100, articles=5, **kw):
    e = {
        "_scope": scope,
        "_path": path or (f"ch/{canton.lower()}/{lang}/{nr}.md" if scope == "cantonal"
                          else f"ch/{nr.split('.')[0]}/{lang}/{nr}.md"),
        "_body_chars": chars,
        "_body_articles": articles,
        "language": lang,
        "title": f"Law {nr} ({lang})",
        "version_date": "2020-01-01",
    }
    if scope == "cantonal":
        e["canton"] = canton
        e["systematic_number"] = nr
    else:
        e["sr_number"] = nr
    e.update(kw)
    return e


class TestCountArticles:
    def test_run_on_federal_text(self):
        body = "EinleitungArt. 1 ZweckText hierArt. 2 GeltungMehr TextArt. 2 nochmal"
        assert count_articles(body) == 2  # distinct IDs, repeat not double-counted

    def test_paragraph_markers_line_anchored(self):
        body = "§ 1 Zweck\nText\n  § 2 Geltung\nInline § 3 wird nicht gezählt? doch nur am Zeilenanfang"
        assert count_articles(body) == 2

    def test_article_premier_french(self):
        body = "Article premier But\ntexte\nArt. 2 Champ"
        assert count_articles(body) == 2

    def test_no_match(self):
        assert count_articles("Nur Metadaten, keine Artikel.") == 0

    def test_lettered_articles(self):
        assert count_articles("Art. 12a Text Art. 12b Text") == 2


class TestGenerateLawIndex:
    def test_entity_split_and_totals(self):
        entries = [
            _entry(scope="federal", nr="101", chars=50, articles=3),
            _entry(canton="GR", nr="900.1"),
            _entry(canton="BE", nr="100.1"),
        ]
        idx = generate_law_index(entries)
        assert set(idx) == {"CH", "GR", "BE"}
        assert list(idx)[0] == "CH"  # CH first
        assert idx["CH"]["laws"] == 1 and idx["CH"]["total_chars"] == 50
        assert idx["GR"]["name"] == "Graubünden"

    def test_all_languages_kept_with_metrics(self):
        entries = [
            _entry(canton="BE", nr="100.1", lang="de", chars=100, articles=4),
            _entry(canton="BE", nr="100.1", lang="fr", chars=90, articles=4),
        ]
        idx = generate_law_index(entries)
        item = idx["BE"]["items"][0]
        assert set(item["languages"]) == {"de", "fr"}
        assert item["languages"]["fr"]["chars"] == 90
        assert idx["BE"]["laws"] == 1  # deduplicated
        assert idx["BE"]["total_chars"] == 190  # both languages summed

    def test_canonical_preferred_over_legacy(self):
        entries = [
            _entry(scope="federal", nr="101", lang="de", path="ch/de/101.md", chars=10),
            _entry(scope="federal", nr="101", lang="de", path="ch/1/de/101.md", chars=20),
        ]
        idx = generate_law_index(entries)
        item = idx["CH"]["items"][0]
        assert item["languages"]["de"]["path"] == "ch/1/de/101.md"
        assert item["languages"]["de"]["chars"] == 20

    def test_link_url_encoded(self):
        entries = [_entry(canton="GE", nr="A 1 03", lang="fr",
                          path="ch/ge/fr/A 1 03.md")]
        idx = generate_law_index(entries)
        assert idx["GE"]["items"][0]["link"].endswith("ch/ge/fr/A%201%2003.md")

    def test_category_fields_carried(self):
        entries = [_entry(canton="GR", nr="900.1",
                          category_type="Interkantonale Vereinbarung",
                          global_category="1.10 Staat")]
        item = generate_law_index(entries)["GR"]["items"][0]
        assert item["category_type"] == "Interkantonale Vereinbarung"
        assert item["global_category"] == "1.10 Staat"


class TestWriteLawIndex:
    def test_writes_master_and_entity_files(self, tmp_path):
        entries = [
            _entry(scope="federal", nr="101"),
            _entry(canton="GR", nr="900.1"),
        ]
        write_law_index(generate_law_index(entries), tmp_path)
        master = json.loads((tmp_path / "index.json").read_text())
        assert master["total_laws"] == 2
        assert master["entities"]["GR"]["file"] == "api/v1/laws/GR.json"
        gr = json.loads((tmp_path / "GR.json").read_text())
        assert gr["laws"] == 1 and gr["items"][0]["id"] == "900.1"
        assert (tmp_path / "CH.json").exists()


class TestBuildAllPayload:
    def _index(self):
        return generate_law_index([
            _entry(scope="federal", nr="101", chars=300, articles=7),
            _entry(scope="federal", nr="101", lang="fr", chars=310, articles=7),
            _entry(canton="GR", nr="900.1", chars=100, articles=5),
            _entry(canton="AG", nr="110.0", chars=50, articles=2),
        ])

    def test_covers_every_entity_not_just_federal(self):
        all_p = build_all_payload(self._index())
        assert all_p["laws"] == 3
        assert {i["id"] for i in all_p["items"]} == {"CH 101", "GR 900.1", "AG 110.0"}

    def test_totals_match_the_sum_over_entities(self):
        index = self._index()
        all_p = build_all_payload(index)
        assert all_p["total_chars"] == sum(v["total_chars"] for v in index.values())
        assert all_p["total_articles"] == sum(v["total_articles"] for v in index.values())
        assert all_p["total_chars"] == 300 + 310 + 100 + 50

    def test_keeps_per_language_volumes_and_paths(self):
        items = {i["id"]: i for i in build_all_payload(self._index())["items"]}
        ch = items["CH 101"]["languages"]
        assert ch["de"] == {"chars": 300, "articles": 7, "path": "ch/101/de/101.md"}
        assert ch["fr"]["path"] == "ch/101/fr/101.md"

    def test_drops_the_bulky_per_item_fields(self):
        item = build_all_payload(self._index())["items"][0]
        assert set(item) <= {"id", "title", "languages", "enactment_date"}

    def test_written_as_a_compact_28th_file(self, tmp_path):
        write_law_index(self._index(), tmp_path)
        raw = (tmp_path / "ALL.json").read_text()
        assert "\n" not in raw          # compact: written without indent
        payload = json.loads(raw)
        assert payload["entity"] == "ALL" and payload["laws"] == 3
        master = json.loads((tmp_path / "index.json").read_text())
        assert master["all"]["file"] == "api/v1/laws/ALL.json"
        assert master["all"]["laws"] == master["total_laws"] == 3
        assert master["all"]["total_chars"] == payload["total_chars"]
