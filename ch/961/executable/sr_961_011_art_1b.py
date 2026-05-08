"""SR 961.011 Art. 1b-1e — Principes de surveillance et allégements

Generated from: ch/961/fr/961.011.md

OS (Ordonnance sur la surveillance) — Supervision principles and relief:
- Art. 1b: FINMA classifies insurers in categories per Annex 2 (by statutory balance sheet total)
- Art. 1c: Small insurer relief (categories 4 & 5) if ALL conditions met:
  SST quotient >= 250% (3-year avg), tied assets >= 130% of debit,
  supervisory minimum capital >= 150%, no loss carry-forward,
  solid planning, no other SST/tied-assets reliefs, no FINMA measures
- Art. 1d: Reinsurer relief (categories 4 & 5) with annual compliance declaration
- Art. 1e: New authorization relief for category 5 for max 3 years
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class categorie_surveillance_assurance(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Catégorie de surveillance FINMA (1-5, basée sur le total du bilan statutaire)"
    reference = "SR 961.011 Art. 1b al. 2"


class quotient_sst_moyenne_3_ans(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Quotient SST moyen sur 3 ans (%)"
    reference = "SR 961.011 Art. 1c let. a"


class taux_couverture_fortune_liee(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux de couverture de la fortune liée en % du débit"
    reference = "SR 961.011 Art. 1c let. b"


class taux_couverture_capital_minimum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux de couverture du capital minimal de surveillance (%)"
    reference = "SR 961.011 Art. 1c let. c"


class a_report_perte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Présente un report de perte (exercices précédents ou en cours)"
    reference = "SR 961.011 Art. 1c let. d"


class beneficie_autre_allegement_sst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bénéficie d'un autre allégement SST ou fortune liée"
    reference = "SR 961.011 Art. 1c let. g"


class fait_objet_mesure_finma(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fait l'objet de mesures FINMA ou d'une procédure ouverte"
    reference = "SR 961.011 Art. 1c let. h"


class est_assurance_directe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Est une entreprise d'assurance directe"
    reference = "SR 961.011 Art. 1c"


class eligible_allegement_petite_entreprise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Éligible aux allégements pour petites entreprises d'assurance"
    reference = "SR 961.011 Art. 1c"

    def formula(person, period, parameters):
        p = parameters(period).sr_961_011
        cat = person('categorie_surveillance_assurance', period)
        directe = person('est_assurance_directe', period)
        sst = person('quotient_sst_moyenne_3_ans', period) >= p.seuil_sst_allegement
        fortune = person('taux_couverture_fortune_liee', period) >= p.seuil_fortune_liee_allegement
        capital = person('taux_couverture_capital_minimum', period) >= p.seuil_capital_minimum_allegement
        pas_perte = 1 - person('a_report_perte', period)
        pas_autre = 1 - person('beneficie_autre_allegement_sst', period)
        pas_mesure = 1 - person('fait_objet_mesure_finma', period)
        cat_eligible = (cat >= 4)  # Categories 4 and 5
        return (
            directe * cat_eligible * sst * fortune *
            capital * pas_perte * pas_autre * pas_mesure
        )
