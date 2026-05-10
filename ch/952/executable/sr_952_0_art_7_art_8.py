"""SR 952.0 Art. 7-8 - Banques d'importance systemique (Systemically Important Banks)

Generated from: ch/952/fr/952.0.md

Definition and criteria for systemically important banks:
- Art. 7: Banks whose failure would seriously harm the Swiss economy and financial system
- Art. 8: Systemic importance assessed by: size, interconnectedness, substitutability
  - Key criteria: market share in systemic functions, guaranteed deposits exceeding
    the maximum limit, ratio of total balance sheet to annual GDP, risk profile
- Systemic functions: deposit, credit, and payment operations
- Swiss National Bank (BNS) determines which banks are systemically important
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lb_total_bilan(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total du bilan de la banque (en francs)"
    reference = "SR 952.0 Art. 8 al. 2 let. c"


class lb_pib_annuel_suisse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Produit interieur brut annuel de la Suisse (en francs)"
    reference = "SR 952.0 Art. 8 al. 2 let. c"


class lb_ratio_bilan_pib(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rapport entre le total du bilan et le PIB annuel suisse"
    reference = "SR 952.0 Art. 8 al. 2 let. c"

    def formula(person, period, parameters):
        bilan = person('lb_total_bilan', period)
        pib = person('lb_pib_annuel_suisse', period)
        return where(pib > 0, bilan / pib, 0)


class lb_depots_garantis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant des depots garantis selon art. 37h al. 1 (en francs)"
    reference = "SR 952.0 Art. 8 al. 2 let. b"


class lb_limite_maximale_depots_garantis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Limite maximale prevue pour les depots garantis selon art. 37h al. 3 let. b"
    reference = "SR 952.0 Art. 8 al. 2 let. b"


class lb_depots_garantis_excedentaires(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant depassant la limite maximale des depots garantis"
    reference = "SR 952.0 Art. 8 al. 2 let. b"

    def formula(person, period, parameters):
        depots = person('lb_depots_garantis', period)
        limite = person('lb_limite_maximale_depots_garantis', period)
        return max_(depots - limite, 0)


class lb_part_marche_fonctions_systemiques(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Part de marche dans les fonctions d'importance systemique (0-1)"
    reference = "SR 952.0 Art. 8 al. 2 let. a"


class lb_est_importance_systemique(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La banque est d'importance systemique (determinee par la BNS)"
    reference = "SR 952.0 Art. 8 al. 3"
