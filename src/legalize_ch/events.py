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

Genuine consolidations are recognisable without heuristics: the commit is
authored *on* the version's entry-into-force date and its subject carries the
same date and the law's own register prefix — ``SR 220: <title> (2025-01-01)``
federally, ``BE 811.011: <title> (2023-01-01)`` for a canton.  Everything else
is dropped rather than kept-and-labelled: the discarded dates record when the
enrichment ran, not when the law changed, so there is no signal in them to
preserve.  ``provenance`` in the written cube reports what was dropped.

The prefix is not decoration: it is what stops a commit from dating a file that
merely rode along in the same batch, and it applies in both directions (a
federal consolidation must not date a cantonal act, and vice versa).

Text volume
-----------
Two different magnitudes, with two different coverages, and the page must not
confuse them:

``lines`` — how much text a revision *moved*, from git numstat.  It needs two
versions of the same file to diff, so it exists wherever the corpus recorded a
law more than once.  Federal law has a real version history (69k measurable
revisions); the cantonal corpus was imported at one version per law, so 19,207
of 19,575 cantonal files have nothing to diff against.

``articles`` — how much text was *in play*, from the markdown bodies
themselves.  Every law in the corpus has a body, so this one covers federal and
cantonal law alike.  It is the law's *current* size credited to each of its
events, which is exact for recent years and anachronistic for old ones — a law
revised in 1995 is credited with the size it has today.
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

# "SR 220: Bundesgesetz vom 30. März 1911 ... (2025-01-01)", and the cantonal
# form "BE 811.011: Verordnung über ... (2023-01-01)".  The trailing
# parenthesised date is the version's entry into force and the commit is
# author-dated to it; requiring both, and requiring them to agree, is what
# separates a consolidation from a bulk rewrite.  The leading token is the
# law's register — SR for federal law, the two-letter canton code otherwise —
# and it is captured so a commit can only date files from its own register.
CONSOLIDATION_SUBJECT_RE = re.compile(
    r"^(SR|[A-Z]{2})\s+\S+:.*\((\d{4}-\d{2}-\d{2})\)\s*$")

# version_dates_source values supplied by an upstream API, i.e. dates we did
# not reconstruct ourselves.
AUTHORITATIVE_VD_SOURCES = {"lexfind_family", "lexwork_api", "fedlex"}

# Sources we never trust on their own, because they are this repo's own
# commit log rather than an upstream statement.
GIT_DERIVED = "git_history"

DELTA_CACHE = "data/state/revision_deltas.json"


def is_consolidation(subject: str, author_date: str) -> str:
    """The commit's register prefix if it is a backdated consolidation, else "".

    Truthy/falsy exactly where the old boolean was, so ``if
    is_consolidation(...)`` still reads correctly; the value identifies *which*
    register the commit may date.
    """
    m = CONSOLIDATION_SUBJECT_RE.match(subject or "")
    return m.group(1) if (m and m.group(2) == author_date) else ""


def law_prefix(entry: dict) -> str:
    """The register a law belongs to: "SR" federally, else the canton code.

    Read from the frontmatter ``canton`` field and never from the path — the
    corpus keeps federal French law and Fribourg law both under ``ch/fr/``.
    """
    canton = entry.get("canton")
    return str(canton).upper() if canton else "SR"


def _git_log(repo_path: str | Path, extra: list[str]) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_path), "log", "--format=%x00%ad%x01%s",
         "--date=short", *extra, "--", "ch/"],
        capture_output=True, text=True, timeout=3600,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git log failed: {result.stderr[:400]}")
    return result.stdout


