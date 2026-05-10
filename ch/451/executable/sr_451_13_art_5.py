"""SR 451.13 Art. 5

Generated from: ch/451/de/451.13.md
Nachfuehrung - vollstaendige Ueberpruefung innert 25 Jahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class letzte_vollstaendige_ueberpruefung_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der letzten vollstaendigen Ueberpruefung des Bundesinventars"
    reference = "SR 451.13 Art. 5 Abs. 1"


class naechste_ueberpruefung_faellig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vollstaendige Ueberpruefung ist faellig (mehr als 25 Jahre seit letzter)"
    reference = "SR 451.13 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        letzte = person('letzte_vollstaendige_ueberpruefung_jahr', period)
        aktuelles_jahr = period.start.year
        return (aktuelles_jahr - letzte) > 25
