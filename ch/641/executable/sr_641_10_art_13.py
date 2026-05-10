"""SR 641.10 Art. 13

Generated from: ch/641/de/641.10.md

Umsatzabgabe - Regel:
1. Gegenstand der Abgabe ist die entgeltliche Uebertragung von Eigentum
   an Urkunden, sofern eine Vertragspartei oder Vermittler Effektenhaendler ist.
2. Steuerbare Urkunden: inlaendische Obligationen, Aktien, Stammanteile,
   Genossenschaftsanteile, Partizipationsscheine, Genussscheine, Anteile an
   kollektiven Kapitalanlagen; gleichwertige auslaendische Urkunden.
3. Effektenhaendler: Banken, SNB, zentrale Gegenparteien; gewerbsmaessige
   Haendler/Vermittler; Gesellschaften mit >10 Mio CHF Aktiven in
   steuerbaren Urkunden; Bund/Kantone/Gemeinden mit >10 Mio CHF.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stg_ist_entgeltliche_uebertragung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine entgeltliche Uebertragung von Eigentum an steuerbaren Urkunden vorliegt"
    reference = "SR 641.10 Art. 13 Abs. 1"


class stg_urkunde_ist_steuerbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Urkunde steuerbar ist nach Art. 13 Abs. 2"
    reference = "SR 641.10 Art. 13 Abs. 2"


class stg_aktiven_steuerbare_urkunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Aktiven in steuerbaren Urkunden gemaess letzter Bilanz (CHF)"
    reference = "SR 641.10 Art. 13 Abs. 3 Bst. d"


class stg_ist_bank_oder_snb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine Bank, bankaehnliche Finanzgesellschaft oder die SNB ist"
    reference = "SR 641.10 Art. 13 Abs. 3 Bst. a"


class stg_ist_gewerbsmaessiger_haendler(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person gewerbsmaessig mit steuerbaren Urkunden handelt oder vermittelt"
    reference = "SR 641.10 Art. 13 Abs. 3 Bst. b"


class stg_ist_effektenhaendler_art13(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person als Effektenhaendler nach Art. 13 Abs. 3 gilt"
    reference = "SR 641.10 Art. 13 Abs. 3"

    def formula(person, period, parameters):
        ist_bank = person('stg_ist_bank_oder_snb', period)
        ist_haendler = person('stg_ist_gewerbsmaessiger_haendler', period)
        aktiven = person('stg_aktiven_steuerbare_urkunden', period)
        schwelle = parameters(period).sr_641_10.effektenhaendler_aktiven_schwelle

        # Art. 13 Abs. 3 Bst. d: Gesellschaften mit Aktiven > 10 Mio CHF
        ist_grosse_gesellschaft = aktiven > schwelle

        return (ist_bank + ist_haendler + ist_grosse_gesellschaft) > 0


class stg_umsatzabgabe_tatbestand_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Tatbestand der Umsatzabgabe erfuellt ist"
    reference = "SR 641.10 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        entgeltlich = person('stg_ist_entgeltliche_uebertragung', period)
        steuerbar = person('stg_urkunde_ist_steuerbar', period)
        ist_haendler = person('stg_ist_effektenhaendler_art13', period)
        return entgeltlich * steuerbar * ist_haendler
