"""SR 142.318 Art. 1

Generated from: ch/142/de/142.318.md

Gegenstand und Zweck: Massnahmen zur Sicherstellung der angemessenen
Unterbringung von Asylsuchenden und der Durchfuehrung von Asylverfahren
im Zusammenhang mit Covid-19.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_asylsuchend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person asylsuchend ist"
    reference = "SR 142.318 Art. 1"


class covid19_massnahmen_asyl_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Covid-19-Massnahmen im Asylbereich anwendbar sind"
    reference = "SR 142.318 Art. 1"

    def formula_2020_04(person, period, parameters):
        return person('ist_asylsuchend', period)
