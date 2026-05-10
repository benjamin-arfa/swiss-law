"""SR 613.2 Art. 19

Generated from: ch/613/de/613.2.md
Hardship equalization: Transitional measure funded 2/3 by Confederation,
1/3 by cantons. Initial amount fixed for 8 years, then decreases by 5% per year.
Canton loses entitlement if resource potential rises above Swiss average.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class hardship_equalization_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hardship equalization payment to canton (CHF)"
    reference = "SR 613.2 Art. 19"

    def formula(person, period, parameters):
        is_weak = person("is_resource_weak_canton", period)
        initial_amount = person("hardship_equalization_initial_amount", period)
        years_since_start = person("years_since_filag_start", period)

        # Fixed for first 8 years, then decreases by 5% per year
        reduction_years = max_(years_since_start - 8, 0)
        reduction_factor = max_(1.0 - 0.05 * reduction_years, 0)
        amount = initial_amount * reduction_factor

        return is_weak * amount


class federal_share_hardship_equalization(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Federal share of hardship equalization (2/3)"
    reference = "SR 613.2 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        total = person("hardship_equalization_amount", period)
        return total * (2.0 / 3.0)