def consolidation_dates(repo_path: str | Path = ".") -> tuple[dict[str, dict[str, str]], dict]:
    """One git walk → ({path: {date: register prefix}}, provenance summary).

    Only commits passing :func:`is_consolidation` contribute.  The prefix
    travels with the date so the caller can reject a commit that touched a file
    from another register.
    """
    dates: dict[str, dict[str, str]] = defaultdict(dict)
    kinds: Counter[str] = Counter()
    touches: Counter[str] = Counter()

    date = prefix = None
    for line in _git_log(repo_path, ["--name-only"]).splitlines():
        if line.startswith("\x00"):
            date, _, subject = line[1:].partition("\x01")
            prefix = is_consolidation(subject, date)
            kinds["consolidation" if prefix else "bulk"] += 1
            if prefix:
                kinds["federal" if prefix == "SR" else "cantonal"] += 1
        elif line.strip() and date:
            touches["consolidation" if prefix else "bulk"] += 1
            if prefix:
                dates[line.strip()][date] = prefix

    provenance = {
        "commits_scanned": sum(kinds[k] for k in ("consolidation", "bulk")),
        "commits_consolidation": kinds["consolidation"],
        "commits_consolidation_federal": kinds["federal"],
        "commits_consolidation_cantonal": kinds["cantonal"],
        "commits_bulk_metadata": kinds["bulk"],
        "file_touches_consolidation": touches["consolidation"],
        "file_touches_bulk_metadata": touches["bulk"],
        "paths_with_consolidations": len(dates),
    }
    logger.info("Consolidation commits: %d of %d (%d federal, %d cantonal, %d paths)",
                kinds["consolidation"], provenance["commits_scanned"],
                kinds["federal"], kinds["cantonal"], len(dates))
    return dict(dates), provenance


def revision_deltas(repo_path: str | Path = ".", cache: str | Path | None = DELTA_CACHE,
                    refresh: bool = False) -> dict[str, dict[str, dict]]:
    """{path: {date: {lines_added, lines_removed, prefix}}} for consolidations.

    How much text moved is the difference between a substantive overhaul and a
    cosmetic touch-up, and a revision *count* treats those as equal.  Measuring
    it needs two versions of the same file: federal law has a real version
    history here, while the cantonal corpus was imported at one version per law,
    so cantonal coverage is a rounding error rather than a series.  See the
    module docstring — ``articles`` is the magnitude that covers both.
    """
    cache_path = Path(repo_path) / cache if cache else None
    if cache_path and cache_path.exists() and not refresh:
        try:
            payload = json.loads(cache_path.read_text(encoding="utf-8"))
            # the cache predates the register prefix if it has no version marker
            if isinstance(payload, dict) and payload.get("cache_version") == 2:
                return payload["deltas"]
            logger.info("Delta cache %s is an older shape — rebuilding", cache_path)
        except (OSError, ValueError):
            logger.warning("Unreadable delta cache %s — rebuilding", cache_path)

    out: dict[str, dict[str, dict]] = defaultdict(dict)
    date = None
    prefix = ""
    for line in _git_log(repo_path, ["--numstat"]).splitlines():
        if line.startswith("\x00"):
            date, _, subject = line[1:].partition("\x01")
            prefix = is_consolidation(subject, date)
            continue
        if not prefix or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, removed, path = parts
        if added == "-" or removed == "-":  # binary
            continue
        prev = out[path].get(date)
        rec = {"lines_added": int(added), "lines_removed": int(removed),
               "prefix": prefix}
        # A path can be touched twice on the same version date (a correction
        # re-run); the magnitudes belong to the same event, so they add.
        if prev and prev.get("prefix") == prefix:
            rec = {"lines_added": prev["lines_added"] + rec["lines_added"],
                   "lines_removed": prev["lines_removed"] + rec["lines_removed"],
                   "prefix": prefix}
        out[path][date] = rec

    result = dict(out)
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps({"cache_version": 2, "deltas": result}),
                              encoding="utf-8")
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


def _law_dates(group: list[dict], cons: dict[str, dict[str, str]],
               prefix: str) -> dict[str, str]:
    """{date: source} for one law, contaminated git dates already removed.

    Order matters only for the source label: the first writer of a date wins,
    so a date attested by a Fedlex consolidation keeps that provenance even
    when it also appears in a weaker field.
    """
    dated: dict[str, str] = {}

    # A consolidation dates law from its own register and nothing else.  Six
    # files were touched by a commit from another register in passing (they
    # rode along in the same batch); crediting them would date, say, a Zurich
    # act with a federal act's entry into force.
    for e in group:
        for d, pfx in cons.get(e.get("_path", ""), {}).items():
            if pfx == prefix and _plausible_date(d):
                dated.setdefault(
                    d, "fedlex_consolidation" if pfx == "SR" else "cantonal_consolidation")

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


