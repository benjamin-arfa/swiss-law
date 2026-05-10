"""SR 0.142.113.149 Art. 4

Generated from: ch/0/de/0.142.113.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mistakenly_transferred(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person was mistakenly transferred (Art. 4 SR 0.142.113.149)"

    def formula(person, period, parameters):
        return parameters(period).migration.mistaken_transfer.was_within_time_limit
