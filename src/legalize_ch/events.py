"""Legal event stream — one record per (law, date), not one per law.

The published trend chart counts *laws*: each law appears once, under the year
it was enacted.  That answers "how much law exists", not "how much law moved",
and it is the second question the Tribunal fédéral asked (frequent revisions
are what makes a judge's work laborious).  This module builds the other unit:

    event = (law, date).  seq 0 is the law's ``publication``; every later
    date is a ``revision``.

A law with a single known date contributes exactly one publication, so the
event stream is a strict superset of the law count and the two reconcile.

Provenance repair
-----------------
``version_dates`` in the frontmatter does not mean one single thing.  For
federal law it was back-filled from this repo's own commit log
(``version_dates_source: git_history``), and that walk swept up **bulk
metadata commits** alongside the genuine backdated consolidations — commits
that rewrote frontmatter for every law at once and are not legal events.
The contamination is large and one-sided: it puts ~11.7k phantom events into
2026 alone, a 5x spike in the current year.

Genuine Fedlex consolidations are recognisable without heuristics: the commit
is authored *on* the version's entry-into-force date and its subject carries
the same date, ``SR 220: <title> (2025-01-01)``.  Everything else is dropped
rather than kept-and-labelled: the discarded dates record when the enrichment
ran, not when the law changed, so there is no signal in them to preserve.
``provenance`` in the written cube reports what was dropped.
"""
from __future__ import annotations

import json
import logging
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

from .stats import _plausible_date, count_articles  # noqa: F401  (count_articles re-exported)

logger = logging.getLogger(__name__)

# "SR 220: Bundesgesetz vom 30. März 1911 ... (2025-01-01)" — the trailing
# parenthesised date is the version's entry into force, and the commit is
# author-dated to it.  Requiring both, and requiring them to agree, is what
# separates a consolidation from a bulk rewrite.
CONSOLIDATION_SUBJECT_RE = re.compile(r"^SR\s+\S+:.*\((\d{4}-\d{2}-\d{2})\)\s*$")

# version_dates_source values supplied by an upstream API, i.e. dates we did
# not reconstruct ourselves.
AUTHORITATIVE_VD_SOURCES = {"lexfind_family", "lexwork_api", "fedlex"}

# Sources we never trust on their own, because they are this repo's own
# commit log rather than an upstream statement.
GIT_DERIVED = "git_history"

DELTA_CACHE = "data/state/revision_deltas.json"


def is_consolidation(subject: str, author_date: str) -> bool:
    """True for a backdated Fedlex consolidation commit."""
    m = CONSOLIDATION_SUBJECT_RE.match(subject or "")
    return bool(m) and m.group(1) == author_date


def _git_log(repo_path: str | Path, extra: list[str]) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_path), "log", "--format=%x00%ad%x01%s",
         "--date=short", *extra, "--", "ch/"],
        capture_output=True, text=True, timeout=3600,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git log failed: {result.stderr[:400]}")
    return result.stdout


def consolidation_dates(repo_path: str | Path = ".") -> tuple[dict[str, list[str]], dict]:
    """One git walk → ({path: sorted version dates}, provenance summary).

    Only commits passing :func:`is_consolidation` contribute.
    """
    dates: dict[str, set[str]] = defaultdict(set)
    kinds: Counter[str] = Counter()
    touches: Counter[str] = Counter()

    date = kind = None
    for line in _git_log(repo_path, ["--name-only"]).splitlines():
        if line.startswith("\x00"):
            date, _, subject = line[1:].partition("\x01")
            kind = "consolidation" if is_consolidation(subject, date) else "bulk"
            kinds[kind] += 1
        elif line.strip() and kind:
            touches[kind] += 1
            if kind == "consolidation":
                dates[line.strip()].add(date)

    provenance = {
        "commits_scanned": sum(kinds.values()),
        "commits_consolidation": kinds["consolidation"],
        "commits_bulk_metadata": kinds["bulk"],
        "file_touches_consolidation": touches["consolidation"],
        "file_touches_bulk_metadata": touches["bulk"],
        "paths_with_consolidations": len(dates),
    }
    logger.info("Consolidation commits: %d of %d (%d paths)",
                kinds["consolidation"], sum(kinds.values()), len(dates))
    return {p: sorted(d) for p, d in dates.items()}, provenance


