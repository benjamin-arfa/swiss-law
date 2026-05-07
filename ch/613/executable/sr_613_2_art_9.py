"""SR 613.2 Art. 9

Generated from: ch/613/de/613.2.md
Determination and distribution of burden equalization funds.
Base amounts from 2019 adjusted for inflation. Additional 80M (2021) and
140M (2022+) for sociodemographic equalization.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class geo_topographic_equalization_base_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Base amount for geographic-topographic equalization (CHF)"
    reference = "SR 613.2 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        # Base 2019: CHF 361,806,484, adjusted for inflation
        base_2019 = 361806484.0
        inflation_factor = person("cumulative_inflation_factor_from_2019", period)
        return base_2019 * inflation_factor


class sociodemographic_equalization_base_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Base amount for sociodemographic equalization (CHF)"
    reference = "SR 613.2 Art. 9 Abs. 2, 2bis"

    def formula(person, period, parameters):
        # Base 2019: CHF 361,806,484, adjusted for inflation
        base_2019 = 361806484.0
        inflation_factor = person("cumulative_inflation_factor_from_2019", period)
        base = base_2019 * inflation_factor

        # Art. 9 Abs. 2bis: additional amounts (not inflation-adjusted)
        year = period.start.year
        additional = where(year == 2021, 80000000.0,
                          where(year >= 2022, 140000000.0, 0))

        return base + additional
