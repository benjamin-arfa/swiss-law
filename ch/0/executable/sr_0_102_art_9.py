"""SR 0.102 Art. 9

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class municipality_financial_autonomy(Variable):
    value_type = float
    entity = Municipality
    definition_period = YEAR
    label = "Municipality financial autonomy index"

    def formula(municipality, period, parameters):
        income = municipality("revenue", period)
        expenses = municipality("expenditure", period)
        autonomy_index = income / expenses
        return autonomy_index
