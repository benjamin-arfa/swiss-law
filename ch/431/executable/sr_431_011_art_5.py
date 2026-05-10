"""SR 431.011 Art. 5

Generated from: ch/431/de/431.011.md

Kommission fuer die Bundesstatistik - hoechstens 25 Mitglieder, tritt zweimal jaehrlich zusammen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class statistikkommission_anzahl_mitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der Kommission fuer die Bundesstatistik"
    reference = "SR 431.011 Art. 5 Abs. 5"


class statistikkommission_zusammensetzung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusammensetzung der Statistikkommission ist zulaessig (hoechstens 25 Mitglieder)"
    reference = "SR 431.011 Art. 5 Abs. 5"

    def formula(person, period, parameters):
        return person('statistikkommission_anzahl_mitglieder', period) <= 25


class statistikkommission_sitzungen_pro_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Sitzungen der Statistikkommission pro Jahr (in der Regel 2)"
    reference = "SR 431.011 Art. 5 Abs. 5"
    default_value = 2
