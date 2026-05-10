"""SR 744.211 Art. 10

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vehicle_documentation_submission_required(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether plans, drawings and calculations must be submitted to the Federal Office for new vehicles or substantial modifications (SR 744.211 Art. 10 para. 1)"
    reference = "SR 744.211 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        is_new_vehicle = person('is_new_vehicle', period)
        has_substantial_modification = person('vehicle_has_substantial_modification', period)
        return is_new_vehicle + has_substantial_modification


class is_new_vehicle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the vehicle is a new vehicle requiring documentation submission"
    reference = "SR 744.211 Art. 10 Abs. 1"


class vehicle_has_substantial_modification(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the vehicle has undergone a subsequent substantial modification or conversion"
    reference = "SR 744.211 Art. 10 Abs. 1"


class vehicle_is_trailer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the vehicle is a trailer (Anhänger)"
    reference = "SR 744.211 Art. 10 Abs. 4"


class road_vehicle_documentation_required(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether road vehicle documentation (type sketch, chassis plan, brake schema, etc.) must be submitted per Art. 10 para. 2"
    reference = "SR 744.211 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        submission_required = person('vehicle_documentation_submission_required', period)
        is_trailer = person('vehicle_is_trailer', period)
        return submission_required * ~is_trailer


class trailer_documentation_required(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether trailer-specific documentation must be submitted per Art. 10 para. 4 (subsets of para. 2 and 3, plus coupling plans)"
    reference = "SR 744.211 Art. 10 Abs. 4"

    def formula(person, period, parameters):
        submission_required = person('vehicle_documentation_submission_required', period)
        is_trailer = person('vehicle_is_trailer', period)
        return submission_required * is_trailer


class electrical_high_voltage_documentation_required(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether electrical high-voltage equipment documentation must be submitted per Art. 10 para. 3"
    reference = "SR 744.211 Art. 10 Abs. 3"

    def formula(person, period, parameters):
        submission_required = person('vehicle_documentation_submission_required', period)
        is_trailer = person('vehicle_is_trailer', period)
        return submission_required * ~is_trailer


class federal_office_compliance_check_triggered(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the Federal Office must verify compliance with applicable legislation upon documentation submission"
    reference = "SR 744.211 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return person('vehicle_documentation_submission_required', period)
