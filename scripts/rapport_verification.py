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
           "reconciled": "rapproché", "exceeds_reference": "au-delà de la référence"}


def build_markdown() -> str:
    cmp_ = json.loads((SITE / "api/v1/stats/concordats_chstat_comparison.json").read_text())
    conc = json.loads((SITE / "api/v1/stats/concordats_by_domain.json").read_text())
    stats = json.loads((SITE / "stats.json").read_text())
    dist = json.loads(
        (SITE / "api/v1/stats/concordats_size_distribution.json").read_text())
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
        f"| Actes d'adhésion (concordat non publié séparément) | {n(cmp_.get('accession_evidence_total', 0))} |",
        f"| Cantons nommés dans l'inventaire Intlex ≤ 2003 | {n(cmp_.get('intlex_named_evidence_total', 0))} |",
        f"| **Total expliqué** | **{n(cmp_.get('explained_total', active + repealed))}** |",
        f"| Écart inexpliqué | {n(cmp_['unexplained_total'])} |",
        f"| (Sans date connue chez nous) | {n(cmp_['undated_total'])} |",
        "",
        f"Notre collection compte au total **{n(conc['totals']['total'])}** appartenances cantonales",
        f"(toutes dates confondues), contre {n(cmp_['chstat_total'])} en 2003.",
        "",
        "**Unité de compte.** Les deux chiffres comptent des *appartenances* (canton × concordat), et non",
        "des concordats. La publication d'origine (IDHEAP/BADAC, communiqué CP4 de 2004, graphique G1)",
        f"annonce pour 1848–2003 **{n(cmp_.get('badac_total_concordats', 733))} concordats** pour",
        f"**{n(cmp_.get('badac_total_memberships', 2564))} appartenances cantonales**. La table chstat",
        f"n'en recense que {n(cmp_['chstat_total'])} parce qu'elle ne tabule que les six domaines",
        f"attribuables ; l'écart de {n(cmp_.get('chstat_vs_badac_unattributed', 42))} correspond à la",
        "septième bande « pas attribuable » du graphique G1.",
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
        "| Canton | chstat 2003 | ≤2003 en vigueur | ≤2003 abrogés | Adhésions | Intlex | Inexpliqué | Total (toutes dates) | Diagnostic |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for c, v in rows.items():
        o = v["ours_enacted_until_2003"]
        a = v.get("additional_evidence", {"accession": 0, "intlex_named": 0})
        lines.append(f"| {c} | {v['chstat_2003']['total']} | {o['active']} | "
                     f"{o['repealed_listed']} | {a['accession']} | {a['intlex_named']} | "
                     f"{v['unexplained']} | {v['all_time_total']} | "
                     f"{DIAG_FR.get(v['diagnosis'], v['diagnosis'])} |")
    lines += [
        f"| **Total** | **{n(cmp_['chstat_total'])}** | **{n(active)}** | **{n(repealed)}** | "
        f"**{n(cmp_.get('accession_evidence_total', 0))}** | "
        f"**{n(cmp_.get('intlex_named_evidence_total', 0))}** | "
        f"**{n(cmp_['unexplained_total'])}** | "
        f"**{n(sum(v['all_time_total'] for v in rows.values()))}** | |",
        "",
        "Diagnostics : *datation* = nous détenons au moins autant de concordats que chstat, mais les dates",
        "en placent une partie hors 2003 ; *retrait du répertoire* = nous en détenons moins que chstat",
        "(actes retirés du répertoire public) ; *rapproché* = écart ≤ 5 ; *au-delà de la référence* =",
        "nous comptons davantage de preuves ≤ 2003 que chstat (textes d'application typés « concordat »",
        "par LexFind, adhésions postérieures nommées dans les intitulés).",
        "",
        "Colonnes *Adhésions* / *Intlex* : appartenances prouvées bien que le concordat lui-même soit",
        "retiré du répertoire — actes d'adhésion cantonaux (Beitritt/adhésion) dont le concordat n'est",
        "pas publié séparément, et cantons nommés dans les intitulés de l'inventaire Intlex ≤ 2003",
        "(collections germanophones uniquement). Piste d'audit :",
        "`api/v1/quality/concordat_membership_evidence.json`.",
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
        "# Nombre de cantons par concordat (reproduction du graphique G1)",
        "",
        "Référence : IDHEAP/BADAC, communiqué CP4 (2004), graphique G1, 1848–2003. Les pourcentages",
        "publiés sont des parts des **appartenances** (« résultats pondérés : 2564 = 100 % »), et non",
        "des parts des 733 concordats — la lecture littérale du texte du communiqué (« 44 % étaient",
        "des accords bilatéraux ») est arithmétiquement impossible : 22 % de 733 concordats réunissant",
        "au moins 20 cantons dépasseraient à eux seuls 3 200 appartenances. Non pondérés, les accords",
        "bilatéraux représentent environ 77 % des concordats.",
        "",
        "| Cantons signataires | Nos concordats | Nos appartenances | Part | Réf. appartenances | Part réf. | Réf. concordats |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for b in dist["bands"]:
        lines.append(
            f"| {b['band']} | {n(b['ours_concordats'])} | {n(b['ours_memberships'])} | "
            f"{100 * b['ours_share_of_memberships']:.1f} % | {n(b['badac_memberships'])} | "
            f"{100 * b['badac_share_of_memberships']:.0f} % | {n(b['badac_concordats_implied'])} |")
    do_, db_ = dist["ours"], dist["baseline"]
    lines += [
        f"| **Total** | **{n(do_['concordats'])}** | **{n(do_['memberships'])}** | 100 % | "
        f"**{n(db_['total_memberships'])}** | 100 % | **{n(db_['total_concordats'])}** |",
        "",
        f"Nombre moyen de cantons par concordat : **{do_['mean_signatories']}** chez nous, contre",
        f"**{db_['total_memberships'] / db_['total_concordats']:.2f}** dans la référence.",
        f"Conventions réunissant les 26 cantons : {n(do_['all_canton_agreements'])} chez nous, une",
        f"douzaine selon la référence ({n(db_['all_canton_conventions'])} nommées en note 1 du communiqué).",
        "",
        "**Comment un canton signataire est établi.** Trois preuves cumulatives : le canton publie le",
        "texte dans son propre recueil ; le canton est nommé dans l'intitulé ; le canton est énuméré",
        "comme partie contractante dans le préambule (texte avant l'art. 1). Détail :",
        "",
        "| Preuve d'appartenance | Nombre |",
        "|---|---:|",
    ]
    ev_fr = {"published_in_own_collection": "publication dans le recueil du canton",
             "named_as_party_in_preamble": "partie nommée au préambule",
             "named_in_title": "canton nommé dans l'intitulé"}
    for k, v in sorted(dist["membership_evidence"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {ev_fr.get(k, k)} | {n(v)} |")
    lines += [
        "",
        f"**Limite structurelle.** {n(do_['unresolved_single_party'])} actes typés « concordat » par",
        "LexFind ne laissent apparaître qu'un seul canton : ce sont des appartenances que nous ne",
        "parvenons pas à résoudre, et non des concordats à un canton — ils sont donc exclus du tableau",
        "ci-dessus plutôt que comptés comme bilatéraux. La cause principale est rédactionnelle : les",
        "concordats ouverts s'adressent « aux cantons signataires » (« Die unterzeichnenden Kantone »)",
        "sans jamais les nommer. Leur composition ne figure nulle part dans le texte ; la BADAC la",
        "tirait de la base de données de l'Institut du fédéralisme, qui enregistre les adhésions,",
        "alors que LexFind ne publie aucune liste de membres. C'est aussi ce qui explique que la bande",
        "20–26 reste sous-représentée chez nous : ce sont précisément les grands concordats ouverts.",
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
    ]

    # date methodology & changelog (frozen basis)
    clog = json.loads((SITE / "api/v1/quality/methodology_changelog.json").read_text())
    pol = clog["canonical_date_policy"]
    lines += [
        "",
        "# Méthodologie des dates — base FIGÉE et journal des versions",
        "",
        f"**Source canonique (figée le {pol['frozen_since']})** : `family_active_since` de LexFind",
        "(API frontend) — la date d'origine de la « famille » de l'acte, disponible pour les 26 cantons.",
        "Les dates LexWork (`date_of_decision`) ont été remplacées car elles reflétaient souvent la",
        "décision d'adhésion du canton : les divergences de dates entre cantons frères sont passées de",
        "**72 groupes à 4** avec la base famille. À défaut de donnée famille, chaîne de repli fixe :",
        "`lexwork_api` > preuve d'un canton frère > analyse du texte > date de version courante.",
        "",
        "**Les chiffres ne changent désormais que si les données sous-jacentes changent, et tout",
        "changement est consigné dans le journal ci-dessous.**",
        "",
        "| v | Base de datation | Exist. <= 2003 | Inexpl. | Sans date | Motif |",
        "|---|---|---:|---:|---:|---|",
    ]
    for v in clog["changelog"]:
        e3 = "—" if v["existed_by_2003"] is None else n(v["existed_by_2003"])
        ux = "—" if v["unexplained"] is None else n(v["unexplained"])
        ud = "—" if v["undated"] is None else n(v["undated"])
        lines.append(f"| {v['version']} | {v['date_basis']} | {e3} | {ux} | {ud} | {v['change_reason']} |")

    lines += [
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


# pdflatex has no glyphs for the mathematical-operator block, and xelatex's
# default Latin Modern text font does not carry them either, so they are
# transliterated before rendering.  Anything left in the arrow/operator ranges
# is dropped rather than allowed to abort the build.
_TEX_SUBSTITUTIONS = {
    "≤": "<=", "≥": ">=", "≈": "~", "≠": "!=",
    "∪": " U ", "∩": " et ", "∈": " dans ",
    "→": "->", "←": "<-", "×": "x", "Δ": "Diff.",
}
_DROP_RANGES = ((0x2190, 0x21FF), (0x2200, 0x22FF), (0x2300, 0x23FF))


def tex_safe(md: str) -> str:
    for src, dst in _TEX_SUBSTITUTIONS.items():
        md = md.replace(src, dst)
    return "".join("" if any(lo <= ord(c) <= hi for lo, hi in _DROP_RANGES) else c
                   for c in md)


def to_pdf(md: str, out: Path):
    md = tex_safe(md)
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
