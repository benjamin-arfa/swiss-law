"""SR 613.2 Art. 3a

Generated from: ch/613/de/613.2.md
Determination and distribution of resource equalization funds:
- Cantons below 70% of Swiss average get equalized to 86.5%
- Cantons between 70-100% get progressively reduced payments
- Ranking of cantons must not change through equalization
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class resource_equalization_payment(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual resource equalization payment to resource-weak canton (CHF)"
    reference = "SR 613.2 Art. 3a"

    def formula(person, period, parameters):
        rp_per_capita = person("resource_potential_per_capita", period)
        swiss_avg = person("swiss_average_resource_potential_per_capita", period)
        population = person("canton_population", period)
        is_weak = person("is_resource_weak_canton", period)

        rp_ratio = where(swiss_avg > 0, rp_per_capita / swiss_avg, 0)

        # Art. 3a Abs. 2 lit. a: below 70% -> equalize to 86.5%
        target_below_70 = 0.865 * swiss_avg
        payment_below_70 = (target_below_70 - rp_per_capita) * population

        # Art. 3a Abs. 2 lit. b: between 70-100% -> progressive reduction
        # At 70%, additional unit reduces payment by 90%
        gap = swiss_avg - rp_per_capita
        reduction_factor = where(rp_ratio < 0.7, 0, 0.9 * (rp_ratio - 0.7) / 0.3)
        payment_70_100 = gap * (1 - reduction_factor) * population

        payment = where(
            rp_ratio < 0.7,
            payment_below_70,
            where(rp_ratio < 1.0, payment_70_100, 0),
        )

        return is_weak * max_(payment, 0)
