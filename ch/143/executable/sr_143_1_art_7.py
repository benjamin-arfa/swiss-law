"""SR 143.1 Art. 7 - Entzug (Withdrawal of Identity Document)

Generated from: ch/143/de/143.1.md

A document is withdrawn if:
a) conditions for issuance are no longer met
b) clear identification is no longer possible
c) it contains false or unofficial entries or has been altered

After withdrawal upon annulment of citizenship, documents must be
returned within 30 days. After that, unreturned documents are
reported as lost in RIPOL.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ausstellungsvoraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Voraussetzungen fuer die Ausweisausstellung (noch) erfuellt sind"
    reference = "SR 143.1 Art. 7 Abs. 1 lit. a"


class eindeutige_identifizierung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine eindeutige Identifizierung noch moeglich ist"
    reference = "SR 143.1 Art. 7 Abs. 1 lit. b"


class ausweis_enthaelt_falsche_eintraege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Ausweis falsche oder nicht amtliche Eintraege enthaelt oder abgeaendert wurde"
    reference = "SR 143.1 Art. 7 Abs. 1 lit. c"


class ausweis_wird_entzogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Ausweis entzogen wird"
    reference = "SR 143.1 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        voraussetzungen = person('ausstellungsvoraussetzungen_erfuellt', period)
        identifizierung = person('eindeutige_identifizierung_moeglich', period)
        falsche_eintraege = person('ausweis_enthaelt_falsche_eintraege', period)
        return (1 - voraussetzungen) + (1 - identifizierung) + falsche_eintraege > 0


class rueckgabefrist_entzogener_ausweis_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist zur Rueckgabe entzogener Ausweise in Tagen"
    reference = "SR 143.1 Art. 7 Abs. 1ter"

    def formula(person, period, parameters):
        return 30
