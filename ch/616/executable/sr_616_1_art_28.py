"""SR 616.1 Art. 28

Generated from: ch/616/de/616.1.md
Non-fulfilment or deficient fulfilment of financial aids:
- Total non-fulfilment despite warning: no payment or full refund + 5% interest
- Deficient fulfilment despite warning: proportional reduction or partial refund + 5%
- Hardship cases: partial or full waiver of refund
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class subsidy_refund_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amount to be refunded due to non-fulfilment of subsidized task (CHF)"
    reference = "SR 616.1 Art. 28"

    def formula(person, period, parameters):
        paid_amount = person("subsidy_amount_paid", period)
        warned = person("received_subsidy_warning", period)
        total_non_fulfilment = person("total_non_fulfilment_of_task", period)
        deficient_fulfilment = person("deficient_fulfilment_of_task", period)
        fulfilment_ratio = person("task_fulfilment_ratio", period)
        is_hardship = person("is_hardship_case", period)

        # Full refund for total non-fulfilment
        full_refund = warned * total_non_fulfilment * paid_amount

        # Proportional refund for deficient fulfilment
        partial_refund = warned * deficient_fulfilment * paid_amount * (1 - fulfilment_ratio)

        refund = full_refund + partial_refund

        # Hardship reduction
        return where(is_hardship, 0, refund)


class subsidy_refund_interest(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Interest on refunded subsidy amount at 5% per year (CHF)"
    reference = "SR 616.1 Art. 28"

    def formula(person, period, parameters):
        refund = person("subsidy_refund_amount", period)
        years_since_payment = person("years_since_subsidy_payment", period)
        return refund * 0.05 * years_since_payment