def revision_deltas(repo_path: str | Path = ".", cache: str | Path | None = DELTA_CACHE,
                    refresh: bool = False) -> dict[str, dict[str, dict]]:
    """{path: {date: {lines_added, lines_removed}}} for consolidation commits.

    How much text moved is the difference between a substantive overhaul and a
    cosmetic touch-up, and a revision *count* treats those as equal.  Only
    federal law has a versioned text history in git, so cantonal paths are
    simply absent here — a coverage asymmetry, not a zero.
    """
    cache_path = Path(repo_path) / cache if cache else None
    if cache_path and cache_path.exists() and not refresh:
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            logger.warning("Unreadable delta cache %s — rebuilding", cache_path)

    out: dict[str, dict[str, dict]] = defaultdict(dict)
    date = None
    keep = False
    for line in _git_log(repo_path, ["--numstat"]).splitlines():
        if line.startswith("\x00"):
            date, _, subject = line[1:].partition("\x01")
            keep = is_consolidation(subject, date)
            continue
        if not keep or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, removed, path = parts
        if added == "-" or removed == "-":  # binary
            continue
        prev = out[path].get(date)
        rec = {"lines_added": int(added), "lines_removed": int(removed)}
        # A path can be touched twice on the same version date (a correction
        # re-run); the magnitudes belong to the same event, so they add.
        if prev:
            rec = {k: prev[k] + rec[k] for k in rec}
        out[path][date] = rec

    result = dict(out)
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(result), encoding="utf-8")
        logger.info("Cached revision deltas for %d paths to %s", len(result), cache_path)
    return result


def law_key(e: dict) -> str:
    """Stable law identity, shared across the language versions of one act."""
    if e.get("_scope") == "cantonal" and e.get("canton"):
        return f"{e['canton']}/{e.get('systematic_number', '')}"
    return f"federal/{e.get('sr_number') or e.get('systematic_number', '')}"


def _representative(group: list[dict]) -> dict:
    de = [e for e in group if e.get("language") == "de"]
    return de[0] if de else group[0]


def _law_dates(group: list[dict], cons: dict[str, list[str]], scope: str) -> dict[str, str]:
    """{date: source} for one law, contaminated git dates already removed.

    Order matters only for the source label: the first writer of a date wins,
    so a date attested by a Fedlex consolidation keeps that provenance even
    when it also appears in a weaker field.
    """
    dated: dict[str, str] = {}

    # A Fedlex consolidation dates federal law and nothing else.  A handful of
    # cantonal files were touched by one of those commits in passing (they
    # rode along in the same batch); crediting them would date a cantonal act
    # with a federal act's entry into force.
    if scope == "federal":
        for e in group:
            for d in cons.get(e.get("_path", ""), ()):
                if _plausible_date(d):
                    dated.setdefault(d, "fedlex_consolidation")

    for e in group:
        src = str(e.get("version_dates_source", ""))
        vds = e.get("version_dates")
        if src not in AUTHORITATIVE_VD_SOURCES or not isinstance(vds, list):
            continue
        for d in vds:
            d = str(d)
            if _plausible_date(d):
                dated.setdefault(d, src)

    for e in group:
        vd = str(e.get("version_date", ""))
        if _plausible_date(vd):
            dated.setdefault(vd, "upstream_version_date")

    for e in group:
        ed = str(e.get("enactment_date", ""))
        if not _plausible_date(ed):
            continue
        # enactment dates carry their own provenance, and 1.8k of them were
        # read off the same contaminated commit log.
        if str(e.get("enactment_date_source", "")) == GIT_DERIVED and ed not in dated:
            continue
        dated.setdefault(ed, f"enactment:{e.get('enactment_date_source', '') or 'unknown'}")

    return dated


