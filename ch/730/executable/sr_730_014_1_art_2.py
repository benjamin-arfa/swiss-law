"""SR 730.014.1 Art. 2

Generated from: ch/730/fr/730.014.1.md

Art. 2 - Imputable costs for hydroelectric remediation measures:
1. If remediation measures affect operation and cause reduced or shifted
   energy production, the resulting revenue losses are imputable costs.
2. Costs are imputable for 40 years from the start of remediation measures.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ocach_debut_assainissement_annee(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Year when remediation measures began"
    reference = "SR 730.014.1 Art. 2 Abs. 2"


class ocach_couts_imputables_admis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether imputable costs can still be claimed (within 40-year window)"
    reference = "SR 730.014.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        debut = person('ocach_debut_assainissement_annee', period)
        p = parameters(period).sr_730_014_1
        duree_max = p.duree_couts_imputables_ans

        annee_courante = period.start.year
        return (annee_courante - debut) <= duree_max


class ocach_perte_production_kwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual electricity production loss due to remediation measures (kWh)"
    reference = "SR 730.014.1 Art. 2 Abs. 1"


class ocach_mesures_affectent_exploitation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether remediation measures affect the plant's operation"
    reference = "SR 730.014.1 Art. 2 Abs. 1"
