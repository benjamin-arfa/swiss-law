"""SR 0.142.114.892 Art. 9

Generated from: ch/0/de/0.142.114.892.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import *
from dateutil.relativedelta import relativedelta


class ahv_agreement_in_effect(Variable):
    value_type = bool
    default_period = MONTH
    label = "AHV agreement in effect (Art. 9 SR 0.142.114.892)"

    def formula(period, parameters):
        last_notification_date = parameters('last_notification_date')# this would need to be either a date parameter, or a parameter storing a date of notification
        entry_date = last_notification_date + relativedelta(days=30)
        if period.start.date() >= entry_date - relativedelta(day=1):
            return True
        return False
