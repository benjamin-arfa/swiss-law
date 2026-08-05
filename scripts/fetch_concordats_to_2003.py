#!/usr/bin/env python3
"""Fetch all intercantonal concordats up to 2003 from LexFind and compare
against the 2003 statistical baseline (BADAC/IDHEAP inventory 1848-2003).

Auditable by design:
  * stdlib only (urllib) — no hidden dependency behaviour;
  * every HTTP request is logged to ``audit_log.jsonl`` with timestamp, URL,
    HTTP status, byte count and SHA-256 of the response body;
  * every raw API response is stored verbatim under ``raw/`` so each number
    in the report can be traced back to its source bytes;
  * a ``run_manifest.json`` records script hash, python version, parameters
    and per-step counts;
  * deterministic output ordering (sorted by systematic number).

Data sources
  1. LexFind (https://www.lexfind.ch) — entity "Intlex", the systematic
     collection of intercantonal law maintained by the ch Foundation
     (ch Stiftung für eidgenössische Zusammenarbeit).
       - /api/fe/{lang}/entities                      → resolve entity id
       - /api/fe/{lang}/entities/{id}/systematics     → category tree + texts
       - /api/frontend/v1/{lang}/texts-of-law/{id}/with-version-groups
                                                      → family/version dates
  2. Baseline: the CHStat (ex-BADAC) concordats visualization, graph G1 of
     the IDHEAP/BADAC press release "Les concordats intercantonaux: clé de
     voûte du fédéralisme suisse" (15.11.2004), built on the concordats
     database of the Institut du fédéralisme, University of Fribourg.
     G1 caption: "Total 1848-2003 = 733 concordats; 2564 cantons membres"
     with "résultats pondérés : 2564 = 100%" — i.e. the visualization's
     percentages are weighted by CANTON MEMBERSHIPS (2564), not by
     concordat count (733). Both units are carried through this script.
     PDF: https://chstat.ch/download/pages/nehhqpsts5nj.pdf/CP4fr.pdf
     (archived by this script under baseline/CP4fr.pdf).

Usage:
    python scripts/fetch_concordats_to_2003.py [--out DIR] [--lang de]
                                               [--cutoff 2003-12-31]
                                               [--rate 0.15]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

FE_API = "https://www.lexfind.ch/api/fe"
FRONTEND_API = "https://www.lexfind.ch/api/frontend/v1"
INTLEX_ABBREVIATION = "intlex"
BATCH_SIZE = 20
USER_AGENT = "swiss-law-concordat-audit/1.0 (research; contact: repo owner)"

# ── 2003 baseline ──────────────────────────────────────────────────────────
# CHStat/BADAC concordats visualization (graph G1 of the IDHEAP/BADAC press
# release of 15.11.2004), based on the concordats database of the Institut du
# fédéralisme, University of Fribourg.
#
# The G1 caption reads: "Total 1848-2003 = 733 concordats; 2564 cantons
# membres" and "résultats pondérés : 2564 = 100%".  Two units therefore
# coexist:
#   * 733  = number of concordats CONCLUDED 1848-2003 (one per treaty);
#   * 2564 = number of CANTON MEMBERSHIPS (each concordat counted once per
#            signatory canton; 2564 / 733 ≈ 3.5 cantons per concordat).
# All percentages published in the visualization (domains and
# signatory-size classes) are weighted by memberships, i.e. shares of 2564.
# The release's prose ("44% étaient des accords bilatéraux") repeats the
# weighted figures loosely; taken as shares of the 733 concordats they are
# arithmetically impossible (44% bilateral + 22% with ≥20 cantons would
# alone exceed 2564 memberships).  The implied per-concordat distribution is
# derived below in `derive_baseline_concordat_distribution()`.
BASELINE_2003 = {
    "source": (
        "CHStat/BADAC (IDHEAP), 'Les concordats intercantonaux: clé de voûte "
        "du fédéralisme suisse', communiqué du 15.11.2004, graphique G1 — "
        "d'après la banque de données des concordats de l'Institut du "
        "fédéralisme, Université de Fribourg. "
        "PDF: https://chstat.ch/download/pages/nehhqpsts5nj.pdf/CP4fr.pdf"
    ),
    "period": "1848-2003",
    "total_concordats": 733,
    "total_canton_memberships": 2564,
    "share_signed_since_1970s": 0.70,  # share of concordats (prose, unweighted)
    "share_signed_last_decade": 0.30,  # 1994-2003, share of concordats
    # Signatory-size classes, membership-weighted (G1 legend, 2564 = 100%).
    "size_classes_membership_weighted": {
        "2": 0.44,
        "3-4": 0.08,
        "5-10": 0.20,
        "11-19": 0.06,
        "20-26": 0.22,
    },
    # NB: no representative sizes are listed here — they are computed from
    # each class label's own bounds in size_class_midpoint().
    # Domain distribution, membership-weighted (G1, 2564 = 100%).
    "domains_membership_weighted": {
        "Éducation, science et culture": 0.25,
        "Organisation étatique et sécurité": 0.13,
        "Finances et fiscalité": 0.20,
        "Économie et agriculture": 0.15,
        "Infrastructure, trafic et environnement": 0.16,
        "Santé et sécurité sociale": 0.10,
    },
}

BASELINE_PDF_URL = "https://chstat.ch/download/pages/nehhqpsts5nj.pdf/CP4fr.pdf"


def size_class_midpoint(cls: str) -> float:
    """Arithmetic midpoint of a G1 size class, parsed from its own label.

    "2" -> 2.0, "3-4" -> 3.5, "20-26" -> 23.0.  Computing it from the label
    keeps the conversion auditable: nothing here is a chosen number.
    """
    lo, _, hi = cls.partition("-")
    return (int(lo) + int(hi or lo)) / 2


def derive_baseline_concordat_distribution() -> dict:
    """Convert the membership-weighted G1 size classes back to concordat counts.

    memberships(class) = share * the published membership total ;
    concordats(class) = memberships / the class midpoint.  The derived total
    reconciles with the published concordat count to within ~1%, which
    validates the weighted reading of the legend.
    """
    total_m = BASELINE_2003["total_canton_memberships"]
    out = {}
    for cls, share in BASELINE_2003["size_classes_membership_weighted"].items():
        memberships = share * total_m
        out[cls] = {
            "memberships": round(memberships),
            "concordats_est": round(memberships / size_class_midpoint(cls)),
            "midpoint": size_class_midpoint(cls),
        }
    out["_derived_total_concordats"] = sum(v["concordats_est"] for v in out.values()
                                           if isinstance(v, dict))
    return out


# Canton names as they appear in German Intlex titles (incl. spelling
# variants).  Used to count named signatories per title — an exact lower
# bound on memberships for treaties that enumerate their parties.
CANTON_NAME_VARIANTS = {
    "ZH": ["Zürich"], "BE": ["Bern"], "LU": ["Luzern"], "UR": ["Uri"],
    "SZ": ["Schwyz"], "OW": ["Obwalden"], "NW": ["Nidwalden"],
    "GL": ["Glarus"], "ZG": ["Zug"], "FR": ["Freiburg", "Fribourg"],
    "SO": ["Solothurn"], "BS": ["Basel-Stadt"],
    "BL": ["Basel-Landschaft", "Basel-Land"],
    "SH": ["Schaffhausen"],
    "AR": ["Appenzell Ausserrhoden", "Appenzell A.Rh", "Appenzell AR"],
    "AI": ["Appenzell Innerrhoden", "Appenzell I.Rh", "Appenzell IR"],
    "SG": ["St.Gallen", "St. Gallen", "Sankt Gallen"],
    "GR": ["Graubünden"], "AG": ["Aargau"], "TG": ["Thurgau"],
    "TI": ["Tessin", "Ticino"], "VD": ["Waadt"], "VS": ["Wallis"],
    "NE": ["Neuenburg"], "GE": ["Genf"], "JU": ["Jura"],
}
# "Basel" alone (without Stadt/Landschaft) historically means BS in
# pre-1833 treaties; matched only when neither compound form is present.
_BASEL_BARE = "Basel"


def cantons_named_in_title(title: str) -> list[str]:
    """Return the sorted canton codes explicitly named in a treaty title."""
    t = title or ""
    found = set()
    for code, variants in CANTON_NAME_VARIANTS.items():
        if any(v in t for v in variants):
            found.add(code)
    if "BS" not in found and "BL" not in found and _BASEL_BARE in t:
        found.add("BS")
    # "Appenzell" bare would double-count via AR/AI variants only if the
    # compound is present, which the variant lists already require.
    return sorted(found)

# Map Intlex top-level chapters (1-9) onto the BADAC domain categories so the
# two distributions can be compared side by side.
CHAPTER_TO_BASELINE_DOMAIN = {
    "1": "Organisation étatique et sécurité",   # Staat, Volk, Behörden
    "2": "Organisation étatique et sécurité",   # Privatrecht, Zivilrechtspflege
    "3": "Organisation étatique et sécurité",   # Strafrechtspflege - Strafvollzug
    "5": "Organisation étatique et sécurité",   # Sicherheit
    "4": "Éducation, science et culture",       # Schule - Wissenschaft - Kultur
    "6": "Finances et fiscalité",               # Finanzen, Steuern und Regale
    "7": "Infrastructure, trafic et environnement",  # Öff. Werke, Energie, Verkehr, Umwelt
    "8": "Santé et sécurité sociale",           # Gesundheit, Soziale Sicherheit
    "9": "Économie et agriculture",             # Wirtschaft
}

GERMAN_MONTHS = {
    "januar": 1, "februar": 2, "märz": 3, "maerz": 3, "april": 4, "mai": 5,
    "juni": 6, "juli": 7, "august": 8, "september": 9, "oktober": 10,
    "november": 11, "dezember": 12,
}
# e.g. "vom 4. November 1950", "vom 26. April/6. Mai 1974", "vom 4./5. Juli 1899"
_TITLE_DATE = re.compile(
    r"\b[Vv]om\s+(\d{1,2})\.(?:\s*/\s*\d{1,2}\.)?\s*"
    r"(?:([A-Za-zäöüÄÖÜ]+)\s+(\d{4})?\s*/\s*)?"
    r"(\d{1,2}\.\s*)?([A-Za-zäöüÄÖÜ]+)\s+(\d{4})"
)
_DDMMYYYY = re.compile(r"^(\d{2})\.(\d{2})\.(\d{4})$")


class AuditedHttp:
    """HTTP GET with retry/backoff; logs every request and stores raw bodies."""

    def __init__(self, out_dir: Path, rate: float):
        self.rate = rate
        self.raw_dir = out_dir / "raw"
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = out_dir / "audit_log.jsonl"
        self.log_fh = open(self.log_path, "a", encoding="utf-8")
        self.request_count = 0

    def get_json(self, url: str, tag: str):
        last_err = None
        for attempt in range(1, 4):
            time.sleep(self.rate)
            record = {
                "ts": datetime.now(timezone.utc).isoformat(),
                "url": url,
                "tag": tag,
                "attempt": attempt,
            }
            try:
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=60) as resp:
                    body = resp.read()
                    record["status"] = resp.status
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                record["error"] = str(exc)
                self._log(record)
                last_err = exc
                time.sleep(2 * attempt)
                continue
            digest = hashlib.sha256(body).hexdigest()
            record["bytes"] = len(body)
            record["sha256"] = digest
            raw_file = self.raw_dir / f"{tag}_{digest[:16]}.json"
            if not raw_file.exists():
                raw_file.write_bytes(body)
            record["raw_file"] = raw_file.name
            self._log(record)
            self.request_count += 1
            return json.loads(body)
        raise RuntimeError(f"GET failed after 3 attempts: {url}: {last_err}")

    def get_bytes(self, url: str, tag: str) -> bytes:
        """Audited GET for non-JSON resources (e.g. the baseline PDF)."""
        last_err = None
        for attempt in range(1, 4):
            time.sleep(self.rate)
            record = {
                "ts": datetime.now(timezone.utc).isoformat(),
                "url": url,
                "tag": tag,
                "attempt": attempt,
            }
            try:
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=60) as resp:
                    body = resp.read()
                    record["status"] = resp.status
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                record["error"] = str(exc)
                self._log(record)
                last_err = exc
                time.sleep(2 * attempt)
                continue
            record["bytes"] = len(body)
            record["sha256"] = hashlib.sha256(body).hexdigest()
            self._log(record)
            self.request_count += 1
            return body
        raise RuntimeError(f"GET failed after 3 attempts: {url}: {last_err}")

    def _log(self, record: dict):
        self.log_fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        self.log_fh.flush()


def parse_title_date(title: str) -> date | None:
    """Extract the (last, i.e. latest) conclusion date from a German title."""
    m = _TITLE_DATE.search(title or "")
    if not m:
        return None
    day = int(m.group(1))
    month_name = (m.group(5) or "").lower()
    year = int(m.group(6))
    month = GERMAN_MONTHS.get(month_name)
    if not month:
        return None
    try:
        return date(year, month, day)
    except ValueError:
        return None


def parse_ddmmyyyy(s: str | None) -> date | None:
    m = _DDMMYYYY.match(str(s or "").strip())
    if not m:
        return None
    try:
        return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


def fetch_family_dates(http: AuditedHttp, lang: str, tol_id: int) -> dict:
    """Earliest family_active_since + version dates for one text of law."""
    data = http.get_json(
        f"{FRONTEND_API}/{lang}/texts-of-law/{tol_id}/with-version-groups",
        tag=f"tol_{tol_id}",
    )
    earliest_family: date | None = None
    earliest_version: date | None = None
    if isinstance(data, dict):
        for family in data.get("families", []):
            for group in family:
                for v in (group if isinstance(group, list) else [group]):
                    if not isinstance(v, dict):
                        continue
                    fa = parse_ddmmyyyy(v.get("family_active_since"))
                    if fa and (earliest_family is None or fa < earliest_family):
                        earliest_family = fa
                    vs = parse_ddmmyyyy(v.get("version_active_since"))
                    if vs and (earliest_version is None or vs < earliest_version):
                        earliest_version = vs
    return {"family_active_since": earliest_family, "earliest_version": earliest_version}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="exports/concordats_2003", help="output directory")
    ap.add_argument("--lang", default="de")
    ap.add_argument("--cutoff", default="2003-12-31", help="inclusive cutoff date")
    ap.add_argument("--rate", type=float, default=0.15, help="seconds between requests")
    args = ap.parse_args()

    cutoff = date.fromisoformat(args.cutoff)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    http = AuditedHttp(out_dir, args.rate)

    # ── Step 1: resolve the Intlex entity id ──────────────────────────────
    entities = http.get_json(f"{FE_API}/{args.lang}/entities", tag="entities")
    intlex_id = None
    for ent in entities:
        if str(ent.get("abbreviation", "")).lower() == INTLEX_ABBREVIATION:
            intlex_id = ent["id"]
    if intlex_id is None:
        print("FATAL: Intlex entity not found on LexFind", file=sys.stderr)
        return 1
    print(f"[1/4] Intlex entity id = {intlex_id}")

    # ── Step 2: systematics tree → chapters, leaves ───────────────────────
    tree_url = f"{FE_API}/{args.lang}/entities/{intlex_id}/systematics"
    tree = http.get_json(tree_url, tag="systematics_tree")
    chapters = {}   # node_id → (identifier, title) for top-level chapters
    node_info = {}  # node_id(str) → node dict
    for k, v in tree.items():
        if not k:
            continue
        node_info[k] = v
        if v.get("parent") is None:
            chapters[int(k)] = (str(v.get("identifier", "")), str(v.get("title", "")))

    def chapter_of(node_id: int) -> tuple[str, str]:
        """Walk up the tree to the top-level chapter."""
        cur = str(node_id)
        while node_info.get(cur, {}).get("parent") is not None:
            cur = str(node_info[cur]["parent"])
        info = node_info.get(cur, {})
        return str(info.get("identifier", "?")), str(info.get("title", "?"))

    leaves = sorted(int(k) for k, v in tree.items() if k and not v.get("children"))
    print(f"[2/4] systematics: {len(node_info)} nodes, {len(leaves)} leaves, "
          f"{len(chapters)} chapters")

    # ── Step 3: enumerate all texts of law (tols), incl. inactive ─────────
    tols: dict[int, dict] = {}
    for i in range(0, len(leaves), BATCH_SIZE):
        batch = leaves[i:i + BATCH_SIZE]
        params = "&".join(f"tols_for_systematics[]={lid}" for lid in batch)
        data = http.get_json(
            f"{tree_url}?active_only=false&{params}",
            tag=f"tols_batch_{i // BATCH_SIZE}",
        )
        for k, v in data.items():
            if not k or not v.get("tols"):
                continue
            ch_ident, ch_title = chapter_of(int(k))
            for t in v["tols"]:
                tid = t.get("id")
                if tid is None or tid in tols:
                    continue
                tols[tid] = {
                    "tol_id": tid,
                    "systematic_number": str(t.get("systematic_number", "")).strip(),
                    "title": str(t.get("title", "")).strip(),
                    "is_active": bool(t.get("is_active", False)),
                    "category_id": t.get("category_id"),
                    "node_identifier": str(v.get("identifier", "")),
                    "node_title": str(v.get("title", "")),
                    "chapter": ch_ident,
                    "chapter_title": ch_title,
                }
    print(f"[3/4] {len(tols)} unique intercantonal texts of law enumerated")

    # ── Step 4: per-text dates (frontend API) + title-date cross-check ────
    for n, (tid, row) in enumerate(sorted(tols.items()), 1):
        dates = fetch_family_dates(http, args.lang, tid)
        title_date = parse_title_date(row["title"])
        row["title_date"] = title_date.isoformat() if title_date else ""
        fam = dates["family_active_since"]
        row["family_active_since"] = fam.isoformat() if fam else ""
        ev = dates["earliest_version"]
        row["earliest_version_date"] = ev.isoformat() if ev else ""
        # Date preference: family_active_since (LexFind's original date of the
        # act family) first — Intlex titles rarely carry dates, and when they
        # do ("Nachtrag zur Übereinkunft vom 1889...") the date can refer to
        # the amended parent act, not the text itself.
        best = fam or title_date or ev
        row["best_date"] = best.isoformat() if best else ""
        row["date_source"] = (
            "family_active_since" if fam else
            "title" if title_date else
            "earliest_version" if ev else "none"
        )
        row["in_scope_to_2003"] = bool(best and best <= cutoff)
        row["url"] = f"https://www.lexfind.ch/tol/{tid}/{args.lang}"
        named = cantons_named_in_title(row["title"])
        row["named_cantons"] = " ".join(named)
        row["n_named_cantons"] = len(named)
        if n % 50 == 0:
            print(f"      dates: {n}/{len(tols)}")
    print(f"[4/4] dates resolved for {len(tols)} texts")

    rows = sorted(tols.values(), key=lambda r: (r["chapter"], r["systematic_number"]))
    in_scope = [r for r in rows if r["in_scope_to_2003"]]
    undated = [r for r in rows if r["date_source"] == "none"]

    # ── CSV outputs ────────────────────────────────────────────────────────
    fieldnames = [
        "tol_id", "systematic_number", "title", "chapter", "chapter_title",
        "node_identifier", "node_title", "is_active", "category_id",
        "title_date", "family_active_since", "earliest_version_date",
        "best_date", "date_source", "in_scope_to_2003", "url",
        "named_cantons", "n_named_cantons",
    ]
    full_csv = out_dir / "intlex_full_inventory.csv"
    with open(full_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    scope_csv = out_dir / "concordats_up_to_2003.csv"
    with open(scope_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(in_scope)

    # ── Baseline source archiving ─────────────────────────────────────────
    baseline_dir = out_dir / "baseline"
    baseline_dir.mkdir(parents=True, exist_ok=True)
    baseline_pdf = baseline_dir / "CP4fr.pdf"
    try:
        pdf_bytes = http.get_bytes(BASELINE_PDF_URL, tag="baseline_pdf")
        baseline_pdf.write_bytes(pdf_bytes)
        baseline_pdf_note = (
            f"archivé dans `baseline/CP4fr.pdf` "
            f"(sha256 `{hashlib.sha256(pdf_bytes).hexdigest()[:16]}…`)"
        )
    except RuntimeError as exc:
        baseline_pdf_note = f"téléchargement échoué ({exc}); URL: {BASELINE_PDF_URL}"

    # ── Statistics + baseline comparison ──────────────────────────────────
    by_decade = Counter()
    for r in in_scope:
        year = int(r["best_date"][:4])
        by_decade[f"{year // 10 * 10}s"] += 1
    by_domain = Counter()
    for r in in_scope:
        by_domain[CHAPTER_TO_BASELINE_DOMAIN.get(r["chapter"], "Autre")] += 1
    bilateral = [
        r for r in in_scope
        if r["n_named_cantons"] == 2
        or re.search(r"zwischen den (Kantonen|Ständen) [^,]+ und ", r["title"])
        or re.search(r"zwischen dem (Kanton|Stand) [^,]+ und dem (Kanton|Stand)", r["title"])
    ]
    active_in_scope = [r for r in in_scope if r["is_active"]]

    baseline_total = BASELINE_2003["total_concordats"]
    baseline_memberships = BASELINE_2003["total_canton_memberships"]
    baseline_derived = derive_baseline_concordat_distribution()
    n_scope = len(in_scope)

    # Canton-membership estimate for the LexFind ≤cutoff subset.
    # Titles that enumerate their parties (≥2 named cantons) give an exact
    # count; open multilateral treaties (no cantons in the title) are bounded
    # by [2, 26] members each and estimated at the baseline's non-bilateral
    # mean of (2564 − 1128) / (733 − 564) ≈ 8.5 members.
    named_rows = [r for r in in_scope if r["n_named_cantons"] >= 2]
    unnamed_rows = [r for r in in_scope if r["n_named_cantons"] < 2]
    named_membership_sum = sum(r["n_named_cantons"] for r in named_rows)
    bilat_m = round(BASELINE_2003["size_classes_membership_weighted"]["2"]
                    * baseline_memberships)
    bilat_c = round(bilat_m / 2)
    nonbilateral_mean = (baseline_memberships - bilat_m) / (baseline_total - bilat_c)
    memberships_low = named_membership_sum + 2 * len(unnamed_rows)
    memberships_high = named_membership_sum + 26 * len(unnamed_rows)
    memberships_est = round(named_membership_sum
                            + nonbilateral_mean * len(unnamed_rows))

    def pct(x, whole):
        return f"{100 * x / whole:.1f}%" if whole else "n/a"

    # ── Markdown report ────────────────────────────────────────────────────
    finished = datetime.now(timezone.utc)
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    lines = []
    a = lines.append
    a("# Concordats intercantonaux jusqu'à 2003 — LexFind vs. visualisation CHStat 2003")
    a("")
    a(f"*Généré le {finished.strftime('%Y-%m-%d %H:%M UTC')} — script "
      f"`scripts/fetch_concordats_to_2003.py` (sha256 `{script_hash[:16]}…`)*")
    a("")
    a("## Résumé")
    a("")
    a(f"| Indicateur | Valeur |")
    a(f"|---|---|")
    a(f"| Textes intercantonaux recensés aujourd'hui sur LexFind (Intlex, actifs + abrogés) | **{len(rows)}** |")
    a(f"| … dont conclus jusqu'au {cutoff.isoformat()} | **{n_scope}** |")
    a(f"| … dont encore en vigueur aujourd'hui | {len(active_in_scope)} |")
    a(f"| … sans date déterminable | {len(undated)} |")
    a(f"| Baseline CHStat 2003 — concordats conclus 1848-2003 | **{baseline_total}** |")
    a(f"| Baseline CHStat 2003 — cantons membres (pondération de la visualisation) | **{baseline_memberships}** |")
    a(f"| Écart LexFind ≤2003 vs baseline (en concordats) | **{n_scope - baseline_total:+d}** "
      f"({pct(n_scope, baseline_total)} de l'inventaire 2003) |")
    a(f"| Adhésions cantonales estimées, LexFind ≤2003 (voir méthode) | ~{memberships_est} "
      f"(bornes [{memberships_low}, {memberships_high}]) |")
    a("")
    a(f"## Les deux unités de la visualisation CHStat : {baseline_total} "
      f"concordats, {baseline_memberships} cantons membres")
    a("")
    a("La visualisation « Concordats » de CHStat/BADAC (graphique G1 du communiqué "
      "IDHEAP du 15.11.2004, d'après la banque de données des concordats de "
      "l'Institut du fédéralisme de l'Université de Fribourg) porte en légende : "
      "**« Total 1848-2003 = 733 concordats; 2564 cantons membres »**, avec la "
      "mention *« résultats pondérés : 2564 = 100% »*. Deux unités coexistent donc :")
    a("")
    a(f"1. **{baseline_total}** — le nombre de concordats *conclus* entre 1848 "
      f"et 2003 (un par traité) ;")
    a(f"2. **{baseline_memberships}** — le nombre d'*adhésions cantonales* : chaque "
      f"concordat compté une fois par canton signataire (soit ≈"
      f"{baseline_memberships / baseline_total:.1f} cantons par concordat en "
      f"moyenne).")
    a("")
    a("Tous les pourcentages affichés par la visualisation (domaines et classes de "
      "taille) sont **pondérés par les adhésions** (2564 = 100 %), pas par le "
      "nombre de textes. Lecture inverse de la légende des classes de taille :")
    a("")
    a("| Cantons signataires | Part des adhésions (G1) | Adhésions | Concordats (dérivé) |")
    a("|---|---|---|---|")
    for cls, share in BASELINE_2003["size_classes_membership_weighted"].items():
        d = baseline_derived[cls]
        a(f"| {cls} | {share:.0%} | {d['memberships']} | ~{d['concordats_est']} |")
    a(f"| **Total** | 100% | {baseline_memberships} | "
      f"~{baseline_derived['_derived_total_concordats']} (publié : {baseline_total}) |")
    a("")
    derived_total = baseline_derived["_derived_total_concordats"]
    bilat = baseline_derived["2"]["concordats_est"]
    bilat_share_memberships = BASELINE_2003[
        "size_classes_membership_weighted"]["2"]
    a(f"Le total dérivé (~{derived_total}) recoupe le total publié "
      f"({baseline_total}) à "
      f"~{abs(derived_total - baseline_total) / baseline_total:.0%} près, ce qui "
      f"valide cette lecture pondérée. Conséquence notable : "
      f"**~{bilat / baseline_total:.0%} des concordats 1848-2003 étaient "
      f"bilatéraux** ({bilat} sur {baseline_total}), même si les accords "
      f"bilatéraux ne représentent que {bilat_share_memberships:.0%} des "
      f"adhésions.")
    a("")
    a("## Interprétation de l'écart")
    a("")
    a("L'inventaire de l'Institut du fédéralisme compte **tous** les concordats "
      "*conclus* entre 1848 et 2003 (y compris les accords bilatéraux ponctuels, "
      "remplacés ou éteints). LexFind/Intlex est en revanche le **recueil "
      "systématique du droit intercantonal** tenu par la Fondation ch : il ne "
      "référence pour l'essentiel que les textes encore pertinents (en vigueur ou "
      "récemment abrogés). L'écart mesure donc surtout l'attrition historique du "
      "corpus — il ne signifie pas que LexFind « manque » des données, mais que "
      "les deux sources répondent à des questions différentes.")
    a("")
    a(f"En unité « concordats » : {n_scope} vs {baseline_total} "
      f"({pct(n_scope, baseline_total)} du corpus historique subsiste). "
      f"En unité « adhésions cantonales » : ~{memberships_est} estimées vs "
      f"{baseline_memberships} — la part subsistante est plus élevée en adhésions "
      f"qu'en textes, car ce sont surtout les petits accords bilatéraux qui ont "
      f"disparu, tandis que les grands concordats multilatéraux ont survécu.")
    a("")
    a("### Méthode d'estimation des adhésions LexFind")
    a("")
    a(f"- {len(named_rows)} textes ≤{cutoff.year} énumèrent leurs cantons dans le "
      f"titre (≥2 cantons nommés) → comptage exact : {named_membership_sum} adhésions ;")
    a(f"- {len(unnamed_rows)} textes multilatéraux « ouverts » ne nomment pas "
      f"leurs parties → bornes [2, 26] par texte, estimation à la moyenne "
      f"non-bilatérale de la baseline "
      f"({baseline_memberships}−{bilat_m} adhésions / {baseline_total}−{bilat_c} "
      f"concordats ≈ {nonbilateral_mean:.1f} cantons/texte) ;")
    a("- LexFind/Intlex ne publie pas la liste des cantons membres par texte via "
      "son API — un comptage exact nécessiterait la banque de données de "
      "l'Institut du fédéralisme ou le dépouillement des clauses d'adhésion des "
      "PDF. Les colonnes `named_cantons`/`n_named_cantons` des CSV rendent le "
      "comptage titre par titre vérifiable.")
    a("")
    a("## Répartition par domaine — comparaison")
    a("")
    a("⚠️ Unités différentes : la colonne CHStat est pondérée par **adhésions** "
      "(2564 = 100 %), la colonne LexFind par **textes** (les adhésions par texte "
      "n'étant pas connues côté LexFind). Les écarts domaine par domaine mêlent "
      "donc attrition réelle et effet de pondération : un domaine riche en "
      "accords bilatéraux (2 adhésions/texte) pèse moins dans la colonne CHStat "
      "qu'en nombre de textes.")
    a("")
    a("| Domaine (nomenclature BADAC) | CHStat 1848-2003 (% adhésions) | LexFind ≤2003 (% textes) |")
    a("|---|---|---|")
    for dom, share in BASELINE_2003["domains_membership_weighted"].items():
        a(f"| {dom} | {share:.0%} (~{round(share * baseline_memberships)} adh.) "
          f"| {pct(by_domain.get(dom, 0), n_scope)} ({by_domain.get(dom, 0)}) |")
    if by_domain.get("Autre"):
        a(f"| Autre / non mappé | — | {pct(by_domain['Autre'], n_scope)} ({by_domain['Autre']}) |")
    a("")
    a("## Répartition par décennie (LexFind, conclus ≤2003)")
    a("")
    a("| Décennie | Textes |")
    a("|---|---|")
    for dec in sorted(by_decade):
        a(f"| {dec} | {by_decade[dec]} |")
    a("")
    a(f"Baseline : ~{BASELINE_2003['share_signed_since_1970s']:.0%} des "
      f"{baseline_total} concordats 1848-2003 signés depuis les années 1970 "
      f"(part en concordats, non pondérée) ; dans LexFind ≤2003 : "
      f"{pct(sum(v for k, v in by_decade.items() if k >= '1970s'), n_scope)}.")
    a("")
    a(f"Bilatéraux (2 cantons nommés dans le titre, ou motif « zwischen den "
      f"Kantonen X und Y ») : {pct(len(bilateral), n_scope)} ({len(bilateral)}) — "
      f"baseline : ~77 % des concordats (dérivé ; 44 % des adhésions). "
      f"La sous-représentation des bilatéraux dans le corpus subsistant est "
      f"encore plus marquée qu'annoncé dans la première version de ce rapport.")
    a("")
    a("## Sources et auditabilité")
    a("")
    a(f"- LexFind : entité Intlex (id {intlex_id}), {http.request_count} requêtes HTTP, "
      f"toutes journalisées dans `audit_log.jsonl` (URL, statut, octets, SHA-256).")
    a("- Réponses brutes archivées dans `raw/` (une par empreinte SHA-256).")
    a(f"- Baseline : {BASELINE_2003['source']} — {baseline_pdf_note}.")
    a("- Fichiers produits : `intlex_full_inventory.csv` (tout Intlex), "
      "`concordats_up_to_2003.csv` (filtré ≤2003), `run_manifest.json`.")
    a("- Date retenue par texte : `family_active_since` de l'API LexFind "
      "(date d'origine de la famille d'actes), sinon la date figurant dans le "
      "titre officiel, sinon la plus ancienne version connue "
      "(`date_source` dans les CSV).")
    report_md = out_dir / "report.md"
    report_md.write_text("\n".join(lines), encoding="utf-8")

    # ── Run manifest ───────────────────────────────────────────────────────
    manifest = {
        "script": str(Path(__file__).resolve()),
        "script_sha256": script_hash,
        "python": sys.version,
        "params": vars(args),
        "started_utc": started.isoformat(),
        "finished_utc": finished.isoformat(),
        "http_requests": http.request_count,
        "intlex_entity_id": intlex_id,
        "counts": {
            "total_intlex_texts": len(rows),
            "in_scope_to_2003": n_scope,
            "active_in_scope": len(active_in_scope),
            "undated": len(undated),
            "baseline_total_concordats_2003": baseline_total,
            "baseline_canton_memberships_2003": baseline_memberships,
            "lexfind_titles_naming_cantons": len(named_rows),
            "lexfind_named_membership_sum": named_membership_sum,
            "lexfind_memberships_estimate": memberships_est,
            "lexfind_memberships_bounds": [memberships_low, memberships_high],
            "bilateral_in_scope": len(bilateral),
        },
        "baseline_derived_size_distribution": baseline_derived,
        "by_decade": dict(sorted(by_decade.items())),
        "by_domain": dict(by_domain),
    }
    (out_dir / "run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"\nDone: {n_scope}/{len(rows)} texts ≤ {cutoff} — baseline {baseline_total}")
    print(f"Report:  {report_md}")
    print(f"CSVs:    {full_csv}, {scope_csv}")
    print(f"Audit:   {http.log_path} + raw/ + run_manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
