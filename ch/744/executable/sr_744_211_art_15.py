"""SR 744.211 Art. 15

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vehicle_is_new_rebuilt_or_acquired(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle is new, rebuilt, or taken over from another operator"
    reference = "SR 744.211 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        is_new = person('vehicle_is_new', period)
        is_rebuilt = person('vehicle_is_rebuilt', period)
        is_acquired_from_other = person('vehicle_acquired_from_other_operator', period)
        return is_new + is_rebuilt + is_acquired_from_other


class vehicle_requires_federal_office_authorization(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle requires Federal Office authorization before being put into service"
    reference = "SR 744.211 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        return person('vehicle_is_new_rebuilt_or_acquired', period)


class vehicle_must_be_reported_to_federal_office(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle must be reported to the Federal Office in time for official inspection scheduling"
    reference = "SR 744.211 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        return person('vehicle_is_new_rebuilt_or_acquired', period)


class vehicle_authorization_limited_to_test_drives(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Federal Office authorization is limited to test drives only"
    reference = "SR 744.211 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        return person('federal_office_authorization_scope_is_test_drive_only', period)


class test_vehicle_prohibited_from_passenger_transport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle designated as test vehicle is prohibited from carrying passengers"
    reference = "SR 744.211 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        return person('vehicle_authorization_limited_to_test_drives', period)


class vehicle_subject_to_periodic_federal_inspection(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle is subject to periodic inspection by the Federal Office"
    reference = "SR 744.211 Art. 15 Abs. 4"

    def formula(person, period, parameters):
        return person('vehicle_in_authorized_service', period)


class vehicle_subject_to_joint_post_accident_inspection(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle involved in traffic accident must undergo joint inspection by Federal Office and cantonal authority experts"
    reference = "SR 744.211 Art. 15 Abs. 4"

    def formula(person, period, parameters):
        return person('vehicle_involved_in_traffic_accident', period)


class trolleybus_inspection_may_be_delegated(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "For trolleybuses, the Federal Office may delegate follow-up inspections to qualified institutions, operators, or organizations"
    reference = "SR 744.211 Art. 15 Abs. 5"

    def formula(person, period, parameters):
        is_trolleybus = person('vehicle_is_trolleybus', period)
        delegate_qualifies = person('delegated_inspection_body_offers_guarantee_of_compliance', period)
        return is_trolleybus * delegate_qualifies


class trolleybus_delegated_inspector_must_report(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Delegated inspection body for trolleybus must report results of follow-up inspections to the Federal Office"
    reference = "SR 744.211 Art. 15 Abs. 5"

    def formula(person, period, parameters):
        return person('trolleybus_inspection_may_be_delegated', period)
