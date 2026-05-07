"""SR 0.105 Art. 11

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *


class torture_prevention_measures(Variable):
    value_type = bool
    label = "Torture prevention measures (Article 11 SR 0.105)"
    definition_period = YEAR
    unit = 1

    def formula_1999(period):
        return False

    def formula_2000(period):
        return False

    def formula_2001(period):
        return False
