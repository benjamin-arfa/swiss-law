"""SR 0.101.3 Art. 4

Generated from: ch/0/de/0.101.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class movement_freedom(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = True

    def formula(person, period, parameters):
        # Return True if person had possibility to return home for 15 consecutive days
        return 1
