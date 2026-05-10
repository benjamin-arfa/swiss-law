"""SR 232.14 Art. 7b

Generated from: ch/232/de/232.14.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class monate_vor_anmeldedatum_offenbart(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Monate vor dem Anmeldedatum, in denen die Erfindung offenbart wurde"
    reference = "SR 232.14 Art. 7b"


class offenbarung_durch_missbrauch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Offenbarung geht auf offensichtlichen Missbrauch zum Nachteil des Patentbewerbers zurück"
    reference = "SR 232.14 Art. 7b lit. a"


class offenbarung_auf_internationaler_ausstellung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Offenbarung auf offizieller oder offiziell anerkannter internationaler Ausstellung"
    reference = "SR 232.14 Art. 7b lit. b"


class offenbarung_unschaedlich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Offenbarung zählt nicht zum Stand der Technik (Neuheitsschonfrist)"
    reference = "SR 232.14 Art. 7b"

    def formula(person, period, parameters):
        monate = person('monate_vor_anmeldedatum_offenbart', period)
        missbrauch = person('offenbarung_durch_missbrauch', period.this_year)
        ausstellung = person('offenbarung_auf_internationaler_ausstellung', period.this_year)
        # Innerhalb von 6 Monaten vor Anmeldedatum und durch Missbrauch oder Ausstellung
        innerhalb_6_monate = monate <= 6
        grund = missbrauch + ausstellung
        return innerhalb_6_monate * grund
