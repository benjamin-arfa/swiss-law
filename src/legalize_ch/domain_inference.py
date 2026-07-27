"""Infer the harmonized-taxonomy domain for laws LexFind leaves unclassified.

Two evidence sources, in priority order:
1. The canton's OWN systematic classification: every law sits in the canton
   tree; the top-level node's TITLE usually names the domain ("Schulwesen",
   "Instruction publique") — keyword-matching ~10 tree-node titles per
   canton is far safer than matching thousands of law titles.
2. The law's title keywords (multilingual).

Inferred values are written to a SEPARATE field ``global_category_inferred``
with ``inference_source`` — the LexFind field is never touched, so the data
stays verifiable. Aggregations combine source ?? inferred and report the
provenance split.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

from .categories import _load_tree

logger = logging.getLogger(__name__)

# Ordered: specific domains first; first match wins.
DOMAIN_KEYWORDS: list[tuple[str, str]] = [
    # 6 Finanzen
    (r"steuer|impôt|imposta|finanzausgleich|p[ée]r[ée]quation|finanzhaushalt|budget|abgabe[nr]?\b|tribut", "6"),
    # 8 Gesundheit / Arbeit / Soziales
    (r"gesundheit|spital|kranken|santé|h[ôo]pital|sanità|ospedal|sozial|social[ei]?\b|fürsorge|arbeitsgesetz|pflege|heim\b|assurance|versicherung|jugendhilfe|kindes", "8"),
    # 4 Bildung / Kultur
    (r"schul|bildung|universität|hochschule|gymnas|kindergarten|stipendien|kultur|museum|archiv|biblioth|[ée]cole|scolaire|enseignement|université|formation|culture|scuola|università|educazione|denkmal", "4"),
    # 5 Sicherheit
    (r"polizei|police|polizia|militär|militaire|zivilschutz|protection civile|feuerwehr|pompiers|pompieri|bevölkerungsschutz", "5"),
    # 3 Strafrecht
    (r"straf|pénal|penale|gefängnis|prison|vollzug", "3"),
    # 7 Bau / Umwelt / Verkehr / Energie
    (r"bau\b|baugesetz|raumplanung|richtplan|strass|verkehr|energie|[ée]nergie|wasser|gewässer|umwelt|abfall|wald|forst|natur|construction|am[ée]nagement|route|transport|eau[x]?\b|environnement|for[êe]t|d[ée]chets|costruzion|strade|acque|ambiente|foreste|rifiuti|energia", "7"),
    # 9 Wirtschaft
    (r"wirtschaft|landwirtschaft|gewerbe|handel|jagd|fischerei|tourismus|bank\b|[ée]conomie|agricole|agriculture|commerce|chasse|p[êe]che|economia|agricol|commercio|caccia|pesca|beherbergung", "9"),
    # 2 Zivilrecht
    (r"zivil|obligationen|grundbuch|notariat|erbschaft|registre foncier|notair|civile\b|notarile|personenrecht", "2"),
    # 1 Staat (general — keep last)
    (r"verfassung|constitution|costituzione|gemeinde|behörde|wahl|abstimmung|gericht|justiz|verwaltungs|bürgerrecht|datenschutz|kirche|commune\b|autorité|[ée]lection|tribunal|justice|[ée]ligibilit[ée]|comun[ei]\b|autorità|tribunale|giustizia|staat|organisation|informationsfreiheit", "1"),
]

_COMPILED = [(re.compile(p, re.IGNORECASE), code) for p, code in DOMAIN_KEYWORDS]


def classify_title(title: str) -> str | None:
    """Keyword-classify a title into a harmonized top-level domain code."""
    for rx, code in _COMPILED:
        if rx.search(title or ""):
            return code
    return None


def build_canton_topcode_map(trees_dir: str | Path, canton: str) -> dict[str, str]:
    """Map a canton's TOP-LEVEL systematics codes to harmonized domain codes.

    Classifies each top-level tree node's title (plus its direct children's
    titles as tie support). A node maps only when its own title matches OR
    a clear majority (>=60%) of its children agree on one domain.
    """
    tree = _load_tree(Path(trees_dir) / f"{canton.lower()}.json")
    mapping: dict[str, str] = {}
    for node in tree:
        ident = str(node.get("identifier", "")).strip()
        if not ident:
            continue
        code = classify_title(str(node.get("title", "")))
        if not code:
            votes: dict[str, int] = {}
            children = node.get("children", [])
            for ch in children:
                c = classify_title(str(ch.get("title", "")))
                if c:
                    votes[c] = votes.get(c, 0) + 1
            if votes:
                best, n = max(votes.items(), key=lambda kv: kv[1])
                if n >= max(2, 0.6 * sum(votes.values())):
                    code = best
        if code:
            mapping[ident] = code
    return mapping


def _canton_top_segment(systematic_number: str) -> str:
    """First classification segment of a cantonal systematic number."""
    sn = str(systematic_number).strip()
    m = re.match(r"^([A-Za-z]+|\d+)", sn)
    if not m:
        return ""
    seg = m.group(1)
    # numeric schemes usually classify by the first digit(s); tree top-level
    # identifiers are typically 1-3 chars — try full leading number then digit
    return seg


def infer_domain(fm: dict, topcode_map: dict[str, str]) -> tuple[str, str] | None:
    """Infer (top_level_code, source) for one law's frontmatter. None if unknown."""
    # 1. canton systematics position
    sysnum = str(fm.get("systematic_number", ""))
    seg = _canton_top_segment(sysnum)
    for cand in (seg, seg[:2], seg[:1]):
        if cand and cand in topcode_map:
            return topcode_map[cand], "canton_systematics"
    # systematic_category carries "code title" — classify its title part too
    sc = str(fm.get("systematic_category", ""))
    if sc:
        code = classify_title(sc.split(" ", 1)[1] if " " in sc else sc)
        if code:
            return code, "canton_systematics"
    # 2. title keywords
    code = classify_title(str(fm.get("title", "")))
    if code:
        return code, "title_keywords"
    return None


