"""SR 613.2 Art. 8

Generated from: ch/613/de/613.2.md
Sociodemographic burden equalization: The Confederation compensates cantons
excessively burdened by sociodemographic situation (poverty, elderly,
foreigners needing integration support, core cities of large agglomerations).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class eligible_for_sociodemographic_equalization(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether canton is eligible for sociodemographic burden equalization"
    reference = "SR 613.2 Art. 8"

    def formula(person, period, parameters):
        poverty = person("above_average_poverty_rate", period)
        elderly = person("above_average_elderly_rate", period)
        foreigners = person("above_average_integration_needs", period)
        core_city = person("is_core_city_of_large_agglomeration", period)
        return poverty + elderly + foreigners + core_city
