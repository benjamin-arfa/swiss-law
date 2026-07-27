"""Tests for the INDEX.md generator."""
import tempfile
from pathlib import Path

import pytest

from legalize_ch.index_generator import (
    _extract_frontmatter,
    _sr_sort_key,
    generate_index,
    generate_laws_json,
    write_index,
)


@pytest.fixture
def sample_repo(tmp_path):
    """Create a minimal repo structure with sample markdown files."""
    # Create ch/1/de/ directory
    de_dir = tmp_path / "ch" / "1" / "de"
    de_dir.mkdir(parents=True)

    # Create sample law files
    (de_dir / "1.001.md").write_text(
        "---\n"
        "language: de\n"
        "source: https://fedlex.data.admin.ch\n"
        "sr_number: 1.001\n"
        "title: Bundesverfassung Test\n"
        "version_date: '2024-01-01'\n"
        "---\n\n# Test content\n",
        encoding="utf-8",
    )
    (de_dir / "1.002.md").write_text(
        "---\n"
        "language: de\n"
        "source: https://fedlex.data.admin.ch\n"
        "sr_number: 1.002\n"
        "title: Zweites Gesetz\n"
        "version_date: '2024-02-01'\n"
        "---\n\n# Content\n",
        encoding="utf-8",
    )

    # Create ch/0/de/ directory with one entry
    de_dir_0 = tmp_path / "ch" / "0" / "de"
    de_dir_0.mkdir(parents=True)
    (de_dir_0 / "0.101.md").write_text(
        "---\n"
        "language: de\n"
        "source: https://fedlex.data.admin.ch\n"
        "sr_number: 0.101\n"
        "title: Konvention zum Schutze der Menschenrechte\n"
        "version_date: '2022-01-01'\n"
        "---\n\n# EMRK\n",
        encoding="utf-8",
    )

    return tmp_path


def test_extract_frontmatter(sample_repo):
    """Test frontmatter extraction from markdown files."""
    path = sample_repo / "ch" / "1" / "de" / "1.001.md"
    fm = _extract_frontmatter(path)
    assert fm is not None
    assert fm["sr_number"] == "1.001"
    assert fm["title"] == "Bundesverfassung Test"
    assert fm["language"] == "de"


def test_extract_frontmatter_no_frontmatter(tmp_path):
    """Test with a file that has no frontmatter."""
    path = tmp_path / "test.md"
    path.write_text("# Just a heading\nNo frontmatter here.\n")
    assert _extract_frontmatter(path) is None


def test_extract_frontmatter_missing_sr(tmp_path):
    """Test with frontmatter but no sr_number."""
    path = tmp_path / "test.md"
    path.write_text("---\ntitle: Test\nlanguage: de\n---\n")
    assert _extract_frontmatter(path) is None


def test_sr_sort_key():
    """Test SR number sort key generation."""
    assert _sr_sort_key("0.101") < _sr_sort_key("0.102")
    assert _sr_sort_key("1.001") < _sr_sort_key("1.002")
    assert _sr_sort_key("0.101.1") < _sr_sort_key("0.101.2")
    assert _sr_sort_key("0.101.1") < _sr_sort_key("0.101.02")
    assert _sr_sort_key("1.001") < _sr_sort_key("2.001")


def test_generate_index(sample_repo):
    """Test full index generation."""
    content = generate_index(repo_path=str(sample_repo), lang="de")

    assert "# Index of Swiss Law" in content
    assert "**3** federal laws" in content
    assert "[0.101]" in content
    assert "[1.001]" in content
    assert "[1.002]" in content
    assert "Bundesverfassung Test" in content
    assert "Konvention zum Schutze der Menschenrechte" in content
    # Check category headers
    assert "0 – Systematische Sammlung des Bundesrechts" in content
    assert "1 – Staat – Volk – Behörden" in content


def test_generate_index_links(sample_repo):
    """Test that links are properly formatted."""
    content = generate_index(repo_path=str(sample_repo), lang="de")
    assert "ch/1/de/1.001.md" in content
    assert "ch/0/de/0.101.md" in content


def test_write_index(sample_repo):
    """Test that INDEX.md is written to disk."""
    out = write_index(repo_path=str(sample_repo), lang="de")
    assert out.exists()
    assert out.name == "INDEX.md"
    content = out.read_text(encoding="utf-8")
    assert "# Index of Swiss Law" in content


def test_generate_index_missing_dir(tmp_path):
    """Test error when ch/ directory doesn't exist."""
    with pytest.raises(FileNotFoundError):
        generate_index(repo_path=str(tmp_path))


@pytest.fixture
def sample_repo_with_cantonal(sample_repo):
    """Extend sample_repo with cantonal law files."""
    # Create ch/bs/de/ directory
    bs_dir = sample_repo / "ch" / "bs" / "de"
    bs_dir.mkdir(parents=True)
    (bs_dir / "300.100.md").write_text(
        "---\n"
        "canton: BS\n"
        "language: de\n"
        "source: LexWork\n"
        "systematic_number: '300.100'\n"
        "title: Gesundheitsgesetz\n"
        "version_date: '2025-01-01'\n"
        "---\n\n# GesG\n",
        encoding="utf-8",
    )
    return sample_repo


