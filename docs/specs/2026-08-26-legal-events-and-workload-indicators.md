# Spec — Legal event stream & judicial-workload indicators

- **Status:** proposal, for discussion with the Tribunal fédéral (TF)
- **Date:** 2026-08-26
- **Author:** Benjamin Arfa
- **Repos touched:** `swiss-law` (pipeline, stats), `swiss-law-as-source` (dashboard, API)

## 1. Context

Our work was presented at the TF on 2026-08-18; first reactions are positive. The TF
is doing comparable work on **FindLex** data, to measure (a) the court's own workload
and (b) the relationship with the cantons for cases that reach the TF on appeal.

Two questions came out of that discussion, and one requirement came out of ours:

| # | Question | Origin |
|---|----------|--------|
| Q1 | How do we build **workload-estimation indicators**? Is document size (KB) a defensible proxy? | TF |
| Q2 | How do we account for **legislative change over time** — frequent revisions are what actually makes a judge's work laborious? | TF |
| R1 | The corpus must be countable **per publication and per revision**, not per unique law — and the dashboard trend bar chart must show both. | swiss-law |

R1 is the precondition for Q2, and Q2 is where the honest answer to Q1 lives: a judge's
burden is not driven by how many laws exist, but by how often the applicable ones move
underneath them, and by how much text moves each time.

## 2. Current state

Facts measured on the working tree on 2026-08-26 (full scan of `ch/**/*.md`):

| Quantity | Value |
|---|---|
| Law files (one per law × language) | 70,370 |
| Distinct laws (deduplicated across languages) | 34,404 |
| — federal | 9,045 |
| — cantonal | 25,359 |
| Distinct `(law, date)` pairs already in frontmatter | 129,103 |
| — federal | 45,700 (5.05 per law) |
| — cantonal | 83,403 (3.29 per law) |
| Laws with ≥ 2 recorded dates | 23,061 (67.0 %) |
| Commits in the repo | 60,384 |

**The revision history already exists.** Every law file carries `version_date` (the
current consolidated version) plus a `version_dates:` list (all known in-force dates),
back-filled by `src/legalize_ch/date_enricher.py`. For federal law, each consolidated
version is additionally a **separate backdated git commit**, so the text of every past
version is recoverable — not just its date.

**But nothing downstream counts it.** `generate_stats()` emits `by_year` with
`year_semantics: "enactment"` — one count per *law*, in the year it was first enacted.
`generate_publications()` groups by `(law_identity, year)` and explicitly documents
"each law appears once per year". The dashboard bar chart therefore shows, for 2025,
**350** — against **3,213** actual dated legal events in the same year. The published
trend understates legislative activity by roughly an order of magnitude, and by
construction cannot show revision pressure at all.

### 2.1 Known data-quality defect (blocks publication)

The `version_dates` values do **not** all mean the same thing. Provenance, counted per law:

| `version_dates_source` | Laws |
|---|---|
| `lexfind_family` | 13,149 |
| `git_history` | 8,908 |
| `lexwork_api` | 985 |
| *(none recorded)* | 11,362 |

