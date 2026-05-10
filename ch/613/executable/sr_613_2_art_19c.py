"""SR 613.2 Art. 19c

Generated from: ch/613/de/613.2.md
Temporary cushioning measures for resource-weak cantons (2021-2025).
Fixed amounts per year, distributed per capita. Canton loses entitlement
permanently if resource potential rises above Swiss average.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class temporary_cushioning_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total temporary cushioning amount available for resource-weak cantons (CHF)"
    reference = "SR 613.2 Art. 19c Abs. 2"

    def formula(person, period, parameters):
        year = period.start.year
        # Art. 19c Abs. 2: fixed amounts per year
        amount = select(
            [year == 2021, year == 2022, year == 2023, year == 2024, year == 2025],
            [80000000.0, 200000000.0, 160000000.0, 120000000.0, 80000000.0],
            default=0,
        )
        return amount
