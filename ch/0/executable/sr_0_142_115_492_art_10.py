"""SR 0.142.115.492 Art. 10

Generated from: ch/0/de/0.142.115.492.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import (
    MONTH,
    YEAR,
)
from openfisca_core.variables import Variable
from openfisca_legislation import Legislation


class agreement_suspended_in_country(Variable):
    value_type = bool
    label = "Suspension of agreement in country (Art. 10)"
    entity = Legislation
    definition_period = ETERNITY
    allows_multiple = True

    def formula(country, time_slot, parameters):
        suspension_48_hours = country("suspension_notification_received", time_slot - 48 * HOUR)
        reason_for_suspension_met = country("suspension_applies", time_slot)
        return reason_for_suspension_met & ~suspension_48_hours

class suspension_applies(Variable):
    value_type = bool
    label = "Suspension applies due to public order/national security/public health (Art. 10)"
    entity = Legislation
    definition_period = ETERNITY
    allows_multiple = True

    def formula(country, time_slot, parameters):
        return country("suspension_granted", time_slot)
