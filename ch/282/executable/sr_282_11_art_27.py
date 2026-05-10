"""SR 282.11 Art. 27 - Widerruf der Stundung

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class stundung_gewaehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Stundung wurde gewaehrt"
    reference = "SR 282.11 Art. 27 Abs. 1"


class voraussetzungen_stundung_nicht_mehr_vorliegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Voraussetzungen fuer die Stundung liegen nicht mehr vor"
    reference = "SR 282.11 Art. 27 Abs. 1 lit. a"


class schuldnerin_handelt_bedingungen_zuwider(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldnerin handelt den Stundungsbedingungen zuwider"
    reference = "SR 282.11 Art. 27 Abs. 1 lit. b"


class finanzlage_wesentlich_verschlechtert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die finanzielle Lage der Schuldnerin hat sich wesentlich verschlechtert"
    reference = "SR 282.11 Art. 27 Abs. 1 lit. c"


# Computed variables

class stundung_muss_widerrufen_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Stundung muss auf Antrag widerrufen werden"
    reference = "SR 282.11 Art. 27 Abs. 1"

    def formula(self, period, parameters):
        gewaehrt = self('stundung_gewaehrt', period)
        keine_voraussetzung = self('voraussetzungen_stundung_nicht_mehr_vorliegen', period)
        zuwider = self('schuldnerin_handelt_bedingungen_zuwider', period)
        verschlechtert = self('finanzlage_wesentlich_verschlechtert', period)
        grund = keine_voraussetzung + zuwider + verschlechtert > 0
        return gewaehrt * grund
