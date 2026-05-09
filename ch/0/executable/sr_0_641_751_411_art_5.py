"""SR 0.641.751.411 Art. 5 - Revenue sharing: incentive environmental taxes

Art. 5: Revenues from incentive environmental taxes paid into common fund.
Each state receives its share of net revenues proportional to its
population relative to the combined population of both states.
Net revenue = total revenue - refunds - annual operating costs of OFDF.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class recettes_brutes_taxes_incitatives(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gross revenues from incentive environmental taxes (Art. 5 par. 1)"
    default_value = 0


class remboursements_taxes_incitatives(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Refunds of incentive environmental taxes (Art. 5 par. 3)"
    default_value = 0


class frais_exploitation_ofdf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual operating costs of OFDF and other enforcement authorities (Art. 5 par. 3)"
    default_value = 0


class recettes_nettes_taxes_incitatives(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net revenues from incentive environmental taxes (Art. 5 par. 3)"

    def formula(person, period, parameters):
        brutes = person("recettes_brutes_taxes_incitatives", period)
        remboursements = person("remboursements_taxes_incitatives", period)
        frais = person("frais_exploitation_ofdf", period)
        return max_(0, brutes - remboursements - frais)


class population_ch(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Swiss population per latest census (Art. 5 par. 2)"
    default_value = 8900000


class population_li(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Liechtenstein population per latest census (Art. 5 par. 2)"
    default_value = 39000


class part_li_taxes_incitatives(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Liechtenstein's share of net incentive tax revenues (Art. 5 par. 2)"

    def formula(person, period, parameters):
        recettes_nettes = person("recettes_nettes_taxes_incitatives", period)
        pop_ch = person("population_ch", period)
        pop_li = person("population_li", period)
        pop_totale = pop_ch + pop_li
        return where(pop_totale > 0, recettes_nettes * pop_li / pop_totale, 0)


class part_ch_taxes_incitatives(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Switzerland's share of net incentive tax revenues (Art. 5 par. 2)"

    def formula(person, period, parameters):
        recettes_nettes = person("recettes_nettes_taxes_incitatives", period)
        pop_ch = person("population_ch", period)
        pop_li = person("population_li", period)
        pop_totale = pop_ch + pop_li
        return where(pop_totale > 0, recettes_nettes * pop_ch / pop_totale, 0)