`git_history` derives dates from this repo's own commit log. That is sound for
backdated consolidation commits, but it also swept up **bulk metadata commits**. The
signature is unmistakable: 7,444 of 9,045 federal laws (82 %) carry a date in 2026, and
at file level the 2026 dates concentrate in 2026-06 and 2026-07 — the enrichment
window, e.g. commit `39c6d8e1` ("data: enactment dates + version histories + inferred
domains for all laws", 2026-07-27), which changed frontmatter only and is not a legal
event. Total 2026 events come out at 14,432 (12,396 federal) versus a genuine baseline
of roughly 800–1,000 federal events per year.

**Publishing the event series before this is filtered would put a fabricated 15× spike
in front of the TF.** Fixing it is phase 1, not a follow-up.

## 3. Proposed model — the legal event stream

One record per `(law, date)`, replacing "one record per law" as the unit of the trend.

```json
{
  "date": "2025-01-01",
  "law": "CH/220",
  "scope": "federal",
  "canton": null,
  "event": "revision",
  "seq": 47,
  "domain": "2 – Privatrecht",
  "type": "Bundesgesetz",
  "delta": { "lines_added": 1908, "lines_removed": 96, "bytes": 71034 },
  "size_after": { "chars": 1204551, "articles": 1338 },
  "source": "fedlex_consolidation",
  "confidence": "authoritative"
}
```

Rules:

- `event = "publication"` for the earliest known date of a law (`seq = 0`), `"revision"`
  for every later date (`seq = 1…n`). A law with a single known date contributes exactly
  one publication record — so the new series is a strict superset of the current one and
  totals reconcile.
- The **key is `(law, date)`**, not `(law, date, language)`. Three language files of the
  same consolidation are one event. This is what keeps the new totals comparable to the
  existing 34,404-law figure.
- `confidence: "authoritative"` for Fedlex consolidations, LexWork/ZHLex API and the
  LexFind family; `"derived"` for anything reconstructed from git history. **The
  published chart uses authoritative events only**; derived events stay in the API,
  labelled, so the coverage gap is visible rather than hidden.
- Future-dated events exist and are legitimate (entry into force already scheduled —
  the corpus holds dates out to 2066). They are kept, and the chart cuts at the current
  year with a note.

### 3.1 Where per-revision size comes from

The corpus stores only the current text of each law, so size *per historical revision*
is not in the files. It **is** in git, for federal law: `git log --numstat` on a law file
returns, per backdated consolidation commit, the lines added and removed. Two real
examples on `ch/de/220.md` (Code des obligations):

- `2025-01-01` → +1908 / −96 lines — a substantive overhaul
- `2025-07-08` → +2 / −2 lines — a cosmetic touch-up

That distinction is the whole point. A count of revisions treats those two as equal;
a magnitude-weighted count does not. For cantonal law, where we lack a versioned text
history, `delta` is `null` and only the count-based indicators apply — a coverage
asymmetry that must be stated wherever both are charted.

## 4. Answering Q1 — workload indicators

Raw document size in KB is a **weak** indicator, and we should say so plainly to the TF
before it becomes the shared metric:

- KB tracks language, formatting and annex volume as much as legal substance.
- Our corpus is multilingual: the same act has three sizes.
- Size is a *stock*; workload from legislative change is a *flow*.

We already compute better stock measures than bytes — `count_articles()` in `stats.py`
yields a per-law article count, exposed alongside `chars` per language in the law index.
Proposed indicator set, cheapest first:

| Indicator | Definition | Unit |
|---|---|---|
| **Volume** | events in period | count |
| **Churn** | revision events in period ÷ laws in force | revisions/law/year |
| **Instability** | share of laws in a domain revised at least once in the period | % |
| **Half-life** | median time between consecutive revisions of the same law | months |
| **Magnitude** | lines changed per revision (federal only) | lines |
| **Weighted churn** | Σ lines changed ÷ laws in force | lines/law/year |
| **Stock** | articles, and chars, per law at a given date | count |

Half-life and instability are the two that speak directly to "révisions fréquentes qui
rendent le travail des juges laborieux", because they are per-law and time-normalised —
a domain where the median law changes every 14 months is a different working environment
from one where it changes every 9 years, independent of how large the corpus is.

The cross-level reference index (`cross_level_refs.json`: cantonal→federal and
federal→cantonal citations, already built) is the natural bridge to the TF's second
interest — cases climbing from cantonal to federal level. It is **out of scope here**
and noted only so we do not rebuild it: the event stream should carry the domain and
scope keys needed to join against it later.

## 5. Dashboard change

New chart section on `index.html`, above the existing cantonal explorer:

- Stacked bar per year: **publications** (first appearance) and **revisions**, colours
  from the existing palette in `assets/charts.js`.
- Toggles: scope (all / federal / cantonal), and a "count / magnitude" switch that
  swaps the y-axis from event count to lines changed (federal only, disabled otherwise).
- A methodology note in the same voice as the existing concordats note, stating the
  counting unit explicitly and that it **differs** from the enactment-year chart below.
  Both remain on the page; neither silently replaces the other.

The existing `by_year` chart and `year_semantics: "enactment"` are left untouched. Two
counting units, both labelled, is the honest presentation — and the reconciliation
(events ≥ laws, publications = laws with a known date) is checkable on the page.

## 6. Implementation plan

| Phase | Work | Files |
|---|---|---|
| 1 | **Provenance repair.** Classify every `git_history` date against the commit that produced it; drop bulk metadata commits (subject not matching `SR …: … (YYYY-MM-DD)`, or frontmatter-only diffs). Re-stamp `version_dates_source`. Verify the 2026 federal count lands near the ~800–1,000/yr baseline. | `date_enricher.py`, `scripts/` one-off |
| 2 | **Event builder.** `build_events(entries)` → the record in §3; `write_events()` → `docs/api/v1/events/{year}.json` + index, mirroring `generate_publications`/`write_publications`. | `stats.py` (new module `events.py` if it grows past ~200 lines) |
| 3 | **Magnitude backfill.** Single pass of `git log --numstat` over `ch/**/*.md`, keyed by the version date in the commit subject; cache to `data/state/revision_deltas.json` so the stats run stays fast. | new `revision_delta.py` |
| 4 | **Indicators.** Churn, instability, half-life, weighted churn — per year × scope × domain × canton, into `stats.json` under `events` and `api/v1/stats/indicators.json`. | `stats.py` |
| 5 | **Dashboard.** New chart section + option builder + methodology note; nav and layout via the existing `scripts/sync_site_nav.py` chrome. | `index.html`, `assets/charts.js` |
| 6 | **Docs & API.** `openapi.json`, `api.html`, `data.html` row for the new endpoints; `ARCHITECTURE.md` module map. | site repo |

Tests: `count_events` reconciliation (publications = laws with ≥1 authoritative date;
events ≥ laws), provenance filter unit tests with a fixture commit log, and a snapshot
test on one known law (SR 220) so the 2025 magnitudes above stay pinned.

## 7. Open questions — for the discussion with the TF

1. **Counting unit.** Does the TF count a multilingual act once, or once per language?
   FindLex may differ from us here; the totals will not reconcile unless we agree.
2. **What is a revision?** Is a consolidation that changes a single cross-reference a
   revision for workload purposes, or should a magnitude threshold apply?
3. **Denominator.** Churn per law in force needs a "laws in force at date *t*" series —
   we can build it from the event stream, but repeals are currently not modelled.
   Do we need them for the indicator to be defensible?
4. **KB or articles?** We propose articles + lines changed over KB, per §4. Does the TF
   have a reason to prefer bytes that we are not seeing?
5. **Cantonal magnitude.** Accepting count-only indicators for cantonal law, or invest
   in fetching versioned cantonal texts (large; LexWork exposes some version history)?

## 8. Non-goals

- Modelling repeals / abrogations (needed for question 3; separate spec).
- Any use of TF case data — this spec covers the legislation side only.
- Replacing the existing enactment-year chart.
