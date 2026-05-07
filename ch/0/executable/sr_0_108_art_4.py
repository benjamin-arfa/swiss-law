"""SR 0.108 Art. 4

Generated from: ch/0/de/0.108.md
"""

from openfisca_core import parameters

class nondiscrimination_policy(Variable):
    value_type = bool
    entity = None
    label = "Implementation period of nondiscriminatory temporary special measures (SR 0.108 Art. 4)"
    definition_period = YEAR

    def formula(parameters, period, _):
        return False