def build_events(entries: list[dict], cons: dict[str, list[str]],
                 deltas: dict[str, dict[str, dict]] | None = None) -> list[dict]:
    """File-level frontmatter entries → the event stream (spec §3).

    ``entries`` is :func:`legalize_ch.stats.collect_all_frontmatter` output —
    one dict per *file*; the language versions of one act are one law here and
    therefore one event per date, not three.
    """
    deltas = deltas or {}
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        groups[law_key(e)].append(e)

    events: list[dict] = []
    for key, group in sorted(groups.items()):
        rep = _representative(group)
        scope = rep.get("_scope", "federal")
        dated = _law_dates(group, cons, scope)
        if not dated:
            continue
        # magnitude is measured on one language version — the German file
        # where there is one — because summing three translations of the same
        # amendment would treble it.
        delta_path = rep.get("_path", "")
        path_deltas = deltas.get(delta_path, {})
        # The earliest delta on a path is the text ARRIVING in this corpus, not
        # the law changing: a backfilled act shows its whole body as lines
        # added on the day it was imported.  Counting it would make magnitude
        # track our own collection work — it was 51% of the 2026 total before
        # this exclusion — so the first recorded version of each law carries no
        # magnitude and the series measures amendments only.
        first_delta = min(path_deltas) if path_deltas else None
        last = max(dated)

        canton = rep.get("canton") or ""
        domain = str(rep.get("global_category") or rep.get("global_category_inferred") or "")
        law_type = str(rep.get("category_type") or rep.get("category_type_inferred") or "")

        for seq, date in enumerate(sorted(dated)):
            # Empty optional fields are omitted rather than written as null:
            # at 140k records a constant key costs megabytes per rebuild, and
            # the year files are regenerated on every update.  ``confidence``
            # is only written when it is NOT the "authoritative" default.
            rec = {
                "date": date,
                "law": key,
                "scope": scope,
                "event": "publication" if seq == 0 else "revision",
                "seq": seq,
                "source": dated[date],
            }
            if canton:
                rec["canton"] = canton
            if domain:
                rec["domain"] = domain
            if law_type:
                rec["type"] = law_type
            d = path_deltas.get(date)
            if d and date != first_delta:
                rec["delta"] = d
            if date == last:
                rec["size_current"] = {
                    "chars": rep.get("_body_chars", 0),
                    "articles": rep.get("_body_articles", 0),
                }
            events.append(rec)

    logger.info("Built %d events over %d laws", len(events), len(groups))
    return events


def _lines(rec: dict) -> int:
    d = rec.get("delta")
    return (d["lines_added"] + d["lines_removed"]) if d else 0


def aggregate_events(events: list[dict], provenance: dict | None = None) -> dict:
    """Year x scope x event-kind cube for the dashboard chart."""
    by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: {"publication": 0, "revision": 0,
                                     "lines": 0, "revisions_with_delta": 0})
    )
    totals = Counter()
    sources = Counter()

    for r in events:
        year = r["date"][:4]
        cell = by_year[year][r["scope"]]
        cell[r["event"]] += 1
        totals[r["event"]] += 1
        sources[r["source"]] += 1
        n = _lines(r)
        if n and r["event"] == "revision":
            cell["lines"] += n
            cell["revisions_with_delta"] += 1

    years = sorted(by_year)
    return {
        "counting_unit": "legal_event",
        "unit_definition": (
            "One record per (law, date). seq 0 is the law's publication, every "
            "later known in-force date is a revision. Language versions of one "
            "act are one law, so a trilingual consolidation is one event."
        ),
        "years": years,
        "earliest_year": years[0] if years else None,
        "latest_year": years[-1] if years else None,
        "totals": {
            "events": sum(totals.values()),
            "publications": totals["publication"],
            "revisions": totals["revision"],
            "laws_with_events": totals["publication"],
        },
        "by_source": dict(sources.most_common()),
        "by_year": {y: {s: dict(c) for s, c in sorted(by_year[y].items())} for y in years},
        "provenance": provenance or {},
    }


def _months_between(a: str, b: str) -> float:
    ya, ma, da = int(a[:4]), int(a[5:7]), int(a[8:10])
    yb, mb, db = int(b[:4]), int(b[5:7]), int(b[8:10])
    return (yb - ya) * 12 + (mb - ma) + (db - da) / 30.44


