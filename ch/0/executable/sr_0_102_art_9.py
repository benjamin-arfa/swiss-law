"""SR 0.102 Art. 9

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Municipality


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
