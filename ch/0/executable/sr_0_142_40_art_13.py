"""SR 0.142.40 Art. 13

Generated from: ch/0/de/0.142.40.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stateless_person_status(Variable):
    value_type = bool
    label = "Stateless person status"
    default_value = False

    definition_period = YEAR

    def formula(stateless_person, period, parameters):
        return stateless_person('is_stateless_person', period)
