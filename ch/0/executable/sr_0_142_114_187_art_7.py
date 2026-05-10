"""SR 0.142.114.187 Art. 7

Generated from: ch/0/de/0.142.114.187.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class annual_intern_quota(Variable):
    value_type = float
    entity = Country
    definition_period = YEAR
    label = "Annual intern quota (Art. 7 SR 0.142.114.187)"

    def formula(country, period):
        return 100
