"""SR 425.15 Art. 7

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auslagen_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betrag der Auslagen in CHF (inkl. Kosten fuer Bibliotheken/Datenbanken)"
    reference = "SR 425.15 Art. 7 Abs. 1"


class auslagenpauschale_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SIR kann eine Auslagenpauschale in Rechnung stellen (Betrag unter 400 CHF)"
    reference = "SR 425.15 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        auslagen = person('auslagen_betrag', period)
        return auslagen < 400.0
