"""SR 831.26 Art. 3

Generated from: ch/831/de/831.26.md

Definition of institutions:
a) Workshops employing disabled persons who cannot work under normal conditions
b) Residential homes and supervised collective housing
c) Day centres for community, leisure and occupation programs
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_werkstaette(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einrichtung eine Werkstaette fuer invalide Personen ist"
    reference = "SR 831.26 Art. 3 Abs. 1 Bst. a"


class ist_wohnheim(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einrichtung ein Wohnheim oder betreutes kollektives Wohnen ist"
    reference = "SR 831.26 Art. 3 Abs. 1 Bst. b"


class ist_tagesstaette(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einrichtung eine Tagesstaette ist"
    reference = "SR 831.26 Art. 3 Abs. 1 Bst. c"


class ist_ifeg_institution(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einrichtung als Institution im Sinne des IFEG gilt"
    reference = "SR 831.26 Art. 3"

    def formula(person, period, parameters):
        werkstaette = person('ist_werkstaette', period)
        wohnheim = person('ist_wohnheim', period)
        tagesstaette = person('ist_tagesstaette', period)
        return werkstaette + wohnheim + tagesstaette > 0
