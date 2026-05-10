"""SR 321.0 Art. 37

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class teilbedingter_strafvollzug_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Teilbedingter Strafvollzug ist zulaessig (Freiheitsstrafe 1-3 Jahre)"
    reference = "SR 321.0 Art. 37 Abs. 1"

    def formula(person, period, parameters):
        dauer = person('freiheitsstrafe_dauer_monate', period)
        return (dauer >= 12) * (dauer <= 36)


class unbedingter_teil_max_monate(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstdauer des unbedingten Teils (Haelfte der Strafe, mind. 6 Monate)"
    reference = "SR 321.0 Art. 37 Abs. 2-3"

    def formula(person, period, parameters):
        dauer = person('freiheitsstrafe_dauer_monate', period)
        haelfte = dauer * 0.5
        return where(haelfte < 6, 6, haelfte)
