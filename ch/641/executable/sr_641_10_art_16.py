"""SR 641.10 Art. 16

Generated from: ch/641/de/641.10.md

Umsatzabgabe - Steuersaetze:
1. Die Abgabe wird auf dem Entgelt berechnet und betraegt:
   a. 1,5 Promille fuer von einem Inlaender ausgegebene Urkunden
   b. 3 Promille fuer von einem Auslaender ausgegebene Urkunden
2. Bei nicht-Geldentgelt ist der Verkehrswert massgebend.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stg_umsatzabgabe_entgelt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Entgelt fuer die Uebertragung von Urkunden (CHF)"
    reference = "SR 641.10 Art. 16 Abs. 1"


class stg_urkunde_ist_inlaendisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Urkunde von einem Inlaender ausgegeben wurde"
    reference = "SR 641.10 Art. 16 Abs. 1"


class stg_umsatzabgabe_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anwendbarer Umsatzabgabesatz (Promille)"
    reference = "SR 641.10 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        ist_inlaendisch = person('stg_urkunde_ist_inlaendisch', period)
        satz_inland = parameters(period).sr_641_10.umsatzabgabe_satz_inland
        satz_ausland = parameters(period).sr_641_10.umsatzabgabe_satz_ausland
        return where(ist_inlaendisch, satz_inland, satz_ausland)


class stg_umsatzabgabe_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der Umsatzabgabe (CHF)"
    reference = "SR 641.10 Art. 16"

    def formula(person, period, parameters):
        entgelt = person('stg_umsatzabgabe_entgelt', period)
        satz = person('stg_umsatzabgabe_satz', period)
        ist_befreit = person('stg_umsatzabgabe_befreit', period)
        return where(ist_befreit, 0, entgelt * satz)


class stg_umsatzabgabe_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Transaktion von der Umsatzabgabe befreit ist (Art. 14)"
    reference = "SR 641.10 Art. 14"
