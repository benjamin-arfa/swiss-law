"""SR 0.103.3 Art. 17

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_detained(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Is the person detained? (SR 0.103.3 Art. 17)"

    def formula(person, period, parameters):
        detention_registry = person('detention_registry', period)
        return person.in_(detention_registry)

class detention_registry(Variable):
    value_type = types.set
    entity = Person
    definition_period = DAY
    label = "Detention Registry (SR 0.103.3 Art. 17)"

    def formula(person, period, parameters):
        detained = includes_detained(person, period)
        return detained | includes_detained(person, period)

def includes_detained(individual, period):
    detention_records = individual('detention_history', period)
    return detention_records != []