# ─── Instrument-type inference ────────────────────────────────────────────────
#
# LexFind files ~6,700 cantonal laws under the catch-all type "Anderes";
# in Swiss legal drafting the instrument is normally the title's leading
# word, so most are rule-classifiable. Rules map ONLY into LexFind's fixed
# 9-type taxonomy and carry ids so every inference is traceable.

_PARL = r"(grand conseil|grosser rat|kantonsrat|landrat|parlament|gran consiglio)"

TYPE_RULES: list[tuple[str, str, str]] = [
    # (rule_id, regex, canonical type)
    ("parl_beschluss", r"^\s*(kantonsrats|grossrats|landrats)beschluss|^\s*beschluss des (kantonsrat|grossen rat|landrat)", "Verordnung des Parlaments (Dekret)"),
    ("decret", r"^\s*(décret|decret\b|decreto)", "Verordnung des Parlaments (Dekret)"),
    ("arrete_parl", rf"^\s*arrêté.{{0,60}}{_PARL}", "Verordnung des Parlaments (Dekret)"),
    ("exec_beschluss", r"^\s*(regierungsrats|regierungs|staatsrats|standeskommissions)beschluss", "Verordnung"),
    ("arrete_exec", r"^\s*arrêté", "Verordnung"),
    ("ausfuehrung", r"^\s*ausführungsbestimmungen", "Verordnung"),
    ("verordnung", r"^\s*(verordnung|ordonnance|ordinanza)\b", "Verordnung"),
    ("reglement", r"^\s*(reglement|règlement|regolamento|geschäftsordnung)\b", "Reglement"),
    ("gesetz", r"^\s*(gesetz|loi|legge)\b", "Gesetz"),
    ("konkordat", r"^\s*(konkordat|interkantonale vereinbarung|accord intercantonal|concordat\b|concordato)", "Interkantonale Vereinbarung"),
    ("vereinb_ik", r"^\s*(vereinbarung|vertrag|convention|convenzione).{0,80}(interkantonal|zwischen den kantonen|entre les cantons|tra i cantoni)", "Interkantonale Vereinbarung"),
    ("vertrag_int", r"^\s*(vereinbarung|vertrag|convention|abkommen).{0,80}(ausländisch|république|bundesrepublik|fürstentum|königreich|frankreich|deutschland|italien|österreich|liechtenstein)", "Staatsvertrag"),
]

# Instruments that genuinely have no slot in the 9-type taxonomy —
# intentionally left as Other (documented residual).
_LEAVE_OTHER = re.compile(
    r"^\s*(richtlinien?|weisungen?|verfügung|entscheid|konzession|kreisschreiben|"
    r"gebührentarif|tarif\b|beitritt|entrée|statuten|statuts|direttive|istruzioni)",
    re.IGNORECASE)

