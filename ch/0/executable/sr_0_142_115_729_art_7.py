"""SR 0.142.115.729 Art. 7

Generated from: ch/0/de/0.142.115.729.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class notified_repatriation_arrangements(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Repatriation arrangements notified (Art. 7 SR 0.142.115.729)"

    def formula(person, period, parameters):
        notified = parameters(period).admin.notified_repatriation_arrangements
        return notified
