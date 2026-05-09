"""SR 510.81 Art. 6 - Verfahren und Voraussetzungen

Generated from: ch/510/de/510.81.md

Die zustaendige Stelle des VBS uebermittelt dem BAZG eine Liste der
verantwortlichen Personen mit Angabe der Fahrzeuge.
Steuerfreier Treibstoff kann verwendet werden, sofern:
a. Treibstoffbezugsausweis vorhanden
b. Fahrzeug in der Liste aufgefuehrt
c. dienstlicher Gebrauch
d. Bezug bei vom BAZG bezeichneten Stellen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_treibstoffbezugsausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die beguenstigte Person einen Treibstoffbezugsausweis besitzt"
    reference = "SR 510.81 Art. 6 Abs. 2 lit. a"


class fahrzeug_in_vbs_liste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Fahrzeug in der dem BAZG uebermittelten Liste aufgefuehrt ist"
    reference = "SR 510.81 Art. 6 Abs. 2 lit. b"


class fahrzeug_dienstlicher_gebrauch_pfp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Fahrzeug von PfP-Truppen oder dem zivilen Gefolge fuer den dienstlichen Gebrauch verwendet wird"
    reference = "SR 510.81 Art. 6 Abs. 2 lit. c"


class treibstoff_von_bazg_stelle_bezogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Treibstoff bei vom BAZG bezeichneten Lagern oder Tankstellen bezogen wird"
    reference = "SR 510.81 Art. 6 Abs. 2 lit. d"


class steuerfreier_treibstoff_verwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob steuerfreier Treibstoff verwendet werden kann (alle Voraussetzungen erfuellt)"
    reference = "SR 510.81 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        ausweis = person('hat_treibstoffbezugsausweis', period)
        liste = person('fahrzeug_in_vbs_liste', period)
        dienstlich = person('fahrzeug_dienstlicher_gebrauch_pfp', period)
        bazg = person('treibstoff_von_bazg_stelle_bezogen', period)
        return ausweis * liste * dienstlich * bazg