def build_events(entries: list[dict], cons: dict[str, dict[str, str]],
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
        prefix = law_prefix(rep)
        dated = _law_dates(group, cons, prefix)
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
            if d and date != first_delta and d.get("prefix", "SR") == prefix:
                rec["delta"] = {"lines_added": d["lines_added"],
                                "lines_removed": d["lines_removed"]}
            if date == last:
                rec["size_current"] = {
                    "chars": rep.get("_body_chars", 0),
                    "articles": rep.get("_body_articles", 0),
                }
            events.append(rec)

    logger.info("Built %d events over %d laws", len(events), len(groups))
    return events


def law_sizes(entries: list[dict]) -> dict[str, dict[str, int]]:
    """{law key: {chars, articles}} — the body metrics of one language version.

    The second magnitude on the page.  Unlike ``lines`` it needs no version
    history, only the text, so it covers cantonal law as completely as federal:
    every file in the corpus has a body.  Measured on the German version where
    there is one, for the same reason the deltas are — three translations of one
    act are one law, and summing them would treble it.
    """
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        groups[law_key(e)].append(e)
    out = {}
    for key, group in groups.items():
        rep = _representative(group)
        out[key] = {"chars": int(rep.get("_body_chars") or 0),
                    "articles": int(rep.get("_body_articles") or 0)}
    return out


def _lines(rec: dict) -> int:
    d = rec.get("delta")
    return (d["lines_added"] + d["lines_removed"]) if d else 0


def aggregate_events(events: list[dict], provenance: dict | None = None,
                     sizes: dict[str, dict[str, int]] | None = None) -> dict:
    """Year x scope x event-kind cube for the dashboard chart.

    ``sizes`` (from :func:`law_sizes`) adds the article counts, which are the
    only magnitude that covers cantonal law; without it those cells are zero and
    the page must not offer the measure.
    """
    sizes = sizes or {}
    by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: {"publication": 0, "revision": 0,
                                     "lines": 0, "revisions_with_delta": 0,
                                     "articles_publication": 0,
                                     "articles_revision": 0})
    )
    totals = Counter()
    sources = Counter()

    for r in events:
        year = r["date"][:4]
        cell = by_year[year][r["scope"]]
        cell[r["event"]] += 1
        totals[r["event"]] += 1
        sources[r["source"]] += 1
        cell[f"articles_{r['event']}"] += sizes.get(r["law"], {}).get("articles", 0)
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
        "measures": {
            "publication/revision": "event counts",
            "lines": (
                "lines added + removed by the revision, from git numstat on the "
                "consolidation commits. Needs two versions of a file to diff, so "
                "it is federal law in practice — the cantonal corpus holds one "
                "version per law."
            ),
            "articles_publication/articles_revision": (
                "articles of the law the event applies to, from the markdown "
                "body. Covers federal and cantonal law alike, because every law "
                "in the corpus has a text. It is the law's CURRENT size credited "
                "to each of its events, so recent years are exact and older ones "
                "are anachronistic."
            ),
        },
        "by_year": {y: {s: dict(c) for s, c in sorted(by_year[y].items())} for y in years},
        "provenance": provenance or {},
    }


def _months_between(a: str, b: str) -> float:
    ya, ma, da = int(a[:4]), int(a[5:7]), int(a[8:10])
    yb, mb, db = int(b[:4]), int(b[5:7]), int(b[8:10])
    return (yb - ya) * 12 + (mb - ma) + (db - da) / 30.44


