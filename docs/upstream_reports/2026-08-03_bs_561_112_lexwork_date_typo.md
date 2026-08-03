# Upstream data-quality report: BS 561.112 — version date "1019-02-01" (LexWork API)

*Draft prepared 2026-08-03 by the Swiss Law Collection pipeline
(swiss-law-as-source.github.io). Ready to send; nothing has been submitted yet.*

## Affected record

- **Canton / number**: Basel-Stadt, systematic number **561.112**
- **Law**: "Zusatzvereinbarung zur Interkantonalen Vereinbarung über die Aufsicht
  sowie …" (intercantonal agreement supplement)
- **Field**: version list served by the LexWork API (`version_dates_source:
  lexwork_api` in our frontmatter)

## The defect

The version history returned by the API contains:

```yaml
version_dates:
- '1019-02-01'
- '2019-02-01'
```

`1019-02-01` is evidently a century typo for **2019-02-01** (both entries otherwise
describe the same version). Year 1019 predates any Swiss legal collection by roughly
250 years (the oldest genuine intercantonal entries in LexFind date from 1562).

## Impact

Any consumer taking `min(version_dates)` as the earliest evidence of the act's
existence places this law in the year 1019. In our statistics this produced a bogus
"1019" year bucket until we introduced a plausibility floor (dates before 1400 are
treated as unknown; see
`api/v1/quality/methodology_changelog.json` on swiss-law-as-source.github.io).
LexFind also serves `1000-01-01` as an "unknown date" placeholder on 348 records
(mostly BE 669.x) — distinct issue, but the same floor covers it; a machine-readable
"date unknown" marker instead of a sentinel date would help all consumers.

## Suggested fix

Correct the version date `1019-02-01` → `2019-02-01` for BS 561.112 in the LexWork
database (and, if feasible, add an input validation rejecting pre-1500 dates).

## Where to report

- LexFind / Institut für Föderalismus, Universität Freiburg — contact via
  https://www.lexfind.ch (the BS collection is served through the LexWork portal).
- Kanton Basel-Stadt, Gesetzessammlung (www.gesetzessammlung.bs.ch) — publisher of
  the underlying record.

## Verification steps for the recipient

1. Query the LexWork API for BS 561.112's version list.
2. Observe the `1019-02-01` entry alongside `2019-02-01`.
3. Cross-check the official publication of the Zusatzvereinbarung: the version in
   question entered into force on 2019-02-01.
