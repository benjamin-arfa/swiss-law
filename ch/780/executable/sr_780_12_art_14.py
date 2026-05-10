"""SR 780.12 Art. 14

Generated from: ch/780/de/780.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class daten_vernichtung_angewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Die zuletzt mit dem Verfahren befasste Behoerde hat den Dienst UePF "
        "vor Ablauf der Aufbewahrungsfrist zur Vernichtung der Daten angewiesen"
    )
    reference = "SR 780.12 Art. 14 Abs. 1"


class auskunftsdaten_speicherdauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Speicherdauer der Daten aus Auskuenften in Monaten (12 Monate)"
    reference = "SR 780.12 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        # Art. 14 Abs. 3: Daten aus Auskuenften werden waehrend
        # zwoelf Monaten gespeichert
        return 12
