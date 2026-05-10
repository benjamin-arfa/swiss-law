"""SR 451.51 Art. 9

Generated from: ch/451/de/451.51.md
Kommission - 9 bis 13 Mitglieder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitglieder_kommission_kulturlandschaft(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der Kommission fuer Finanzhilfe Kulturlandschaften"
    reference = "SR 451.51 Art. 9 Abs. 1"


class anzahl_mitglieder_kommission_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der Kommission ist zulaessig (9 bis 13)"
    reference = "SR 451.51 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('anzahl_mitglieder_kommission_kulturlandschaft', period)
        return (anzahl >= 9) * (anzahl <= 13)
