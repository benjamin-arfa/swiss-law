"""SR 0.103.2 Art. 19

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_right_to_free_opinion(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right to free opinion (Art. 19 SR 0.103.2)"

    def formula(person, period, parameters):
        return True  # Everyone has the right to free opinion


class has_right_to_access_and_share_information(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right to access and share information (Art. 19 SR 0.103.2)"

    def formula(person, period, parameters):
        return True  # Everyone has the right to access and share information


class has_permission_to_access_restrictions(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Permission to access restrictions (Art. 19 SR 0.103.2)"

    def formula(person, period, parameters):
        restrictions_condition1 = person("has_right_pursuant_to_others", period)
        restrictions_condition2 = person("has_right_for_national_security", period)
        return restrictions_condition1 | restrictions_condition2


class has_right_pursuant_to_others(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right of others (Art. 19 SR 0.103.2)"

    def formula(person, period, parameters):
        return False


class has_right_for_national_security(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right for national security (Art. 19 SR 0.103.2)"

    def formula(person, period, parameters):
        return False
