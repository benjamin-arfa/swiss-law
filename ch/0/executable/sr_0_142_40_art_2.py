"""SR 0.142.40 Art. 2

Generated from: ch/0/de/0.142.40.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stateless_obligation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "General obligations of stateless persons (Art. 2 Ausländergesetz)"

    def formula(person, period, parameters):
        is_stateless = person("is_stateless", period)
        is_present_in_ch = person("is_present_in_switzerland", period)
        return is_stateless & is_present_in_ch
