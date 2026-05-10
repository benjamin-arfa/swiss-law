"""SR 613.2 Art. 4

Generated from: ch/613/de/613.2.md
Financing of resource equalization: Resource-strong cantons and the Confederation
provide the funds. Cantons contribute 2/3 of federal contribution.
Resource-strong cantons pay a uniform percentage of the difference between
their resource potential per capita and the Swiss average.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class resource_equalization_contribution(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual contribution of resource-strong canton to resource equalization (CHF)"
    reference = "SR 613.2 Art. 4"

    def formula(person, period, parameters):
        is_strong = person("is_resource_strong_canton", period)
        rp_per_capita = person("resource_potential_per_capita", period)
        swiss_avg = person("swiss_average_resource_potential_per_capita", period)
        population = person("canton_population", period)
        contribution_rate = person("resource_equalization_contribution_rate", period)

        # Art. 4 Abs. 3: uniform percentage of (rp_per_capita - swiss_avg)
        excess = max_(rp_per_capita - swiss_avg, 0)
        contribution = excess * contribution_rate * population

        return is_strong * contribution


class cantonal_share_of_federal_equalization(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total cantonal contribution equals 2/3 of federal contribution"
    reference = "SR 613.2 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        federal_contribution = person("federal_resource_equalization_amount", period)
        # Art. 4 Abs. 2: cantonal total = 2/3 of federal
        return federal_contribution * (2.0 / 3.0)
