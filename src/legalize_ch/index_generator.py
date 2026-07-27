"""Generate INDEX.md with all SR numbers, titles, and links (federal + cantonal)."""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# SR category names (top-level classification)
SR_CATEGORIES = {
    "0": "Systematische Sammlung des Bundesrechts (Völkerrecht)",
    "1": "Staat – Volk – Behörden",
    "2": "Privatrecht – Zivilrechtspflege – Vollstreckung",
    "3": "Strafrecht – Strafrechtspflege – Strafvollzug",
    "4": "Schule – Wissenschaft – Kultur",
    "5": "Landesverteidigung",
    "6": "Finanzen",
    "7": "Öffentliche Werke – Energie – Verkehr",
    "8": "Gesundheit – Arbeit – Soziale Sicherheit",
    "9": "Wirtschaft – Technische Zusammenarbeit",
}

# Canton full names
CANTON_NAMES = {
    "ag": "Aargau",
    "ai": "Appenzell Innerrhoden",
    "ar": "Appenzell Ausserrhoden",
    "be": "Bern",
    "bl": "Basel-Landschaft",
    "bs": "Basel-Stadt",
    "fr": "Fribourg",
    "ge": "Genève",
    "gl": "Glarus",
    "gr": "Graubünden",
    "ju": "Jura",
    "lu": "Luzern",
    "ne": "Neuchâtel",
    "nw": "Nidwalden",
    "ow": "Obwalden",
    "sg": "St. Gallen",
    "sh": "Schaffhausen",
    "so": "Solothurn",
    "sz": "Schwyz",
    "tg": "Thurgau",
    "ti": "Ticino",
    "ur": "Uri",
    "vd": "Vaud",
    "vs": "Valais",
    "zg": "Zug",
    "zh": "Zürich",
}

# Known federal SR prefix directories (numeric)
_FEDERAL_PREFIXES = set(str(i) for i in range(10))


