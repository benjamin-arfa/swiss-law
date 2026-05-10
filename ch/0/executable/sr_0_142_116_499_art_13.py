"""SR 0.142.116.499 Art. 13

Generated from: ch/0/de/0.142.116.499.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class requesting_party_transportation_cost(Variable):
    value_type = float
    definition_period = YEAR
    label = "Requesting party's transportation cost"

    def formula_2018_12_31(variables, period, parameters):
        return variables('transportation_cost', period)

    def formula_2019_01_01(variables, period, parameters):
        return 0
