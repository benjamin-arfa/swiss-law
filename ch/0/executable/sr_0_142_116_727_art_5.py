"""SR 0.142.116.727 Art. 5

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class restricted_foreign_employment(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Restriction on employment in foreign countries (Art. 5 SR 0.142.116.727)"

    def formula(person, period, parameters):
        employed_abroad = person("employed_in_foreign_countries", period)
        return ~employed_abroad
