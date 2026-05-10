"""SR 520.13 Art. 3

Generated from: ch/520/de/520.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class askbw_mitglied(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist Mitglied des Ausschusses Koordinierter Bereich Wetter (ASKBW)"
    reference = "SR 520.13 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        ist_direktor_meteoschweiz = person('ist_direktor_meteoschweiz', period)
        ist_vertreter_babs = person('ist_vertreter_babs_wetter', period)
        ist_vertreter_verteidigung = person('ist_vertreter_verteidigung_wetter', period)
        return ist_direktor_meteoschweiz + ist_vertreter_babs + ist_vertreter_verteidigung


class ist_direktor_meteoschweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist Direktorin oder Direktor von MeteoSchweiz"
    reference = "SR 520.13 Art. 3 Abs. 2 lit. a"


class ist_vertreter_babs_wetter(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist Vertreterin oder Vertreter des BABS im ASKBW"
    reference = "SR 520.13 Art. 3 Abs. 2 lit. b"


class ist_vertreter_verteidigung_wetter(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist Vertreterin oder Vertreter des koordinierten Wetterdienstes der Gruppe Verteidigung"
    reference = "SR 520.13 Art. 3 Abs. 2 lit. c"


class askbw_vorsitz(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Hat den Vorsitz des ASKBW"
    reference = "SR 520.13 Art. 3 Abs. 4"

    def formula(person, period, parameters):
        return person('ist_direktor_meteoschweiz', period)
