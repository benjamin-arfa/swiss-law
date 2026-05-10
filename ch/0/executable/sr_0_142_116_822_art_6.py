"""SR 0.142.116.822 Art. 6

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_exempted_from_fee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "SR-exempt from fee (Art. 6 of the bilateral agreement)"

    def formula(person, period, parameters):
        return (
            person("official_delegate", period)
            | person("member_of_government_or_parliament", period)
            | person("participating_in_scientific-cultural_and_artistic_activities", period)
            | person("student_or_doctoral_candidate", period)
            | person("taking_part_in_sport_events", period)
            | person("taking_part_in_exchange_programs", period)
            | person("disabled_or_acc_companion", period)
            | person("civic_society Representative", period)
            | person("humanitarian_reasons", period)
            | person("journalist", period)
            | person("transport_driver", period)
            | person("train_staff_member", period)
            | person("family_member_visiting_serb_citizen", period)
            | person("representative_of_traditional_religious_communities", period)
            | person("free_professional", period)
            | person("retiree", period)
            | person("child_under_6", period)
        )


class sr_fee(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "SR visa processing fee (Art. 6 of the bilateral agreement)"

    def formula(person, period, parameters):
        exempt = person("sr_exempted_from_fee", period)
        standard_fee = parameters(period).sr_standard_fee
        return (1 - exempt) * standard_fee
