"""SR 221.214.1 Art. 14

Generated from: ch/221/fr/221.214.1.md

Maximum interest rate for consumer credit: set by Federal Council,
generally must not exceed 15%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lcc_taux_interet_annuel_convenu(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taux d'interet annuel convenu pour le credit a la consommation en pourcentage"
    reference = "SR 221.214.1 Art. 14"


class lcc_taux_maximum_legal_pourcent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux maximum admissible fixe par le Conseil federal (en regle generale max 15%)"
    reference = "SR 221.214.1 Art. 14"

    def formula(person, period, parameters):
        return 15.0


class lcc_taux_depasse_maximum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le taux d'interet convenu depasse le taux maximum legal"
    reference = "SR 221.214.1 Art. 14"

    def formula(person, period, parameters):
        taux_convenu = person('lcc_taux_interet_annuel_convenu', period)
        return taux_convenu > 15.0
