"""SR 432.30 Art. 11

Generated from: ch/432/de/432.30.md

Museumsrat - 7 bis 9 Mitglieder, Amtsdauer 4 Jahre, einmal wiederwaehlbar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class museumsrat_anzahl_mitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder des Museumsrats"
    reference = "SR 432.30 Art. 11 Abs. 1"


class museumsrat_zusammensetzung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusammensetzung des Museumsrats ist zulaessig (7 bis 9 Mitglieder)"
    reference = "SR 432.30 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('museumsrat_anzahl_mitglieder', period)
        return (anzahl >= 7) * (anzahl <= 9)


class museumsrat_amtsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer des Museumsrats in Jahren"
    reference = "SR 432.30 Art. 11 Abs. 2"
    default_value = 4


class museumsrat_bereits_einmal_wiedergewaehlt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mitglied des Museumsrats wurde bereits einmal wiedergewaehlt"
    reference = "SR 432.30 Art. 11 Abs. 2"


class museumsrat_wiederwahl_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mitglied des Museumsrats kann wiedergewaehlt werden"
    reference = "SR 432.30 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return not_(person('museumsrat_bereits_einmal_wiedergewaehlt', period))
