"""SR 0.131.334.92 Art. 11

Generated from: ch/0/de/0.131.334.92.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_effect_month(Variable):
    value_type = int
    label = "Month of treaty effect (Art. 11 SR 0.131.334.92)"

    def formula(period, parameters):
        return period.start
