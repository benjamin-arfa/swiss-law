"""SR 0.142.311 Art. 19

Generated from: ch/0/de/0.142.311.md
"""

from openfisca_core.model_api import *
from openfisca_entities import Entity


class treaty_termination_date(Variable):
    value_type = datetime.date
    entity = Entity('contract')
    definition_period = YEAR
    label = "Date the Treaty came to an end"

    def formula(contract, period, parameters):
        on_year_notice = contract('notification_year', period)
        on_six_month_notice = contract('notification_six_month', period)

        six_month_after_notification = contract('notification_date', period) + relativedelta(months=6)
        one_year_after_notification = contract('notification_date', period) + relativedelta(years=1)

        return max(six_month_after_notification, one_year_after_notification)
