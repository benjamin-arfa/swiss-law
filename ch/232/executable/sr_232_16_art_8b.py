"""SR 232.16 Art. 8b

Generated from: ch/232/de/232.16.md

Art. 8b defines the conditions for a plant variety to be protectable:
it must be new, distinct, uniform, and stable.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sorte_ist_neu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Sorte ist neu (kein Verkauf in CH >1 Jahr, im Ausland >4 Jahre vor Anmeldung)"
    reference = "SR 232.16 Art. 8b Abs. 2"


class sorte_ist_unterscheidbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Sorte unterscheidet sich deutlich von jeder anderen bekannten Sorte"
    reference = "SR 232.16 Art. 8b Abs. 3"


class sorte_ist_homogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Sorte ist in ihren wesentlichen Merkmalen hinreichend einheitlich"
    reference = "SR 232.16 Art. 8b Abs. 4"


class sorte_ist_bestaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die wesentlichen Merkmale der Sorte bleiben nach Vermehrung unveraendert"
    reference = "SR 232.16 Art. 8b Abs. 5"


class sorte_ist_schutzfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Sorte erfuellt alle Voraussetzungen fuer Sortenschutz (neu, unterscheidbar, homogen, bestaendig)"
    reference = "SR 232.16 Art. 8b Abs. 1"

    def formula(person, period, parameters):
        neu = person('sorte_ist_neu', period)
        unterscheidbar = person('sorte_ist_unterscheidbar', period)
        homogen = person('sorte_ist_homogen', period)
        bestaendig = person('sorte_ist_bestaendig', period)
        return neu * unterscheidbar * homogen * bestaendig
