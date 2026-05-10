"""SR 514.544.1 Art. 5

Generated from: ch/514/de/514.544.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class waffenhandel_theorie_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Theoretische Teilpruefung mit genuegend bewertet"


class waffenhandel_praxis_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Praktische Teilpruefung mit genuegend bewertet"


class waffenhandel_pruefung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pruefung fuer Waffenhandelsbewilligung bestanden (Art. 5 Abs. 2 SR 514.544.1)"
    reference = "SR 514.544.1 Art. 5"

    def formula(person, period, parameters):
        # Die Pruefung gilt als bestanden, wenn beide Teilpruefungen
        # mit genuegend bewertet werden.
        theorie = person('waffenhandel_theorie_genuegend', period)
        praxis = person('waffenhandel_praxis_genuegend', period)
        return theorie * praxis


class waffenhandel_wiederholung_theorie_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl bisherige Wiederholungen der theoretischen Teilpruefung"


class waffenhandel_wiederholung_praxis_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl bisherige Wiederholungen der praktischen Teilpruefung"


class waffenhandel_theorie_wiederholung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Theoretische Teilpruefung kann wiederholt werden (Art. 5 Abs. 3 SR 514.544.1)"
    reference = "SR 514.544.1 Art. 5"

    def formula(person, period, parameters):
        wiederholungen = person('waffenhandel_wiederholung_theorie_anzahl', period)
        # Hoechstens zweimal wiederholt werden
        return wiederholungen < 2


class waffenhandel_praxis_wiederholung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Praktische Teilpruefung kann wiederholt werden (Art. 5 Abs. 3 SR 514.544.1)"
    reference = "SR 514.544.1 Art. 5"

    def formula(person, period, parameters):
        wiederholungen = person('waffenhandel_wiederholung_praxis_anzahl', period)
        return wiederholungen < 2
