"""SR 112 Art. 5

Generated from: ch/de/112.md

Reversion clause: if the Bundesrathaus ceases to serve the central
federal administration, property returns to Bern and CHF 500,000
must be repaid.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bundesrathaus_nicht_mehr_zentralverwaltung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Bundesrathaus nicht mehr der Zentralverwaltung dient"
    reference = "SR 112 Art. 5 Abs. 1"


class objekte_fallen_zurueck(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Objekte nach Art. 1 an die Gemeinde zurueckfallen"
    reference = "SR 112 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('bundesrathaus_nicht_mehr_zentralverwaltung', period)


class rueckerstattung_500000(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Eidgenossenschaft CHF 500000 zurueckerstatten muss"
    reference = "SR 112 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        return person('bundesrathaus_nicht_mehr_zentralverwaltung', period)
