"""SR 453.0 Art. 42

Generated from: ch/453/de/453.0.md
Fachgremium - hoechstens 9 Mitglieder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitglieder_cites_kommission(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der CITES-Kommission"
    reference = "SR 453.0 Art. 42 Abs. 2"


class anzahl_mitglieder_cites_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der CITES-Kommission ist zulaessig (hoechstens 9)"
    reference = "SR 453.0 Art. 42 Abs. 2"

    def formula(person, period, parameters):
        anzahl = person('anzahl_mitglieder_cites_kommission', period)
        return anzahl <= 9
