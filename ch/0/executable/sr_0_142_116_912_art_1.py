"""SR 0.142.116.912 Art. 1

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_belonging_to_slovenia(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belonging to Slovenia (Art. 1 SR 0.142.116.912)"

    def formula(person, period, parameters):
        return person("country_of_birth", period) == "Slovenia"


class has_slovenian_passport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has valid Slovenian passport (Art. 1 SR 0.142.116.912)"

    def formula(person, period, parameters):
        # Assume this information is provided in the database
        return person("has_slovenian_passport", period)


class does_not_intend_to_stay_for_3_months(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Does not intend to stay for 3 months in Switzerland (Art. 1 SR 0.142.116.912)"

    def formula(person, period, parameters):
        # Assume this intention is evaluated based on past behavior or other information
        return not person("stays_in_switzerland_for_3_months", period)


class does_not_exercise_work_in_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Does not exercise work in Switzerland (Art. 1 SR 0.142.116.912)"

    def formula(person, period, parameters):
        # Assume this condition is evaluated based on employment status in Switzerland
        return not person("exercises_work_in_switzerland", period)


class has_permit_to_enter_switzerland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has permit to enter Switzerland due to Slovenian citizenship (Art. 1 SR 0.142.116.912)"

    def formula(person, period, parameters):
        return (
            is_belonging_to_slovenia(person, period)
            & has_slovenian_passport(person, period)
            & does_not_intend_to_stay_for_3_months(person, period)
            & does_not_exercise_work_in_ch(person, period)
        )
