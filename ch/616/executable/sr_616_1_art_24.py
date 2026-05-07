"""SR 616.1 Art. 24

Generated from: ch/616/de/616.1.md
Late payment interest: If the authority has not paid the financial aid or
compensation within 60 days of due date, it owes 5% annual interest from that point.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class subsidy_late_payment_interest(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Late payment interest owed on overdue subsidy (CHF)"
    reference = "SR 616.1 Art. 24"

    def formula(person, period, parameters):
        overdue_amount = person("overdue_subsidy_amount", period)
        days_overdue = person("subsidy_days_overdue", period)
        # Interest only accrues after 60-day grace period
        effective_days = max_(days_overdue - 60, 0)
        # 5% annual interest
        interest = overdue_amount * 0.05 * effective_days / 365.0
        return interest