def compute_indicators(events: list[dict], entries: list[dict]) -> dict:
    """Workload indicators per year x scope (spec §4).

    ``churn`` and ``instability`` are the two that answer the TF's question
    directly, because both are normalised by the stock of law in force: a
    domain where the median law moves every 14 months is a different working
    environment from one where it moves every 9 years, whatever the corpus size.
    """
    repealed: dict[str, str] = {}
    for e in entries:
        rd = str(e.get("repealed_date", ""))
        if _plausible_date(rd):
            k = law_key(e)
            repealed[k] = min(repealed.get(k, rd), rd)

    first_year: dict[str, str] = {}
    prev_date: dict[str, str] = {}
    gaps: dict[str, list[float]] = defaultdict(list)      # year -> gaps (months)
    per_year: dict[str, dict] = defaultdict(
        lambda: defaultdict(lambda: {"publications": 0, "revisions": 0, "lines": 0,
                                     "laws_revised": set()})
    )

    # Every event lands in its own scope AND in the pooled "all" bucket. A
    # median cannot be recombined after the fact — averaging the federal and
    # cantonal medians is not the median of the two together — so the pooled
    # figures are computed here rather than in the page.
    for r in sorted(events, key=lambda r: (r["law"], r["date"])):
        year, law, scope = r["date"][:4], r["law"], r["scope"]
        for sk in (scope, "all"):
            cell = per_year[year][sk]
            if r["event"] == "publication":
                cell["publications"] += 1
            else:
                cell["revisions"] += 1
                cell["laws_revised"].add(law)
                cell["lines"] += _lines(r)
                if law in prev_date:
                    gaps[f"{year}/{sk}"].append(_months_between(prev_date[law], r["date"]))
        if r["event"] == "publication":
            first_year[law] = year
        prev_date[law] = r["date"]

    scopes_of: dict[str, str] = {}
    for r in events:
        scopes_of.setdefault(r["law"], r["scope"])

    out: dict[str, dict] = {}
    for year in sorted(per_year):
        out[year] = {}
        for scope, cell in sorted(per_year[year].items()):
            in_force = sum(
                1 for law, fy in first_year.items()
                if (scope == "all" or scopes_of.get(law) == scope) and fy <= year
                and (law not in repealed or repealed[law][:4] > year)
            )
            g = gaps.get(f"{year}/{scope}", [])
            out[year][scope] = {
                "volume": cell["publications"] + cell["revisions"],
                "publications": cell["publications"],
                "revisions": cell["revisions"],
                "laws_in_force": in_force,
                "laws_revised": len(cell["laws_revised"]),
                "churn": round(cell["revisions"] / in_force, 4) if in_force else None,
                "instability": round(len(cell["laws_revised"]) / in_force, 4) if in_force else None,
                "median_gap_months": round(median(g), 1) if g else None,
                "lines_changed": cell["lines"],
                "weighted_churn": round(cell["lines"] / in_force, 1) if in_force and cell["lines"] else None,
            }

    return {
        "definitions": {
            "volume": "events in the year (publications + revisions)",
            "churn": "revision events in the year / laws in force that year",
            "instability": "share of laws in force revised at least once in the year",
            "median_gap_months": "median months since the same law's previous event, over the year's revisions",
            "scopes": "federal, cantonal, and all — 'all' is computed over the pooled events, not averaged from the other two",
            "lines_changed": "lines added + removed per revision, summed (federal only — cantonal law has no versioned text history)",
            "weighted_churn": "lines changed / laws in force",
            "laws_in_force": "laws whose publication year is on or before this year and whose repeal, if recorded, is after it",
        },
        "coverage": {
            "magnitude_scope": "federal",
            "magnitude_note": (
                "delta comes from git numstat on the backdated consolidation "
                "commits, which exist for federal law only; cantonal cells "
                "report no lines rather than zero lines. Each law's earliest "
                "recorded version carries no delta — that commit is the text "
                "entering the corpus, not the law changing."
            ),
        },
        "by_year": out,
    }


# ─── Writers ──────────────────────────────────────────────────────────────────

def write_events(events: list[dict], output_dir: str | Path) -> dict:
    """Per-year event files + index, mirroring write_publications()."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    by_year: dict[str, list[dict]] = defaultdict(list)
    for r in events:
        by_year[r["date"][:4]].append(r)

    for year, recs in by_year.items():
        recs.sort(key=lambda r: (r["date"], r["law"]))
        payload = {"date_prefix": year, "count": len(recs),
                   "counting_unit": "legal_event",
                   "default_confidence": "authoritative",
                   "events": recs}
        (out / f"{year}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8")

    years = sorted(by_year)
    index = {
        "years": years,
        "total_events": len(events),
        "earliest_year": years[0] if years else None,
        "latest_year": years[-1] if years else None,
    }
    (out / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Wrote %d year files (%d events) to %s", len(years), len(events), out)
    return index


def write_json(payload: dict, path: str | Path) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return p
