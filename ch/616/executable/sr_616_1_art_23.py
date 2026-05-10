"""SR 616.1 Art. 23

Generated from: ch/616/de/616.1.md
Payments: Financial aids and compensations may be paid out at the earliest
when expenses are immediately forthcoming. Before final determination,
no more than 80% may be paid out.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class max_advance_subsidy_payment(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum advance payment before final determination (CHF)"
    reference = "SR 616.1 Art. 23 Abs. 2"

    def formula(person, period, parameters):
        total_subsidy = person("approved_subsidy_amount", period)
        # Before final amount, at most 80% may be paid
        return total_subsidy * 0.80
