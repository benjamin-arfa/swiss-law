"""SR 952.0 Art. 37m - Avoirs en desherence (Dormant Assets)

Generated from: ch/952/fr/952.0.md

Liquidation of dormant assets (Art. 37m):
- Banks liquidate dormant assets after 50 years if the rightful owner
  has not come forward despite prior publication
- Dormant assets up to CHF 500 can be liquidated without prior publication
- The rightful owner's claim expires upon liquidation
- Proceeds go to the Confederation
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

DELAI_LIQUIDATION_ANNEES = 50
SEUIL_PUBLICATION_PREALABLE = 500  # CHF


class lb_avoir_en_desherence_montant(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant de l'avoir en desherence (en francs)"
    reference = "SR 952.0 Art. 37m al. 1"


class lb_avoir_en_desherence_annees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre d'annees depuis le dernier contact avec l'ayant droit"
    reference = "SR 952.0 Art. 37m al. 1"


class lb_avoir_liquidable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'avoir en desherence peut etre liquide (apres 50 ans)"
    reference = "SR 952.0 Art. 37m al. 1"

    def formula(person, period, parameters):
        annees = person('lb_avoir_en_desherence_annees', period)
        return annees >= DELAI_LIQUIDATION_ANNEES


class lb_publication_prealable_requise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Une publication prealable est requise avant liquidation (montant > 500 CHF)"
    reference = "SR 952.0 Art. 37m al. 1"

    def formula(person, period, parameters):
        montant = person('lb_avoir_en_desherence_montant', period)
        return montant > SEUIL_PUBLICATION_PREALABLE
