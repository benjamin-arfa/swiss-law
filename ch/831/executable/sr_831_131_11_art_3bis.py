"""SR 831.131.11 Art. 3bis

Generated from: ch/831/de/831.131.11.md

Stateless persons: Articles 1-3 apply equally to stateless persons.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_staatenlos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person staatenlos ist"
    reference = "SR 831.131.11 Art. 3bis"


class staatenlos_anspruch_ordentliche_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch einer staatenlosen Person auf ordentliche AHV/IV-Renten (wie Fluechtlinge)"
    reference = "SR 831.131.11 Art. 3bis i.V.m. Art. 1 Abs. 1"

    def formula(person, period, parameters):
        staatenlos = person('ist_staatenlos', period)
        wohnsitz = person('wohnsitz_schweiz', period)
        return staatenlos * wohnsitz


class staatenlos_anspruch_ausserordentliche_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch einer staatenlosen Person auf ausserordentliche AHV/IV-Renten"
    reference = "SR 831.131.11 Art. 3bis i.V.m. Art. 1 Abs. 2"

    def formula(person, period, parameters):
        staatenlos = person('ist_staatenlos', period)
        wohnsitz = person('wohnsitz_schweiz', period)
        aufenthalt = person('aufenthaltsdauer_schweiz_jahre', period)
        return staatenlos * wohnsitz * (aufenthalt >= 5)
