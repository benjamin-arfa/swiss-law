"""SR 514.546.1 Art. 5

Generated from: ch/514/de/514.546.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class waffentrag_theorie_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Theoretische Teilpruefung Waffentragbewilligung mit genuegend bewertet"


class waffentrag_praxis_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Praktische Teilpruefung Waffentragbewilligung mit genuegend bewertet"


class waffentrag_pruefung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pruefung fuer Waffentragbewilligung bestanden (Art. 5 Abs. 2 SR 514.546.1)"
    reference = "SR 514.546.1 Art. 5"

    def formula(person, period, parameters):
        theorie = person('waffentrag_theorie_genuegend', period)
        praxis = person('waffentrag_praxis_genuegend', period)
        return theorie * praxis


class waffentrag_wiederholung_theorie_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl bisherige Wiederholungen der theoretischen Teilpruefung Waffentragbewilligung"


class waffentrag_wiederholung_praxis_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl bisherige Wiederholungen der praktischen Teilpruefung Waffentragbewilligung"


class waffentrag_theorie_wiederholung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Theoretische Teilpruefung Waffentragbewilligung kann wiederholt werden (Art. 5 Abs. 3 SR 514.546.1)"
    reference = "SR 514.546.1 Art. 5"

    def formula(person, period, parameters):
        wiederholungen = person('waffentrag_wiederholung_theorie_anzahl', period)
        return wiederholungen < 2


class waffentrag_praxis_wiederholung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Praktische Teilpruefung Waffentragbewilligung kann wiederholt werden (Art. 5 Abs. 3 SR 514.546.1)"
    reference = "SR 514.546.1 Art. 5"

    def formula(person, period, parameters):
        wiederholungen = person('waffentrag_wiederholung_praxis_anzahl', period)
        return wiederholungen < 2
