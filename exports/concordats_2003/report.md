# Concordats intercantonaux jusqu'à 2003 — LexFind vs. visualisation CHStat 2003

*Généré le 2026-07-28 10:38 UTC — script `scripts/fetch_concordats_to_2003.py` (sha256 `48d4321282fe2bdd…`)*

## Résumé

| Indicateur | Valeur |
|---|---|
| Textes intercantonaux recensés aujourd'hui sur LexFind (Intlex, actifs + abrogés) | **333** |
| … dont conclus jusqu'au 2003-12-31 | **171** |
| … dont encore en vigueur aujourd'hui | 162 |
| … sans date déterminable | 0 |
| Baseline CHStat 2003 — concordats conclus 1848-2003 | **733** |
| Baseline CHStat 2003 — cantons membres (pondération de la visualisation) | **2564** |
| Écart LexFind ≤2003 vs baseline (en concordats) | **-562** (23.3% de l'inventaire 2003) |
| Adhésions cantonales estimées, LexFind ≤2003 (voir méthode) | ~996 (bornes [366, 2694]) |

## Les deux unités de la visualisation CHStat : 733 concordats, 2564 cantons membres

La visualisation « Concordats » de CHStat/BADAC (graphique G1 du communiqué IDHEAP du 15.11.2004, d'après la banque de données des concordats de l'Institut du fédéralisme de l'Université de Fribourg) porte en légende : **« Total 1848-2003 = 733 concordats; 2564 cantons membres »**, avec la mention *« résultats pondérés : 2564 = 100% »*. Deux unités coexistent donc :

1. **733** — le nombre de concordats *conclus* entre 1848 et 2003 (un par traité) ;
2. **≈2500 (2564)** — le nombre d'*adhésions cantonales* : chaque concordat compté une fois par canton signataire (soit ≈3,5 cantons par concordat en moyenne).

Tous les pourcentages affichés par la visualisation (domaines et classes de taille) sont **pondérés par les adhésions** (2564 = 100 %), pas par le nombre de textes. Lecture inverse de la légende des classes de taille :

| Cantons signataires | Part des adhésions (G1) | Adhésions | Concordats (dérivé) |
|---|---|---|---|
| 2 | 44% | 1128 | ~564 |
| 3-4 | 8% | 205 | ~59 |
| 5-10 | 20% | 513 | ~68 |
| 11-19 | 6% | 154 | ~10 |
| 20-26 | 22% | 564 | ~25 |
| **Total** | 100% | 2564 | ~726 (publié : 733) |

Le total dérivé (~726) recoupe le total publié (733) à ~1 % près, ce qui valide cette lecture pondérée. Conséquence notable : **~77 % des concordats 1848-2003 étaient bilatéraux** (564 sur 733), même si les accords bilatéraux ne représentent que 44 % des adhésions.

## Interprétation de l'écart

L'inventaire de l'Institut du fédéralisme compte **tous** les concordats *conclus* entre 1848 et 2003 (y compris les accords bilatéraux ponctuels, remplacés ou éteints). LexFind/Intlex est en revanche le **recueil systématique du droit intercantonal** tenu par la Fondation ch : il ne référence pour l'essentiel que les textes encore pertinents (en vigueur ou récemment abrogés). L'écart mesure donc surtout l'attrition historique du corpus — il ne signifie pas que LexFind « manque » des données, mais que les deux sources répondent à des questions différentes.

En unité « concordats » : 171 vs 733 (23.3% du corpus historique subsiste). En unité « adhésions cantonales » : ~996 estimées vs 2564 — la part subsistante est plus élevée en adhésions qu'en textes, car ce sont surtout les petits accords bilatéraux qui ont disparu, tandis que les grands concordats multilatéraux ont survécu.

### Méthode d'estimation des adhésions LexFind

- 74 textes ≤2003 énumèrent leurs cantons dans le titre (≥2 cantons nommés) → comptage exact : 172 adhésions ;
- 97 textes multilatéraux « ouverts » ne nomment pas leurs parties → bornes [2, 26] par texte, estimation à la moyenne non-bilatérale de la baseline (2564−1128 adhésions / 733−564 concordats ≈ 8.5 cantons/texte) ;
- LexFind/Intlex ne publie pas la liste des cantons membres par texte via son API — un comptage exact nécessiterait la banque de données de l'Institut du fédéralisme ou le dépouillement des clauses d'adhésion des PDF. Les colonnes `named_cantons`/`n_named_cantons` des CSV rendent le comptage titre par titre vérifiable.

## Répartition par domaine — comparaison

⚠️ Unités différentes : la colonne CHStat est pondérée par **adhésions** (2564 = 100 %), la colonne LexFind par **textes** (les adhésions par texte n'étant pas connues côté LexFind). Les écarts domaine par domaine mêlent donc attrition réelle et effet de pondération : un domaine riche en accords bilatéraux (2 adhésions/texte) pèse moins dans la colonne CHStat qu'en nombre de textes.

| Domaine (nomenclature BADAC) | CHStat 1848-2003 (% adhésions) | LexFind ≤2003 (% textes) |
|---|---|---|
| Éducation, science et culture | 25% (~641 adh.) | 23.4% (40) |
| Organisation étatique et sécurité | 13% (~333 adh.) | 18.7% (32) |
| Finances et fiscalité | 20% (~513 adh.) | 21.6% (37) |
| Économie et agriculture | 15% (~385 adh.) | 2.9% (5) |
| Infrastructure, trafic et environnement | 16% (~410 adh.) | 31.0% (53) |
| Santé et sécurité sociale | 10% (~256 adh.) | 2.3% (4) |

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

Baseline : ~70 % des 733 concordats 1848-2003 signés depuis les années 1970 (part en concordats, non pondérée) ; dans LexFind ≤2003 : 69.6%.

Bilatéraux (2 cantons nommés dans le titre, ou motif « zwischen den Kantonen X und Y ») : 39.2% (67) — baseline : ~77 % des concordats (dérivé ; 44 % des adhésions). La sous-représentation des bilatéraux dans le corpus subsistant est encore plus marquée qu'annoncé dans la première version de ce rapport.

## Sources et auditabilité

- LexFind : entité Intlex (id 28), 339 requêtes HTTP, toutes journalisées dans `audit_log.jsonl` (URL, statut, octets, SHA-256).
- Réponses brutes archivées dans `raw/` (une par empreinte SHA-256).
- Baseline : CHStat/BADAC (IDHEAP), 'Les concordats intercantonaux: clé de voûte du fédéralisme suisse', communiqué du 15.11.2004, graphique G1 — d'après la banque de données des concordats de l'Institut du fédéralisme, Université de Fribourg. PDF: https://chstat.ch/download/pages/nehhqpsts5nj.pdf/CP4fr.pdf — archivé dans `baseline/CP4fr.pdf` (sha256 `a68bf7e83c77ed4e…`).
- Fichiers produits : `intlex_full_inventory.csv` (tout Intlex), `concordats_up_to_2003.csv` (filtré ≤2003), `run_manifest.json`.
- Date retenue par texte : `family_active_since` de l'API LexFind (date d'origine de la famille d'actes), sinon la date figurant dans le titre officiel, sinon la plus ancienne version connue (`date_source` dans les CSV).