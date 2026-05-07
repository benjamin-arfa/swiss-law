"""SR 613.2 Art. 3

Generated from: ch/613/de/613.2.md
Resource potential: A canton's resource potential is the value of its fiscally
exploitable resources, calculated from taxable income, wealth, and corporate profits.
Cantons above average are resource-strong, below are resource-weak.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class resource_potential_per_capita(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Canton resource potential per capita (CHF)"
    reference = "SR 613.2 Art. 3"

    def formula(person, period, parameters):
        taxable_income = person("canton_aggregate_taxable_income", period)
        wealth = person("canton_aggregate_wealth", period)
        corporate_profits = person("canton_aggregate_corporate_profits", period)
        population = person("canton_population", period)
        # Simplified: resource potential is based on standardized tax yields
        resource_potential = taxable_income + wealth + corporate_profits
        return where(population > 0, resource_potential / population, 0)


class is_resource_strong_canton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the canton is resource-strong (above Swiss average)"
    reference = "SR 613.2 Art. 3 Abs. 5"

    def formula(person, period, parameters):
        rp_per_capita = person("resource_potential_per_capita", period)
        swiss_average = person("swiss_average_resource_potential_per_capita", period)
        return rp_per_capita > swiss_average


class is_resource_weak_canton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the canton is resource-weak (below Swiss average)"
    reference = "SR 613.2 Art. 3 Abs. 5"

    def formula(person, period, parameters):
        rp_per_capita = person("resource_potential_per_capita", period)
        swiss_average = person("swiss_average_resource_potential_per_capita", period)
        return rp_per_capita < swiss_average
