"""SR 744.10 Art. 3a

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_foreign_road_transport_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the entity is a foreign road transport company operating in Switzerland"
    reference = "SR 744.10 Art. 3a"

    def formula(person, period, parameters):
        return person('has_foreign_registered_transport_company', period)


class has_foreign_registered_transport_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the person holds a foreign-registered road transport company"
    reference = "SR 744.10 Art. 3a"


class cross_border_transport_agreement_applies(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Whether a bilateral agreement between Switzerland and a third state on cross-border "
        "commercial passenger or freight transport applies to this company (Art. 3a para. 1 lit. a)"
    )
    reference = "SR 744.10 Art. 3a para. 1 lit. a"

    def formula(person, period, parameters):
        is_foreign = person('is_foreign_road_transport_company', period)
        outside_land_transport_agreement = person('outside_land_verkehrsabkommen_scope', period)
        no_cabotage = person('does_not_perform_cabotage_within_switzerland', period)
        return is_foreign * outside_land_transport_agreement * no_cabotage


class outside_land_verkehrsabkommen_scope(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the transport activity falls outside the scope of the Land Transport Agreement (SR 0.740.72)"
    reference = "SR 744.10 Art. 3a para. 1"


class does_not_perform_cabotage_within_switzerland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the transport company does not perform cabotage within Switzerland"
    reference = "SR 744.10 Art. 3a para. 1"


class participates_in_multilateral_road_freight_system(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Whether the company participates in the multilateral system of international road freight "
        "under the ECMT Protocol of 17 October 1953 (SR 0.740.1) (Art. 3a para. 1 lit. b)"
    )
    reference = "SR 744.10 Art. 3a para. 1 lit. b"

    def formula(person, period, parameters):
        is_foreign = person('is_foreign_road_transport_company', period)
        outside_lvk = person('outside_land_verkehrsabkommen_scope', period)
        no_cabotage = person('does_not_perform_cabotage_within_switzerland', period)
        return is_foreign * outside_lvk * no_cabotage


class eligible_for_deviation_from_swiss_transport_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Whether a foreign road transport company is eligible to deviate from certain Swiss "
        "transport law requirements as specified by the Federal Council in a bilateral agreement "
        "or multilateral decision (Art. 3a para. 2)"
    )
    reference = "SR 744.10 Art. 3a para. 2"

    def formula(person, period, parameters):
        agreement = person('cross_border_transport_agreement_applies', period)
        multilateral = person('participates_in_multilateral_road_freight_system', period)
        return agreement + multilateral


class subject_to_eu_aligned_road_transport_admission_rules(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Whether the company is subject to admission rules aligned with EU regulations on "
        "road transport operators as updated by the Federal Council under Art. 3a para. 3 "
        "(approval of changes to Annexes 1, 3 and 4 of the Land Transport Agreement)"
    )
    reference = "SR 744.10 Art. 3a para. 3"

    def formula(person, period, parameters):
        is_foreign = person('is_foreign_road_transport_company', period)
        return is_foreign
