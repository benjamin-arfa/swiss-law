"""SR 0.142.115.161 Art. 1

Generated from: ch/0/de/0.142.115.161.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class can_enter_lithuania_without_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Can enter Lithuania without a visa (SR-RL 0.142.115.161, Art. 1)"

    def formula(person, period, parameters):
        has_swiss_citizenship = person("has_swiss_citizenship", period)
        has_swiss_passport = person("has_swiss_passport", period)
        stays_short_term_in_lithuania = person("stays_short_term_in_lithuania", period)
        works_short_term_in_lithuania = person("works_short_term_in_lithuania", period)

        return (has_swiss_citizenship & has_swiss_passport & stays_short_term_in_lithuania & ~works_short_term_in_lithuania)
