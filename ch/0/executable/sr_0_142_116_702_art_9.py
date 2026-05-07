"""SR 0.142.116.702 Art. 9

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country

class agreement_effective_date_swiss(Variable):
    value_type = date
    entity = Country
    definition_period = LEGISLATIVE_YEAR
    label = "Effective date of SR 0.142.116.702 agreement in Switzerland (Art. 9)"

    def formula(country, period, parameters):
        last_notification_swiss = country("notification_last_dispatch_date_swiss", period)
        return (last_notification_swiss + TIMEDAYS(30))
