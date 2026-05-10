"""SR 831.131.11 Art. 1

Generated from: ch/831/de/831.131.11.md

Refugees in Switzerland: entitlement to ordinary and extraordinary
pensions of AHV/IV under same conditions as Swiss citizens.
Extraordinary pensions require 5 years uninterrupted residence.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_fluechtling(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person anerkannter Fluechtling ist"
    reference = "SR 831.131.11 Art. 1"


class wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Wohnsitz und gewoehnlichen Aufenthalt in der Schweiz hat"
    reference = "SR 831.131.11 Art. 1 Abs. 1"


class aufenthaltsdauer_schweiz_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Ununterbrochene Aufenthaltsdauer in der Schweiz in Jahren"
    reference = "SR 831.131.11 Art. 1 Abs. 2"


class fluechtling_anspruch_ordentliche_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch eines Fluechtlings auf ordentliche AHV/IV-Renten"
    reference = "SR 831.131.11 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        ist_fl = person('ist_fluechtling', period)
        wohnsitz = person('wohnsitz_schweiz', period)
        return ist_fl * wohnsitz


class fluechtling_anspruch_ausserordentliche_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch eines Fluechtlings auf ausserordentliche AHV/IV-Renten"
    reference = "SR 831.131.11 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        ist_fl = person('ist_fluechtling', period)
        wohnsitz = person('wohnsitz_schweiz', period)
        aufenthalt = person('aufenthaltsdauer_schweiz_jahre', period)
        return ist_fl * wohnsitz * (aufenthalt >= 5)
