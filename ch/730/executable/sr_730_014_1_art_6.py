"""SR 730.014.1 Art. 6

Generated from: ch/730/fr/730.014.1.md

Art. 6 - Payment of compensation:
2. If average annual probable imputable costs >= CHF 100,000, the operator
   submits an annual cost summary within 6 months after fiscal year end.
3. If average annual probable imputable costs < CHF 100,000:
   - FOEN pays annually; first payment 1 year after measure start
   - Operator submits 5-year cost summary
   - FOEN adjusts compensation based on summary
   - Final settlement at end of compensation period
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ocach_couts_moyens_annuels_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Average annual probable imputable costs as set by decision (CHF)"
    reference = "SR 730.014.1 Art. 6 Abs. 2-3"


class ocach_versement_annuel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether annual detailed cost reporting is required (costs >= CHF 100,000)"
    reference = "SR 730.014.1 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        couts_moyens = person('ocach_couts_moyens_annuels_chf', period)
        p = parameters(period).sr_730_014_1
        return couts_moyens >= p.seuil_versement_annuel_chf


class ocach_periode_recapitulatif_ans(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Cost summary reporting period in years (1 if annual, 5 if below threshold)"
    reference = "SR 730.014.1 Art. 6 Abs. 2-3"

    def formula(person, period, parameters):
        versement_annuel = person('ocach_versement_annuel', period)
        p = parameters(period).sr_730_014_1
        return where(versement_annuel, 1, p.periode_recapitulatif_simplifie_ans)
