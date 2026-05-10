"""SR 442.1 Art. 34

Generated from: ch/442/de/442.1.md

Stiftungsrat Pro Helvetia: 7-9 Mitglieder, 4 Jahre Amtsdauer, einmalige
Wiederwahl. Abberufung aus wichtigen Gruenden moeglich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitglieder_stiftungsrat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Mitglieder des Stiftungsrats Pro Helvetia"
    reference = "SR 442.1 Art. 34 Abs. 1"


class stiftungsrat_zusammensetzung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zusammensetzung des Stiftungsrats gueltig ist (7-9 Mitglieder)"
    reference = "SR 442.1 Art. 34 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('anzahl_mitglieder_stiftungsrat', period)
        return (anzahl >= 7) * (anzahl <= 9)


class amtsdauer_stiftungsrat_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Amtsdauer eines Stiftungsratsmitglieds in Jahren"
    reference = "SR 442.1 Art. 34 Abs. 2"
    default_value = 4


class anzahl_amtsperioden_stiftungsrat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Bisherige Anzahl Amtsperioden als Stiftungsratsmitglied"
    reference = "SR 442.1 Art. 34 Abs. 2"


class wiederwahl_stiftungsrat_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Wiederwahl in den Stiftungsrat moeglich ist (max. 1 Wiederwahl)"
    reference = "SR 442.1 Art. 34 Abs. 2"

    def formula(person, period, parameters):
        perioden = person('anzahl_amtsperioden_stiftungsrat', period)
        return perioden < 2