def compute_indicators(events: list[dict], entries: list[dict],
                       sizes: dict[str, dict[str, int]] | None = None) -> dict:
    """Workload indicators per year x scope (spec §4).

    ``churn`` and ``instability`` are the two that answer the TF's question
    directly, because both are normalised by the stock of law in force: a
    domain where the median law moves every 14 months is a different working
    environment from one where it moves every 9 years, whatever the corpus size.
    """
    sizes = sizes or {}
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
                                     "articles": 0, "laws_revised": set()})
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
                cell["articles"] += sizes.get(law, {}).get("articles", 0)
                if law in prev_date:
                    gaps[f"{year}/{sk}"].append(_months_between(prev_date[law], r["date"]))
        if r["event"] == "publication":
            first_year[law] = year
        prev_date[law] = r["date"]

    scopes_of: dict[str, str] = {}
    # How much of each scope's magnitude is actually measured, counted rather
    # than asserted: a hardcoded share would drift on every weekly rebuild, and
    # this is the number that decides whether the page may offer the measure.
    measured: dict[str, Counter] = defaultdict(Counter)
    for r in events:
        scopes_of.setdefault(r["law"], r["scope"])
        if r["event"] == "revision":
            measured[r["scope"]]["revisions"] += 1
            if r.get("delta"):
                measured[r["scope"]]["with_delta"] += 1

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
                "articles_in_revised_laws": cell["articles"],
                "weighted_churn": round(cell["lines"] / in_force, 1) if in_force and cell["lines"] else None,
                "article_churn": round(cell["articles"] / in_force, 1) if in_force and cell["articles"] else None,
            }

    return {
        "definitions": {
            "volume": "events in the year (publications + revisions)",
            "churn": "revision events in the year / laws in force that year",
            "instability": "share of laws in force revised at least once in the year",
            "median_gap_months": "median months since the same law's previous event, over the year's revisions",
            "scopes": "federal, cantonal, and all — 'all' is computed over the pooled events, not averaged from the other two",
            "lines_changed": "lines added + removed per revision, summed (federal in practice — see coverage)",
            "articles_in_revised_laws": (
                "articles of the laws revised that year, summed over the year's "
                "revisions — the article-weight of revision activity, not a count "
                "of articles that changed (federal and cantonal alike)"
            ),
            "weighted_churn": "lines changed / laws in force",
            "article_churn": "articles in revised laws / laws in force",
            "laws_in_force": "laws whose publication year is on or before this year and whose repeal, if recorded, is after it",
        },
        "coverage": {
            "lines_changed_scope": "federal",
            "lines_changed_measured": {
                scope: {
                    "revisions": c["revisions"],
                    "revisions_with_delta": c["with_delta"],
                    "share": round(c["with_delta"] / c["revisions"], 4) if c["revisions"] else None,
                }
                for scope, c in sorted(measured.items())
            },
            "lines_changed_note": (
                "delta comes from git numstat on the backdated consolidation "
                "commits, and diffing needs two recorded versions of a file. "
                "Federal law has a version history; the cantonal corpus was "
                "imported at one version per law, so almost no cantonal revision "
                "has anything to diff against — see lines_changed_measured for "
                "the share actually measured in each scope. What cantonal lines "
                "do exist are concentrated in the years the corpus was being "
                "built, which would read as a surge in legislative activity, so "
                "the page reports no cantonal lines rather than zero lines. Each "
                "law's earliest recorded version carries no delta either — that "
                "commit is the text entering the corpus, not the law changing."
            ),
            "articles_in_revised_laws_scope": "federal and cantonal",
            "articles_in_revised_laws_note": (
                "counted from the markdown body, which every law in the corpus "
                "has, so this magnitude has no scope gap. It credits each revision "
                "with the whole article count of the law revised — the corpus "
                "records the text before and after, not which articles the "
                "revision rewrote, so this measures how much law was under "
                "revision, not how much of it changed. It uses the law's current "
                "article count: exact for recent years, anachronistic for old ones."
            ),
        },
        "by_year": out,
    }


# ─── Writers ──────────────────────────────────────────────────────────────────

# Columns of the two published tables.  The event stream is written as arrays
# rather than objects because the keys are the bulk of it: at 140k events a
# repeated key like "source" costs more than every value it ever labels.
EVENT_COLUMNS = ("date", "law", "event", "seq", "source", "delta")
LAW_COLUMNS = ("law", "scope", "canton", "domain", "type", "chars", "articles",
               "latest")
EVENT_KINDS = ("publication", "revision")

# Every key build_events() can put on a record, split by where it belongs in
# the published form.  A record carrying anything else is a new field that
# would be silently dropped, so the writer refuses instead.
_EVENT_FIELDS = {"date", "law", "event", "seq", "source", "delta"}
_LAW_FIELDS = {"scope", "canton", "domain", "type", "size_current"}


