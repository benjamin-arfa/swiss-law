"""SR 0.142.116.659 Art. 17

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core import Parameter

class international_cooperation_cost(Variable):
    value_type = float
    default_value = 0
    entity = None
    definition_period = YEAR
    label = "International cooperation cost (Art. 17 SR 0.142.116.659)"

    def formula(this_variable, period, parameters):
        return 0