_TYPE_RULES_COMPILED = [(rid, re.compile(rx, re.IGNORECASE), t)
                        for rid, rx, t in TYPE_RULES]

OTHER_TYPES = {"Anderes", "Autre", "Altro", ""}


def classify_type(title: str) -> tuple[str, str] | None:
    """Classify a title into (canonical instrument type, rule_id)."""
    t = str(title or "")
    if _LEAVE_OTHER.match(t):
        return None
    for rid, rx, ctype in _TYPE_RULES_COMPILED:
        if rx.search(t):
            return ctype, rid
    return None


def enrich_types(repo_path: str | Path, cantons: list[str] | None = None,
                 dry_run: bool = False) -> dict:
    """Back-fill category_type_inferred for laws LexFind types as 'Other'.

    LexFind's value is never touched; inferences carry the matching
    rule id (``type_inference_rule``) for verifiability. Idempotent."""
    from .cantonal import ALL_CANTONS
    from .categories import canonical_category_type
    from .category_enricher import _parse_frontmatter, _write_frontmatter

    repo = Path(repo_path)
    cantons = [c.lower() for c in (cantons or ALL_CANTONS)]
    stats = {"scanned": 0, "typed_by_lexfind": 0, "inferred": 0,
             "already_inferred": 0, "residual": 0}
    per_rule: dict[str, int] = {}

    for canton in cantons:
        for md in sorted((repo / "ch" / canton).rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            fm, body = _parse_frontmatter(text)
            if fm is None or not fm.get("systematic_number"):
                continue
            stats["scanned"] += 1
            ct = canonical_category_type(str(fm.get("category_type", "")))
            if ct not in OTHER_TYPES:
                stats["typed_by_lexfind"] += 1
                continue
            if fm.get("category_type_inferred"):
                stats["already_inferred"] += 1
                continue
            result = classify_type(str(fm.get("title", "")))
            if not result:
                stats["residual"] += 1
                continue
            ctype, rule = result
            stats["inferred"] += 1
            per_rule[rule] = per_rule.get(rule, 0) + 1
            if not dry_run:
                fm["category_type_inferred"] = ctype
                fm["type_inference_rule"] = rule
                md.write_text(_write_frontmatter(fm, body), encoding="utf-8")

    stats["per_rule"] = per_rule
    logger.info("Type inference: %s", stats)
    return stats


def enrich_domains(repo_path: str | Path, cantons: list[str] | None = None,
                   dry_run: bool = False) -> dict:
    """Back-fill global_category_inferred for cantonal laws without a
    LexFind global_category. Offline (trees already on disk); idempotent."""
    from .cantonal import ALL_CANTONS
    from .categories import DOMAIN_EN
    from .category_enricher import _parse_frontmatter, _write_frontmatter

    repo = Path(repo_path)
    trees_dir = repo / "docs" / "trees"
    cantons = [c.lower() for c in (cantons or ALL_CANTONS)]

    stats = {"scanned": 0, "already_classified": 0, "canton_systematics": 0,
             "title_keywords": 0, "residual": 0}
    # domain label lookup: prefer German titles of the global tree top levels
    from .categories import build_global_title_map
    top_titles = {k: v for k, v in build_global_title_map(trees_dir).items()
                  if "." not in k}

    for canton in cantons:
        topcode_map = build_canton_topcode_map(trees_dir, canton)
        for md in sorted((repo / "ch" / canton).rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            fm, body = _parse_frontmatter(text)
            if fm is None or not fm.get("systematic_number"):
                continue
            stats["scanned"] += 1
            if fm.get("global_category"):
                stats["already_classified"] += 1
                continue
            if fm.get("global_category_inferred"):
                stats[fm.get("inference_source", "title_keywords")] += 1
                continue
            inferred = infer_domain(fm, topcode_map)
            if not inferred:
                stats["residual"] += 1
                continue
            code, source = inferred
            label = f"{code} {top_titles.get(code, DOMAIN_EN.get(code, ''))}".strip()
            stats[source] += 1
            if not dry_run:
                fm["global_category_inferred"] = label
                fm["inference_source"] = source
                md.write_text(_write_frontmatter(fm, body), encoding="utf-8")

    logger.info("Domain inference: %s", stats)
    return stats
