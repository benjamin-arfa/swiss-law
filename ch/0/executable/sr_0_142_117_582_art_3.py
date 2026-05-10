"""SR 0.142.117.582 Art. 3

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_valid_travel_document(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Travel document valid as per international agreement"

    def formula(person, period, parameters):
        travel_document = person("travel_document", period)
        return travel_document.is_valid


class complies_with_local_laws(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Compliance with local laws and regulations"

    def formula(person, period, parameters):
        passport_validity = person("passport_validity", period)
        return passport_validity >= parameters(period).general.passport_validity
