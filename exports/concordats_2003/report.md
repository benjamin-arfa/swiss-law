# Concordats intercantonaux jusqu'à 2003 — LexFind vs. statistique 2003

*Généré le 2026-07-28 07:14 UTC — script `scripts/fetch_concordats_to_2003.py` (sha256 `06b549e7852f2de9…`)*

## Résumé

| Indicateur | Valeur |
|---|---|
| Textes intercantonaux recensés aujourd'hui sur LexFind (Intlex, actifs + abrogés) | **333** |
| … dont conclus jusqu'au 2003-12-31 | **171** |
| … dont encore en vigueur aujourd'hui | 162 |
| … sans date déterminable | 0 |
| Baseline 2003 (BADAC/IDHEAP, 1848-2003) | **733** concordats conclus |
| Écart LexFind (≤2003) vs baseline | **-562** (23.3% de l'inventaire 2003) |

## Interprétation de l'écart

L'inventaire BADAC 2003 compte **tous** les concordats *conclus* entre 1848 et 2003 (y compris les accords bilatéraux ponctuels, remplacés ou éteints). LexFind/Intlex est en revanche le **recueil systématique du droit intercantonal** tenu par la Fondation ch : il ne référence pour l'essentiel que les textes encore pertinents (en vigueur ou récemment abrogés). L'écart mesure donc surtout l'attrition historique du corpus — il ne signifie pas que LexFind « manque » des données, mais que les deux sources répondent à des questions différentes.

## Répartition par domaine — comparaison

| Domaine (nomenclature BADAC) | BADAC 1848-2003 | LexFind ≤2003 (aujourd'hui) |
|---|---|---|
| Éducation, science et culture | 25% (~183) | 23.4% (40) |
| Organisation étatique et sécurité | 13% (~95) | 18.7% (32) |
| Finances et fiscalité | 20% (~147) | 21.6% (37) |
| Économie et agriculture | 15% (~110) | 2.9% (5) |
| Infrastructure, trafic et environnement | 16% (~117) | 31.0% (53) |
| Santé et sécurité sociale | 10% (~73) | 2.3% (4) |

## Répartition par décennie (LexFind, conclus ≤2003)

| Décennie | Textes |
|---|---|
| 1820s | 1 |
| 1840s | 1 |
| 1860s | 1 |
| 1870s | 4 |
| 1880s | 2 |
| 1890s | 2 |
| 1900s | 3 |
| 1910s | 3 |
| 1920s | 4 |
| 1930s | 6 |
| 1940s | 5 |
| 1950s | 5 |
| 1960s | 15 |
| 1970s | 27 |
| 1980s | 17 |
| 1990s | 46 |
| 2000s | 29 |

Baseline : ~70 % des 733 concordats 1848-2003 signés depuis les années 1970 ; dans LexFind ≤2003 : 69.6%.

Bilatéraux (heuristique sur le titre « zwischen den Kantonen X und Y ») : 19.9% (34) — baseline : 44 %.

## Sources et auditabilité

- LexFind : entité Intlex (id 28), 338 requêtes HTTP, toutes journalisées dans `audit_log.jsonl` (URL, statut, octets, SHA-256).
- Réponses brutes archivées dans `raw/` (une par empreinte SHA-256).
- Baseline : Bochsler/Koller/Sciarini/Traimond/Trippolini (2004): 'Les cantons suisses sous la loupe', BADAC/IDHEAP, Haupt Verlag. Press release: https://www.presseportal.ch/fr/pm/100006693/100488671
- Fichiers produits : `intlex_full_inventory.csv` (tout Intlex), `concordats_up_to_2003.csv` (filtré ≤2003), `run_manifest.json`.
- Date retenue par texte : `family_active_since` de l'API LexFind (date d'origine de la famille d'actes), sinon la date figurant dans le titre officiel, sinon la plus ancienne version connue (`date_source` dans les CSV).