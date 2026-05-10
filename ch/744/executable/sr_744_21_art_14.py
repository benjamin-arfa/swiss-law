"""SR 744.21 Art. 14

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_driver_license_held(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person holds a valid trolleybus driver's license issued by the competent cantonal authority"
    reference = "SR 744.21 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        training_completed = person('trolleybus_driver_training_completed', period)
        examination_passed = person('trolleybus_driver_examination_passed', period)
        license_not_refused = person('trolleybus_driver_license_refusal_notified', period) == False
        license_not_withdrawn = person('trolleybus_driver_license_withdrawal_notified', period) == False
        return training_completed * examination_passed * license_not_refused * license_not_withdrawn


class trolleybus_driver_training_completed(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has completed trolleybus driver training as prescribed by Federal Council regulations"
    reference = "SR 744.21 Art. 14 Abs. 1"


class trolleybus_driver_examination_passed(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has passed the trolleybus driver examination as prescribed by Federal Council regulations"
    reference = "SR 744.21 Art. 14 Abs. 1"


class trolleybus_driver_license_refusal_notified(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Refusal of trolleybus driver's license has been communicated with supervisory authority reasoning"
    reference = "SR 744.21 Art. 14 Abs. 3"


class trolleybus_driver_license_withdrawal_notified(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Withdrawal of trolleybus driver's license has been communicated with supervisory authority reasoning"
    reference = "SR 744.21 Art. 14 Abs. 3"
