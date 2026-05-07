"""SR 531.211.36 Art. 2

Generated from: ch/531/de/531.211.36.md
Maximum quantity: The maximum quantity that can be released equals the difference
between demonstrated domestic demand and the quantity freely available on the market.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class max_stockpile_release_quantity(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Maximum quantity of rabies vaccine that can be released from mandatory stockpile"
    reference = "SR 531.211.36 Art. 2"

    def formula(person, period, parameters):
        domestic_demand = person("demonstrated_domestic_demand", period)
        freely_available = person("freely_available_market_quantity", period)
        return max_(domestic_demand - freely_available, 0)
