"""SR 744.211 Art. 18

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_valid_heavy_motor_vehicle_license(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person holds a valid driver's license for heavy motor vehicles"
    reference = "SR 744.211 Art. 18 Abs. 3-4"

    def formula(person, period, parameters):
        return person('heavy_motor_vehicle_license_valid', period)


class trolleybus_training_theoretical_completed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trainee has completed theoretical instruction (traffic rules, vehicle technology, electrical systems, operational specifics) before practical training"
    reference = "SR 744.211 Art. 18 Abs. 2"

    def formula(person, period, parameters):
        traffic_rules = person('trolleybus_instruction_traffic_rules_done', period)
        technical = person('trolleybus_instruction_vehicle_technology_done', period)
        electrical = person('trolleybus_instruction_electrical_systems_done', period)
        operational = person('trolleybus_instruction_operational_specifics_done', period)
        return traffic_rules * technical * electrical * operational


class trolleybus_training_must_start_with_heavy_truck(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trainee must begin practical training with a heavy truck (no valid heavy vehicle license held)"
    reference = "SR 744.211 Art. 18 Abs. 3"

    def formula(person, period, parameters):
        has_license = person('has_valid_heavy_motor_vehicle_license', period)
        return ~has_license


class trolleybus_training_may_start_directly_on_trolleybus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trainee may begin practical training directly on a trolleybus (holds valid heavy vehicle license)"
    reference = "SR 744.211 Art. 18 Abs. 4"

    def formula(person, period, parameters):
        return person('has_valid_heavy_motor_vehicle_license', period)


class trolleybus_partial_exam_passed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trainee without prior heavy vehicle license has passed the first part of the driver's exam (Art. 19 Abs. 4) before proceeding to trolleybus"
    reference = "SR 744.211 Art. 18 Abs. 3"

    def formula(person, period, parameters):
        must_start_with_truck = person('trolleybus_training_must_start_with_heavy_truck', period)
        partial_exam_done = person('trolleybus_driver_partial_exam_completed', period)
        # Only applicable for those who needed heavy truck phase; others are not subject to this requirement
        return (~must_start_with_truck) + (must_start_with_truck * partial_exam_done)


class trolleybus_training_hours_completed(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total hours the trainee has driven a trolleybus or heavy motor vehicle and trolleybus combined (including apprenticeship period)"
    reference = "SR 744.211 Art. 18 Abs. 6"

    def formula(person, period, parameters):
        return person('trolleybus_driving_hours_logged', period)


class trolleybus_final_exam_admission_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trainee meets the minimum 60-hour driving requirement for admission to the final trolleybus driver's exam"
    reference = "SR 744.211 Art. 18 Abs. 6"

    MINIMUM_HOURS = 60.0

    def formula(person, period, parameters):
        hours = person('trolleybus_training_hours_completed', period)
        return hours >= trolleybus_final_exam_admission_eligible.MINIMUM_HOURS


class trolleybus_learner_drive_permitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Learner drive on a trolleybus is permitted (accompanied by a person holding the trolleybus driver's license)"
    reference = "SR 744.211 Art. 18 Abs. 7"

    def formula(person, period, parameters):
        accompanied = person('trolleybus_learner_accompanied_by_license_holder', period)
        return accompanied


class trolleybus_exclusive_training_approved(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Federal Office has approved exclusive trolleybus-only training for the trainee's company (company has full training facilities; cantonal authority consulted)"
    reference = "SR 744.211 Art. 18 Abs. 5"

    def formula(person, period, parameters):
        company_has_facilities = person('trolleybus_company_has_full_training_facilities', period)
        federal_office_approval = person('trolleybus_federal_office_exclusive_training_approval', period)
        cantonal_authority_consulted = person('trolleybus_cantonal_authority_consulted', period)
        return company_has_facilities * federal_office_approval * cantonal_authority_consulted
