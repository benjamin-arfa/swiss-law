"""SR 0.142.116.829 Art. 15

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class international_agreement_transportation_cost(
    Variable,
):
    value_type = float
    label = "International agreement transportation cost, exempted by the requesting state (Art. 15 SR 0.142.116.82X)"
    definition_period = MONTH

    def formula_1(self, scenario, period, parameters):
        return 0
