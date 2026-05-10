"""SR 321.0 Art. 36

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class freiheitsstrafe_dauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Freiheitsstrafe in Monaten"
    reference = "SR 321.0 Art. 36"


class vorstrafe_freiheitsstrafe_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frueherer Freiheitsstrafenumfang in Monaten (letzte 5 Jahre vor der Tat)"
    reference = "SR 321.0 Art. 36 Abs. 2"


class besonders_guenstige_umstaende(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegen besonders guenstige Umstaende vor"
    reference = "SR 321.0 Art. 36 Abs. 2"


class bedingter_strafvollzug_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bedingter Strafvollzug ist zulaessig (Freiheitsstrafe bis 2 Jahre)"
    reference = "SR 321.0 Art. 36 Abs. 1-2"

    def formula(person, period, parameters):
        dauer = person('freiheitsstrafe_dauer_monate', period)
        vorstrafe = person('vorstrafe_freiheitsstrafe_monate', period)
        guenstig = person('besonders_guenstige_umstaende', period)

        # Abs. 1: Freiheitsstrafe hoechstens 2 Jahre (24 Monate)
        strafe_zulaessig = dauer <= 24

        # Abs. 2: Vorstrafe > 6 Monate in letzten 5 Jahren → nur bei besonders guenstigen Umstaenden
        vorstrafe_sperre = (vorstrafe > 6) * not_(guenstig)

        return strafe_zulaessig * not_(vorstrafe_sperre)
