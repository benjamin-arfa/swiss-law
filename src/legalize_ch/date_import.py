"""Apply user-corrected enactment dates from a filled undated_laws.csv.

Round-trip companion to the ``undated_laws.csv`` export
(api/v1/csv/undated_laws.csv): a user fills ``corrected_enactment_date``
(YYYY-MM-DD) and optionally ``correction_note`` (source / citation), then
runs ``legalize-ch import-dates <csv>``.  Valid corrections are written to
every language version of the law as::

    enactment_date: '<date>'
    enactment_date_source: manual_import
    enactment_date_note: '<note>'   # only when a note was given

Guard rails: only laws that are currently UNDATED (no plausible evidence,
see ``enactment_year``) are touched unless ``force`` is set — authoritative
upstream data is never silently overwritten.  The statistics pick the
corrections up on the next ``legalize-ch stats`` run.
"""
from __future__ import annotations

import csv
import io
import logging
import re
from pathlib import Path

from .category_enricher import _parse_frontmatter, _write_frontmatter
from .stats import MIN_PLAUSIBLE_YEAR, enactment_year

logger = logging.getLogger(__name__)

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MAX_PLAUSIBLE_YEAR = 2100

LANGS = ("de", "fr", "it")


def _validate_date(value: str) -> str | None:
    """Return an error message, or None when the date is acceptable."""
    if not _DATE_RE.match(value):
        return "not an ISO date (YYYY-MM-DD)"
    year = int(value[:4])
    if year < MIN_PLAUSIBLE_YEAR or year > MAX_PLAUSIBLE_YEAR:
        return f"year {year} outside plausible range [{MIN_PLAUSIBLE_YEAR}, {MAX_PLAUSIBLE_YEAR}]"
    month, day = int(value[5:7]), int(value[8:10])
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return "not a valid calendar date"
    return None


def _law_files(repo: Path, entity: str, law_id: str, link: str) -> list[Path]:
    """All language files of one law.

    Cantonal laws live at ``ch/<canton>/<lang>/<id>.md``.  Federal laws sit
    under an SR-prefix directory — derived from the exported ``link`` path,
    swapping the language segment.
    """
    paths = []
    if entity != "CH":
        base = repo / "ch" / entity.lower()
    else:
        m = re.search(r"ch/([^/]+)/(?:de|fr|it)/", link)
        if not m:
            return []
        base = repo / "ch" / m.group(1)
    for lang in LANGS:
        p = base / lang / f"{law_id}.md"
        if p.exists():
            paths.append(p)
    return paths


def import_dates(csv_path: str | Path, repo_path: str | Path = ".",
                 dry_run: bool = False, force: bool = False) -> dict:
    """Apply corrections from a filled undated_laws.csv.

    Returns a summary dict: ``applied`` (laws), ``files`` (files written),
    ``skipped`` (list of (id, reason)), ``rows`` (data rows seen).
    """
    repo = Path(repo_path)
    text = Path(csv_path).read_text(encoding="utf-8")
    data_lines = [l for l in text.splitlines() if not l.startswith("#")]
    reader = csv.DictReader(io.StringIO("\n".join(data_lines)))

    applied = 0
    files_written = 0
    rows = 0
    skipped: list[tuple[str, str]] = []

    for row in reader:
        rows += 1
        law_id = (row.get("id") or "").strip()
        entity = (row.get("entity") or "").strip().upper()
        date = (row.get("corrected_enactment_date") or "").strip()
        note = (row.get("correction_note") or "").strip()
        if not date:
            continue
        label = f"{entity} {law_id}"
        err = _validate_date(date)
        if err:
            skipped.append((label, err))
            continue
        paths = _law_files(repo, entity, law_id, row.get("link", ""))
        if not paths:
            skipped.append((label, "no law files found"))
            continue

        law_files = 0
        for path in paths:
            fm, body = _parse_frontmatter(path.read_text(encoding="utf-8"))
            if fm is None:
                skipped.append((label, f"unparseable frontmatter: {path.name}"))
                continue
            if not force and enactment_year(fm):
                skipped.append((label, "already dated (use force to overwrite)"))
                break
            fm["enactment_date"] = date
            fm["enactment_date_source"] = "manual_import"
            if note:
                fm["enactment_date_note"] = note
            if not dry_run:
                path.write_text(_write_frontmatter(fm, body), encoding="utf-8")
            law_files += 1
        if law_files:
            applied += 1
            files_written += law_files

    logger.info("import-dates: %d corrections applied (%d files)%s, %d skipped",
                applied, files_written, " [dry-run]" if dry_run else "", len(skipped))
    return {"rows": rows, "applied": applied, "files": files_written,
            "skipped": skipped, "dry_run": dry_run}
