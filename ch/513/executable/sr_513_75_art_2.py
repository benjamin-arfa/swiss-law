"""SR 513.75 Art. 2

Generated from: ch/513/de/513.75.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class zivile_mittel_ausgeschoepft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mittel und Moeglichkeiten der betroffenen zivilen Behoerden sind ausgeschoepft"


class katastrophenhilfe_voraussetzung_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzung fuer militaerische Katastrophenhilfe erfuellt (Art. 2 SR 513.75)"
    reference = "SR 513.75 Art. 2"

    def formula(person, period, parameters):
        # Katastrophenhilfe kann geleistet werden bei einem Ereignis, das so
        # viele Schaeden verursacht, dass die zivilen Behoerden ihre Aufgaben
        # nicht selbst bewaeltigen koennen.
        return person('zivile_mittel_ausgeschoepft', period)
