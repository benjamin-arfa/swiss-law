"""SR 0.142.112.492 Art. 9

Generated from: ch/0/de/0.142.112.492.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import Month, YEAR
from openfisca_core.variables import Variable


class amendment_effective_date(Variable):
    value_type = Year
    default_value = YEAR.first
    label = "Effective date of amendments to the agreement between Switzerland and a particular country"

    def formula(person, period, parameters):
        notification_date = parameters('notification_date', period)
        return notification_date + Month(30)
