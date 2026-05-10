"""SR 0.142.116.919 Art. 7

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class person_taken_back(Variable):
    value_type = bool
    entity = Person
    definition_period = once
    label = "Is a person taken back after return (Art. 7 SR 0.142.116.919)"

    def formula(person, period, parameters):
        return person("met_conditions_under_art_4", period)

# Assuming the variable "met_conditions_under_art_4" is implemented elsewhere