def _extract_frontmatter(path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    if not text.startswith("---"):
        return None

    end = text.find("\n---", 3)
    if end == -1:
        return None

    frontmatter = {}
    for line in text[4:end].split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip("'\"")
            if key in ("sr_number", "title", "language", "version_date",
                       "canton", "systematic_number", "abbreviation"):
                frontmatter[key] = value
    return frontmatter if ("sr_number" in frontmatter or "systematic_number" in frontmatter) else None


def _is_canton_dir(name: str) -> bool:
    """Check if a directory name is a canton code (not a federal SR prefix)."""
    return name in CANTON_NAMES


_TREE_LANGS = ("de", "fr", "it")


def _lang_preference(lang: str) -> list[str]:
    """Preferred-language order: requested language first, then de/fr/it."""
    return [lang] + [l for l in _TREE_LANGS if l != lang]


def _collect_federal_entries(ch_dir: Path, lang: str) -> dict[str, dict]:
    """Collect federal law entries: sr_number -> {title, path, languages}.

    Scans the canonical tree ``ch/{prefix}/{lang}/*.md`` AND the legacy tree
    ``ch/{de,fr,it}/**/*.md`` (some laws exist only there).  Per law, the
    requested language is preferred (de/fr/it fallback), and the canonical
    tree wins over the legacy tree for the same (law, language).
    """
    # candidates[sr][lang] = (path, title, is_canonical)
    candidates: dict[str, dict[str, tuple[str, str, bool]]] = {}

    def _add(md_file: Path, file_lang: str, canonical: bool):
        fm = _extract_frontmatter(md_file)
        if not fm or not fm.get("sr_number"):
            return
        sr = fm["sr_number"]
        file_lang = fm.get("language", file_lang) or file_lang
        title = fm.get("title", "(kein Titel)")
        rel = str(md_file.relative_to(ch_dir.parent))
        existing = candidates.setdefault(sr, {}).get(file_lang)
        if existing and existing[2] and not canonical:
            return  # canonical already present
        if existing is None or (canonical and not existing[2]):
            candidates[sr][file_lang] = (rel, title, canonical)

    for subdir in sorted(ch_dir.iterdir()):
        if not subdir.is_dir() or _is_canton_dir(subdir.name):
            continue
        if subdir.name in _TREE_LANGS or subdir.name == "en":
            # Legacy tree ch/{lang}/... (flat files and prefix subdirs)
            if subdir.name != "en":
                for md_file in sorted(subdir.rglob("*.md")):
                    _add(md_file, subdir.name, canonical=False)
            continue
        # Canonical tree ch/{prefix}/{lang}/
        for tree_lang in _TREE_LANGS:
            lang_dir = subdir / tree_lang
            if not lang_dir.is_dir():
                continue
            for md_file in sorted(lang_dir.rglob("*.md")):
                _add(md_file, tree_lang, canonical=True)

    entries: dict[str, dict] = {}
    for sr, per_lang in candidates.items():
        for pick in _lang_preference(lang):
            if pick in per_lang:
                path, title, _ = per_lang[pick]
                entries[sr] = {
                    "title": title,
                    "path": path,
                    "languages": sorted(per_lang.keys()),
                }
                break

    return entries


def _collect_cantonal_entries(ch_dir: Path, lang: str = "de") -> dict[str, list[dict]]:
    """Collect cantonal law entries grouped by canton.

    Returns canton_code -> list of {id, title, path, languages}.  Uses
    rglob so nested systematic numbers (e.g. GL ``III H/1``) are found,
    and treats a language as available only when it has actual files —
    empty ``de/`` dirs (GE, JU, NE, TI, VD) no longer mask fr/it laws.
    """
    cantonal: dict[str, list[dict]] = {}

    for subdir in sorted(ch_dir.iterdir()):
        if not subdir.is_dir() or not _is_canton_dir(subdir.name):
            continue
        canton = subdir.name

        # candidates[sys_num][lang] = (path, title)
        candidates: dict[str, dict[str, tuple[str, str]]] = {}
        for tree_lang in _TREE_LANGS + ("rm",):
            lang_dir = subdir / tree_lang
            if not lang_dir.is_dir():
                continue
            for md_file in sorted(lang_dir.rglob("*.md")):
                fm = _extract_frontmatter(md_file)
                if not fm:
                    continue
                sys_num = fm.get("systematic_number") or str(
                    md_file.relative_to(lang_dir))[:-3]
                title = fm.get("title", "(kein Titel)")
                rel = str(md_file.relative_to(ch_dir.parent))
                candidates.setdefault(sys_num, {}).setdefault(
                    tree_lang, (rel, title))

        entries = []
        for sys_num in sorted(candidates):
            per_lang = candidates[sys_num]
            for pick in _lang_preference(lang) + ["rm"]:
                if pick in per_lang:
                    path, title = per_lang[pick]
                    entries.append({
                        "id": sys_num,
                        "title": title,
                        "path": path,
                        "languages": sorted(per_lang.keys()),
                    })
                    break

        if entries:
            cantonal[canton] = entries

    return cantonal


def generate_index(repo_path: str = ".", lang: str = "de") -> str:
    """Generate INDEX.md content from all markdown files (federal + cantonal).

    Args:
        repo_path: Path to the swiss-law repo root.
        lang: Language to use for titles (de, fr, it).

    Returns:
        The full INDEX.md content as a string.
    """
    repo = Path(repo_path)
    ch_dir = repo / "ch"

    if not ch_dir.exists():
        raise FileNotFoundError(f"Directory not found: {ch_dir}")

    # Collect federal entries
    entries = _collect_federal_entries(ch_dir, lang)
    # Collect cantonal entries
    cantonal = _collect_cantonal_entries(ch_dir, lang)

    total_cantonal = sum(len(v) for v in cantonal.values())
    logger.info(f"Found {len(entries)} federal + {total_cantonal} cantonal laws ({lang})")

    # Build INDEX.md
    lines: list[str] = []
    lines.append("# Index of Swiss Law (Systematische Rechtssammlung)")
    lines.append("")
    lines.append(f"Total: **{len(entries)}** federal laws, **{total_cantonal}** cantonal laws indexed")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Federal Laws ===
    lines.append("# Federal Laws (Bundesrecht)")
    lines.append("")

    # Group by top-level category
    categorized: dict[str, list[tuple[str, dict]]] = {}
    for sr, entry in sorted(entries.items(), key=lambda x: _sr_sort_key(x[0])):
        cat = sr.split(".")[0] if "." in sr else sr
        top = cat.split(".")[0]
        top_cat = top[0] if top else "0"
        categorized.setdefault(top_cat, []).append((sr, entry))

    for cat_num in sorted(categorized.keys()):
        cat_name = SR_CATEGORIES.get(cat_num, f"Kategorie {cat_num}")
        cat_entries = categorized[cat_num]
        lines.append(f"## {cat_num} – {cat_name}")
        lines.append("")
        lines.append(f"*{len(cat_entries)} laws*")
        lines.append("")
        lines.append("| SR Number | Title |")
        lines.append("|-----------|-------|")

        for sr, entry in cat_entries:
            title = entry["title"]
            display_title = title if len(title) <= 120 else title[:117] + "..."
            display_title = display_title.replace("|", "\\|")
            lines.append(f"| [{sr}]({entry['path']}) | {display_title} |")

        lines.append("")

    # === Cantonal Laws ===
    if cantonal:
        lines.append("---")
        lines.append("")
        lines.append("# Cantonal Laws (Kantonsrecht)")
        lines.append("")
        lines.append(f"*{total_cantonal} laws across {len(cantonal)} canton(s)*")
        lines.append("")

        for canton in sorted(cantonal.keys()):
            canton_name = CANTON_NAMES.get(canton, canton.upper())
            canton_entries = cantonal[canton]
            lines.append(f"## {canton.upper()} – {canton_name}")
            lines.append("")
            lines.append(f"*{len(canton_entries)} laws*")
            lines.append("")
            lines.append("| Systematic Number | Title |")
            lines.append("|-------------------|-------|")

            for entry in canton_entries:
                title = entry["title"]
                display_title = title if len(title) <= 120 else title[:117] + "..."
                display_title = display_title.replace("|", "\\|")
                lines.append(f"| [{entry['id']}]({entry['path']}) | {display_title} |")

            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Generated automatically by the swiss-law pipeline.*")
    lines.append("")

    return "\n".join(lines)


def generate_laws_json(repo_path: str = ".", lang: str = "de") -> list[dict]:
    """Generate a JSON array of all laws (federal + cantonal) for GitHub Pages.

    Returns:
        List of dicts with keys: sr, title, path, cat, scope, canton (optional)
    """
    repo = Path(repo_path)
    ch_dir = repo / "ch"

    if not ch_dir.exists():
        raise FileNotFoundError(f"Directory not found: {ch_dir}")

    laws: list[dict] = []

    # Federal
    entries = _collect_federal_entries(ch_dir, lang)
    for sr, entry in sorted(entries.items(), key=lambda x: _sr_sort_key(x[0])):
        sr_prefix = sr.split(".")[0]
        top_cat = sr_prefix[0] if sr_prefix else "0"
        cat_name = SR_CATEGORIES.get(top_cat, f"Kategorie {top_cat}")
        laws.append({
            "sr": sr,
            "title": entry["title"],
            "path": entry["path"],
            "cat": f"{top_cat} – {cat_name}",
            "scope": "federal",
            "languages": entry["languages"],
        })

    # Cantonal
    cantonal = _collect_cantonal_entries(ch_dir, lang)
    for canton in sorted(cantonal.keys()):
        canton_name = CANTON_NAMES.get(canton, canton.upper())
        for entry in cantonal[canton]:
            laws.append({
                "sr": entry["id"],
                "title": entry["title"],
                "path": entry["path"],
                "cat": f"{canton.upper()} – {canton_name}",
                "scope": "cantonal",
                "canton": canton,
                "languages": entry["languages"],
            })

    return laws


def _sr_sort_key(sr: str) -> tuple:
    """Convert SR number to a sortable tuple of numeric parts."""
    parts = sr.split(".")
    result = []
    for p in parts:
        sub_parts = p.split("-")
        for sp in sub_parts:
            try:
                result.append(int(sp))
            except ValueError:
                result.append(0)
    return tuple(result)


def write_index(repo_path: str = ".", lang: str = "de") -> Path:
    """Generate and write INDEX.md to the repo root.

    Returns:
        Path to the written INDEX.md file.
    """
    content = generate_index(repo_path=repo_path, lang=lang)
    out_path = Path(repo_path) / "INDEX.md"
    out_path.write_text(content, encoding="utf-8")
    logger.info(f"Written: {out_path} ({len(content)} bytes)")
    return out_path


def write_laws_json(repo_path: str = ".", lang: str = "de") -> Path:
    """Generate and write docs/laws.json for GitHub Pages.

    Returns:
        Path to the written laws.json file.
    """
    laws = generate_laws_json(repo_path=repo_path, lang=lang)
    out_path = Path(repo_path) / "docs" / "laws.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(laws, ensure_ascii=False), encoding="utf-8")
    logger.info(f"Written: {out_path} ({len(laws)} entries)")
    return out_path
