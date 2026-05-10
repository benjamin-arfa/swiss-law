"""SR 836.21 Art. 13 - Financing of family compensation funds

Art. 13: Family compensation funds are financed by contributions, income
and withdrawals from the fluctuation reserve, and payments from any cantonal
burden-sharing scheme. The fluctuation reserve is adequate when it amounts
to at least 20% and at most 100% of average annual family allowance expenditure.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahresausgabe_familienzulagen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Average annual family allowance expenditure (Art. 13 par. 2 FamZV)"
    default_value = 0


class schwankungsreserve_bestand(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Current balance of the fluctuation reserve (Art. 13 par. 2 FamZV)"
    default_value = 0


class schwankungsreserve_minimum(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum adequate fluctuation reserve = 20% of avg annual expenditure (Art. 13 par. 2 FamZV)"

    def formula(person, period, parameters):
        return person("jahresausgabe_familienzulagen", period) * 0.20


class schwankungsreserve_maximum(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum adequate fluctuation reserve = 100% of avg annual expenditure (Art. 13 par. 2 FamZV)"

    def formula(person, period, parameters):
        return person("jahresausgabe_familienzulagen", period) * 1.00


class schwankungsreserve_angemessen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fluctuation reserve is within adequate range (Art. 13 par. 2 FamZV)"

    def formula(person, period, parameters):
        bestand = person("schwankungsreserve_bestand", period)
        minimum = person("schwankungsreserve_minimum", period)
        maximum = person("schwankungsreserve_maximum", period)
        return (bestand >= minimum) * (bestand <= maximum)
