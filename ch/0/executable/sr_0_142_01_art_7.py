"""SR 0.142.01 Art. 7

Generated from: ch/0/de/0.142.01.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dummy_variable(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dummy variable"

    def formula(person, period, parameters):
        return 1