def test_generate_index_includes_cantonal(sample_repo_with_cantonal):
    """Test that INDEX.md includes cantonal laws section."""
    content = generate_index(repo_path=str(sample_repo_with_cantonal), lang="de")
    assert "# Cantonal Laws (Kantonsrecht)" in content
    assert "BS – Basel-Stadt" in content
    assert "[300.100]" in content
    assert "Gesundheitsgesetz" in content


def test_generate_laws_json_includes_cantonal(sample_repo_with_cantonal):
    """Test that laws.json includes both federal and cantonal entries."""
    laws = generate_laws_json(repo_path=str(sample_repo_with_cantonal), lang="de")
    federal = [l for l in laws if l["scope"] == "federal"]
    cantonal = [l for l in laws if l["scope"] == "cantonal"]
    assert len(federal) == 3
    assert len(cantonal) == 1
    assert cantonal[0]["sr"] == "300.100"
    assert cantonal[0]["canton"] == "bs"
    assert cantonal[0]["cat"] == "BS – Basel-Stadt"


def test_generate_laws_json_no_cantonal(sample_repo):
    """Test laws.json with only federal laws."""
    laws = generate_laws_json(repo_path=str(sample_repo), lang="de")
    assert all(l["scope"] == "federal" for l in laws)
    assert len(laws) == 3


def _law_md(canton: str, num: str, lang: str, title: str) -> str:
    return (
        "---\n"
        f"canton: {canton.upper()}\n"
        f"language: {lang}\n"
        f"systematic_number: '{num}'\n"
        f"title: {title}\n"
        "---\n\n# Text\n"
    )


def test_empty_de_dir_falls_back_to_fr(sample_repo):
    """GE-style canton: empty de/ dir must not mask the fr/ laws."""
    (sample_repo / "ch" / "ge" / "de").mkdir(parents=True)  # empty
    ge_fr = sample_repo / "ch" / "ge" / "fr"
    ge_fr.mkdir(parents=True)
    (ge_fr / "A 1 03.md").write_text(_law_md("ge", "A 1 03", "fr", "Constitution"),
                                     encoding="utf-8")
    laws = generate_laws_json(repo_path=str(sample_repo), lang="de")
    ge = [l for l in laws if l.get("canton") == "ge"]
    assert len(ge) == 1
    assert ge[0]["path"] == "ch/ge/fr/A 1 03.md"
    assert ge[0]["languages"] == ["fr"]


def test_nested_systematic_numbers_found(sample_repo):
    """GL-style nested paths (systematic numbers containing '/') are indexed."""
    gl_nested = sample_repo / "ch" / "gl" / "de" / "III H"
    gl_nested.mkdir(parents=True)
    (gl_nested / "1.md").write_text(_law_md("gl", "III H/1", "de", "Steuergesetz"),
                                    encoding="utf-8")
    laws = generate_laws_json(repo_path=str(sample_repo), lang="de")
    gl = [l for l in laws if l.get("canton") == "gl"]
    assert len(gl) == 1
    assert gl[0]["sr"] == "III H/1"
    assert gl[0]["path"] == "ch/gl/de/III H/1.md"


def test_federal_legacy_tree_scanned(sample_repo):
    """Laws existing only in the legacy ch/{lang}/ tree must appear."""
    legacy = sample_repo / "ch" / "de" / "211"
    legacy.mkdir(parents=True)
    (legacy / "211.413.1.md").write_text(
        "---\nsr_number: '211.413.1'\nlanguage: de\ntitle: Legacy Law\n---\n\n# L\n",
        encoding="utf-8")
    laws = generate_laws_json(repo_path=str(sample_repo), lang="de")
    legacy_laws = [l for l in laws if l["sr"] == "211.413.1"]
    assert len(legacy_laws) == 1
    assert legacy_laws[0]["path"] == "ch/de/211/211.413.1.md"


def test_canonical_preferred_over_legacy(sample_repo):
    """Same (law, lang) in both trees: canonical ch/{prefix}/{lang}/ wins."""
    legacy = sample_repo / "ch" / "de"
    legacy.mkdir(parents=True, exist_ok=True)
    (legacy / "999.md").write_text(
        "---\nsr_number: '999'\nlanguage: de\ntitle: Legacy Copy\n---\n\n# L\n",
        encoding="utf-8")
    canonical = sample_repo / "ch" / "999" / "de"
    canonical.mkdir(parents=True)
    (canonical / "999.md").write_text(
        "---\nsr_number: '999'\nlanguage: de\ntitle: Canonical Copy\n---\n\n# C\n",
        encoding="utf-8")
    laws = generate_laws_json(repo_path=str(sample_repo), lang="de")
    entry = [l for l in laws if l["sr"] == "999"][0]
    assert entry["path"] == "ch/999/de/999.md"
    assert entry["title"] == "Canonical Copy"


def test_languages_array_union(sample_repo_with_cantonal):
    """languages lists every available language version of a law."""
    bs_fr = sample_repo_with_cantonal / "ch" / "bs" / "fr"
    bs_fr.mkdir(parents=True)
    (bs_fr / "300.100.md").write_text(_law_md("bs", "300.100", "fr", "Loi santé"),
                                      encoding="utf-8")
    laws = generate_laws_json(repo_path=str(sample_repo_with_cantonal), lang="de")
    bs = [l for l in laws if l.get("canton") == "bs"][0]
    assert bs["languages"] == ["de", "fr"]
    assert bs["path"] == "ch/bs/de/300.100.md"  # de preferred
