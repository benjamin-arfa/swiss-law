#!/usr/bin/env python3
"""Rapport de vérification (français) — PDF via pandoc, envoi Telegram.

Construit le rapport depuis les JSON publiés (chiffres toujours à jour),
le rend en PDF (pandoc → pdflatex) et l'envoie par Telegram (sendDocument).

Usage:
    .venv/bin/python scripts/rapport_verification.py [--pdf out.pdf] [--send]
"""
from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent.parent / "swiss-law-as-source"

DIAG_FR = {"dating": "datation", "delisting_or_coverage": "retrait du répertoire",
           "reconciled": "rapproché"}


def build_markdown() -> str:
    cmp_ = json.loads((SITE / "api/v1/stats/concordats_chstat_comparison.json").read_text())
    conc = json.loads((SITE / "api/v1/stats/concordats_by_domain.json").read_text())
    stats = json.loads((SITE / "stats.json").read_text())
    unc = json.loads((SITE / "api/v1/quality/unclassified_types.json").read_text())

    n = lambda x: f"{x:,}".replace(",", " ")
    rows = cmp_["cantons"]
    active = sum(v["ours_enacted_until_2003"]["active"] for v in rows.values())
    repealed = sum(v["ours_enacted_until_2003"]["repealed_listed"] for v in rows.values())
    today = datetime.date.today().strftime("%d.%m.%Y")

    lines = [
        "---",
        "title: Rapport de vérification — Concordats intercantonaux",
        f"subtitle: Collection Swiss Law vs chstat.ch (2003) — état au {today}",
        "lang: fr",
        "geometry: margin=2.2cm",
        "---",
        "",
        "# Résumé",
        "",
        "La table de référence « Concordats par domaine » (chstat.ch, Institut du fédéralisme, 2003)",
        f"recense **{n(cmp_['chstat_total'])}** appartenances cantonales à des concordats. Rapprochement",
        "avec notre collection (source : LexFind / portails cantonaux) :",
        "",
        "| Composante | Nombre |",
        "|---|---:|",
        f"| Référence chstat 2003 | **{n(cmp_['chstat_total'])}** |",
        f"| Nos concordats existant ≤ 2003, en vigueur | {n(active)} |",
        f"| Nos concordats existant ≤ 2003, abrogés mais répertoriés | {n(repealed)} |",
        f"| Écart inexpliqué | {n(cmp_['unexplained_total'])} |",
        f"| (Sans date connue chez nous) | {n(cmp_['undated_total'])} |",
        "",
        f"Notre collection compte au total **{n(conc['totals']['total'])}** entrées de concordats",
        "(toutes dates confondues), contre 2 522 en 2003 — la croissance attendue sur 23 ans.",
        "",
        "# Méthodologie",
        "",
        "1. **Une loi est un couple (loi, version).** Tout filtrage temporel utilise la *première preuve",
        "   d'existence connue* : date d'origine de l'acte (« famille » LexFind), historique des versions,",
        "   ou — lorsque la date propre du canton n'est pas vérifiée — la date faisant foi la plus ancienne",
        "   du même concordat dans un canton frère (un concordat est le même acte dans chaque canton membre).",
        "2. **Hiérarchie de provenance des dates** : `lexfind_family` (date d'origine de la famille,",
        "   API frontend LexFind, disponible pour les 26 cantons) > `lexwork_api` (`date_of_decision`",
        "   du portail — parfois la décision d'adhésion du canton) > `sibling` > `text` (analyse du texte).",
        "   Une provenance supérieure remplace une provenance inférieure, jamais l'inverse.",
        "3. **Les lois abrogées sont incluses et marquées** (`is_active: false` selon LexFind).",
        "4. **Réserve adhésion / appartenance** : chstat comptait l'appartenance en 2003 ; certaines dates",
        "   faisant foi sont des décisions d'adhésion cantonales — des groupes de concordats-frères aux",
        "   dates faisant foi divergentes le prouvent.",
        "",
        "# Rapprochement par canton",
        "",
        "| Canton | chstat 2003 | ≤2003 en vigueur | ≤2003 abrogés | Inexpliqué | Total (toutes dates) | Diagnostic |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for c, v in rows.items():
        o = v["ours_enacted_until_2003"]
        lines.append(f"| {c} | {v['chstat_2003']['total']} | {o['active']} | "
                     f"{o['repealed_listed']} | {v['unexplained']} | {v['all_time_total']} | "
                     f"{DIAG_FR.get(v['diagnosis'], v['diagnosis'])} |")
    lines += [
        f"| **Total** | **{n(cmp_['chstat_total'])}** | **{n(active)}** | **{n(repealed)}** | "
        f"**{n(cmp_['unexplained_total'])}** | "
        f"**{n(sum(v['all_time_total'] for v in rows.values()))}** | |",
        "",
        "Diagnostics : *datation* = nous détenons au moins autant de concordats que chstat, mais les dates",
        "en placent une partie hors 2003 ; *retrait du répertoire* = nous en détenons moins que chstat",
        "(actes retirés du répertoire public) ; *rapproché* = écart ≤ 5.",
        "",
        "## Preuves utilisées (≤ 2003)",
        "",
        "| Type de preuve | Nombre |",
        "|---|---:|",
    ]
    for k, v in sorted(cmp_.get("year_evidence_le2003", {}).items(), key=lambda kv: -kv[1]):
        fr = {"own_enactment": "date d'origine propre", "own_versions": "historique des versions propre",
              "sibling_group": "preuve d'un canton frère", "undated": "sans date"}.get(k, k)
        lines.append(f"| {fr} | {n(v)} |")
    tp = stats.get("type_provenance", {})
    # comparison by domain (chstat per-domain vs ours <=2003)
    keys6 = ["etat", "sante", "educ", "infra", "eco", "fin"]
    chstat_dom = {k: sum(v["chstat_2003"].get(k, 0) for v in rows.values()) for k in keys6}
    ours03 = {k: 0 for k in keys6 + ["autres"]}
    for y, pc in conc.get("by_year", {}).items():
        if y == "unknown" or y > "2003":
            continue
        for row in pc.values():
            for k, v in row.items():
                if k in ours03:
                    ours03[k] += v
    labels_fr = {d["key"]: d["label_fr"] for d in conc["domains"]}
    lines += [
        "",
        "# Comparaison par domaine (chstat 2003 vs notre collection)",
        "",
        "| Domaine | chstat 2003 | Chez nous ≤ 2003 | Chez nous (toutes dates) | Δ ≤2003 |",
        "|---|---:|---:|---:|---:|",
    ]
    for k in keys6:
        lines.append(f"| {labels_fr[k]} | {n(chstat_dom[k])} | {n(ours03[k])} | "
                     f"{n(conc['totals'][k])} | {ours03[k] - chstat_dom[k]:+d} |")
    lines += [
        f"| {labels_fr['autres']} (absent de chstat) | — | {n(ours03['autres'])} | "
        f"{n(conc['totals']['autres'])} | — |",
        f"| **Total** | **{n(cmp_['chstat_total'])}** | "
        f"**{n(sum(ours03.values()))}** | **{n(conc['totals']['total'])}** | |",
        "",
        "La base interne 2003 de l'Institut classait chaque concordat dans un domaine ; notre colonne",
        "« Autres » (droit civil, droit pénal, actes sans domaine à la source) explique l'essentiel des",
        "écarts négatifs des colonnes nominales.",
        "",
        "# Qualité des données",
        "",
        f"- **Dates** : provenance classée, {n(sum(cmp_.get('date_provenance_total', {}).values()))} concordats",
        "  ≤ 2003 datés ; détail par source dans le JSON de rapprochement.",
        f"- **Types d'actes** : {n(tp.get('lexfind', 0))} typés par LexFind, {n(tp.get('inferred', 0))}",
        f"  complétés par règles sur les intitulés ; {n(unc.get('residual', 0))} actes réellement « autres »",
        "  (directives, décisions, concessions, tarifs) — liste de contrôle publiée.",
        "- **Domaines juridiques** : taxonomie harmonisée LexFind (« domaine juridique ») couvrant droit",
        "  fédéral et cantonal, avec inférence tracée pour les actes non classés à la source.",
        "",
        "# Limites et prochaine étape",
        "",
        f"L'écart inexpliqué ({n(cmp_['unexplained_total'])}) recouvre : (a) des concordats qui ne sont plus",
        "rattachés aux catalogues systématiques publics de LexFind — les statistiques globales de LexFind",
        "recensent davantage de textes que ses catalogues n'en énumèrent — et (b) la sémantique",
        "adhésion / appartenance. Pour clore entièrement le rapprochement, la voie réaliste est la base",
        "interne de l'Institut du fédéralisme (opérateur de chstat.ch), dont la table 2003 est issue.",
        "",
        "----",
        "",
        "*Rapport généré automatiquement depuis les données publiées :*",
        "*https://swiss-law-as-source.github.io/verification.html (rapport interactif),*",
        "*api/v1/stats/concordats_chstat_comparison.json (données de cette page).*",
    ]
    return "\n".join(lines)


def to_pdf(md: str, out: Path):
    # pdflatex lacks glyphs for these — use math-mode equivalents
    md = md.replace("≤", "<=").replace("Δ", "Diff.")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(md)
        src = f.name
    subprocess.run(["pandoc", src, "-o", str(out), "--pdf-engine=pdflatex",
                    "-V", "fontsize=10pt"], check=True, timeout=300)


def send_telegram(pdf: Path) -> bool:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
    from legalize_ch.notify import _load_telegram_config
    import requests
    token, chat_id = _load_telegram_config()
    if not token:
        print("No Telegram credentials")
        return False
    with open(pdf, "rb") as f:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendDocument",
            data={"chat_id": chat_id,
                  "caption": "📊 Rapport de vérification — concordats intercantonaux "
                             "vs chstat.ch 2003 (généré automatiquement)"},
            files={"document": (pdf.name, f, "application/pdf")},
            timeout=120)
    ok = r.ok and r.json().get("ok")
    print("Telegram:", "ok" if ok else r.text[:200])
    return bool(ok)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--send", action="store_true")
    args = ap.parse_args()
    md = build_markdown()
    out = Path(args.pdf or f"rapport_verification_{datetime.date.today():%Y%m%d}.pdf")
    to_pdf(md, out)
    print(f"PDF: {out} ({out.stat().st_size:,} bytes)")
    if args.send:
        sys.exit(0 if send_telegram(out) else 1)
