"""SR 0.101.1 Art. 6

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class PersonBindedByConvention(Variable):
    value_type = bool
    entity = Person
    label = 'Is the person bound by the convention?'
    definition_period = YEAR

    def formula(person, period, parameters):
        # This variable is set based on the convention.
        return person('is_party_to_convention'), period
