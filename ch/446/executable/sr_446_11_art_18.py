"""SR 446.11 Art. 18

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_modellvorhaben_kantone_gemeinden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Qualifiziert als Modellvorhaben von Kantonen und Gemeinden nach Art. 11 KJFG"
    reference = "SR 446.11 Art. 18"

    def formula(person, period, parameters):
        einmalig = person('projekt_ist_einmalig', period)
        dauer = person('projekt_dauer_jahre', period)
        innovativ = person('projekt_hat_innovative_aspekte', period)
        uebertragbar = person('projekt_ist_uebertragbar', period)
        beduerfnis = person('projekt_beduerfnis_nachgewiesen', period)
        wissenstransfer = person('projekt_wissenstransfer_sichergestellt', period)
        return einmalig * (dauer <= 3) * innovativ * uebertragbar * beduerfnis * wissenstransfer
