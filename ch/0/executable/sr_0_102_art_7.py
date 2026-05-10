"""SR 0.102 Art. 7

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class municipal_representative_conditions(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Conditions met for municipal representative duties (Art. 7 SR 0.102)"

    def formula(person, period, parameters):
        representative_free_from_others = \
            person("representative_free_from_others", period) | \
            person("representative_statute_satisfies_freedom", period)

        representative_compensated_adequately = \
            person("representative_compensated_adequately", period) | \
            person("representative_statute_satisfies_compensation", period)

        representative_compensated_for_work = \
            person("representative_compensated_for_work", period) | \
            person("representative_statute_satisfies_wages", period)

        return ((representative_compensated_adequately &
                representative_free_from_others) &
                representative_compensated_for_work)


class overall_meeting_conditions(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Conditions met for municipal representative duties overall (Art. 7 SR 0.102)"

    def formula(person, period, parameters):
        return municipal_representative_conditions(person, period, parameters)


class representative_compensated_adequately(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Adequately compensated as a municipal representative (Art. 7 SR 0.102)"

    def formula(person, period, parameters):
        representative_compensated_adequately = \
            person("representative_compensated_adequately", period) | \
            person("representative_statute_satisfies_compensation", period)
        return representative_compensated_adequately


class representative_free_from_others(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Free from other obligations as a municipal representative (Art. 7 SR 0.102)"

    def formula(person, period, parameters):
        representative_free_from_others = \
            person("representative_free_from_others", period) | \
            person("representative_statute_satisfies_freedom", period)
        return representative_free_from_others


class representative_compensated_for_work(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fairly remunerated for work as a municipal representative (Art. 7 SR 0.102)"

    def formula(person, period, parameters):
        representative_compensated_for_work = \
            person("representative_compensated_for_work", period) | \
            person("representative_statute_satisfies_wages", period)
        return representative_compensated_for_work