def law_dimension(events: list[dict]) -> dict:
    """The law table: the attributes that belong to a law, not to its events.

    ``scope``, ``canton``, ``domain``, ``type`` and ``size_current`` are
    properties of the law itself — they are identical on all 4.1 events the
    average law contributes, and writing them per event was 12 of the stream's
    26 MB.  They move here, one row per law, joined back on the law key.

    ``size_current`` in particular is the law's size *today*, so there is only
    ever one value of it per law; repeating it was never anything but repetition.

    The denormalised form marked the law's current version implicitly, by
    hanging ``size_current`` on its most recent event and no other.  That is
    real information — which event produced the text the law has today — and
    a year file cannot recover it alone, so it becomes the ``latest`` column
    rather than being lost with the repetition.  It also stops the size being
    summed per event: one law, one row, one size.
    """
    laws: dict[str, dict] = {}
    for e in events:
        row = laws.setdefault(e["law"], {})
        for k in _LAW_FIELDS:
            if k in e:
                row[k] = e[k]
        if e["date"] > row.get("latest", ""):
            row["latest"] = e["date"]

    def _book(field: str) -> list[str]:
        return sorted({r[field] for r in laws.values() if r.get(field)})

    scopes, cantons = _book("scope"), _book("canton")
    domains, types = _book("domain"), _book("type")
    idx = {f: {v: i for i, v in enumerate(b)} for f, b in
           (("scope", scopes), ("canton", cantons), ("domain", domains), ("type", types))}

    def _code(row: dict, field: str) -> int | None:
        v = row.get(field)
        return idx[field][v] if v else None

    rows = []
    for key in sorted(laws):
        r = laws[key]
        size = r.get("size_current") or {}
        rows.append([key, _code(r, "scope"), _code(r, "canton"),
                     _code(r, "domain"), _code(r, "type"),
                     size.get("chars"), size.get("articles"), r.get("latest")])
    return {"count": len(rows), "counting_unit": "law",
            "columns": list(LAW_COLUMNS),
            "codebooks": {"scope": scopes, "canton": cantons,
                          "domain": domains, "type": types},
            "rows": rows}


def _event_rows(recs: list[dict], sources: list[str]) -> list[list]:
    """Records to positional rows, trailing absent values omitted.

    93% of events carry no ``delta`` (a text diff needs two published versions
    of the same law).  Writing ``null`` in that slot 130k times costs half a
    megabyte to say nothing, so a short row means "the rest is absent" — the
    same reason build_events() omits empty keys rather than nulling them.
    """
    src = {s: i for i, s in enumerate(sources)}
    kind = {k: i for i, k in enumerate(EVENT_KINDS)}
    rows = []
    for e in recs:
        row = [e["date"], e["law"], kind[e["event"]], e["seq"], src[e["source"]]]
        d = e.get("delta")
        if d:
            row.append([d["lines_added"], d["lines_removed"]])
        rows.append(row)
    return rows


def write_events(events: list[dict], output_dir: str | Path) -> dict:
    """Per-year event files + the law table they join to + index.

    Split rather than denormalised: the year files hold what varies per event
    (when, which law, publication or revision, how much text moved) and
    ``laws.json`` holds what is constant per law.  Both are plain JSON with a
    ``columns`` header and inline ``codebooks``, so a reader needs no schema
    to decode them and the join key stays the law's real register number.
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    unknown = {k for e in events for k in e} - _EVENT_FIELDS - _LAW_FIELDS
    if unknown:
        raise ValueError(
            f"event field(s) {sorted(unknown)} have no column and would be "
            f"dropped; add them to EVENT_COLUMNS or LAW_COLUMNS")

    laws = law_dimension(events)
    (out / "laws.json").write_text(
        json.dumps(laws, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")

    sources = sorted({e["source"] for e in events})
    by_year: dict[str, list[dict]] = defaultdict(list)
    for r in events:
        by_year[r["date"][:4]].append(r)

    for year, recs in by_year.items():
        recs.sort(key=lambda r: (r["date"], r["law"]))
        payload = {"date_prefix": year, "count": len(recs),
                   "counting_unit": "legal_event",
                   "default_confidence": "authoritative",
                   "laws": "laws.json",
                   "columns": list(EVENT_COLUMNS),
                   "codebooks": {"event": list(EVENT_KINDS), "source": sources},
                   "rows": _event_rows(recs, sources)}
        (out / f"{year}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8")

    years = sorted(by_year)
    index = {
        "years": years,
        "total_events": len(events),
        "total_laws": laws["count"],
        "earliest_year": years[0] if years else None,
        "latest_year": years[-1] if years else None,
        "format": "columnar",
        "decoding": (
            "Each year file has `columns`, `codebooks` and `rows`. A row is "
            "positional against `columns`; a row shorter than `columns` has "
            "its remaining fields absent. Integer values of a column named in "
            "`codebooks` index that codebook. Join `law` to rows in laws.json "
            "for the law's scope, canton, domain and type. `chars`/`articles` "
            "there are the law's size today, held once per law rather than per "
            "event so they cannot be summed twice; `latest` is the date of the "
            "event that produced that text."),
    }
    (out / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Wrote %d year files (%d events, %d laws) to %s",
                len(years), len(events), laws["count"], out)
    return index


def write_json(payload: dict, path: str | Path) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return p
