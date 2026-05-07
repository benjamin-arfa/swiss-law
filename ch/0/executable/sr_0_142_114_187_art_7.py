"""SR 0.142.114.187 Art. 7

Generated from: ch/0/de/0.142.114.187.md
"""

from openfisca_core.model_api import *


class annual_intern_quota(Variable):
    value_type = float
    entity = Country
    definition_period = YEAR
    label = "Annual intern quota (Art. 7 SR 0.142.114.187)"

    def formula(country, period):
        return 100
