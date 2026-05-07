"""SR 613.2 Art. 7

Generated from: ch/613/de/613.2.md
Geographic-topographic burden equalization: The Confederation compensates cantons
excessively burdened by geographic-topographic situation (high-altitude settlements,
dispersed settlement structures, low population density).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class eligible_for_geo_topographic_equalization(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether canton is eligible for geographic-topographic burden equalization"
    reference = "SR 613.2 Art. 7"

    def formula(person, period, parameters):
        high_altitude = person("above_average_high_altitude_settlements", period)
        dispersed = person("has_dispersed_settlement_structure", period)
        low_density = person("has_low_population_density", period)
        return high_altitude + dispersed + low_density
