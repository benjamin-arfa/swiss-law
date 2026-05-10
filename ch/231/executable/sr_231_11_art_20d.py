"""SR 231.11 Art. 20d

Generated from: ch/231/de/231.11.md

Bearbeitung und Aufbewahrung von Personendaten: Daten duerfen
hoechstens 5 Jahre nach Ablauf des Antrags aufbewahrt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antrag_geltungsdauer_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Geltungsdauer des Antrags auf Hilfeleistung abgelaufen ist"
    reference = "SR 231.11 Art. 20d Abs. 3"


class hilfeleistung_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Hilfeleistung bereits erfolgt ist"
    reference = "SR 231.11 Art. 20d Abs. 3"


class maximale_datenaufbewahrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Aufbewahrungsdauer der Daten in Jahren (5 Jahre)"
    reference = "SR 231.11 Art. 20d Abs. 3"

    def formula(person, period, parameters):
        return 5


class ige_zustaendig_fuer_vollzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das IGE fuer den Vollzug des Verfahrens zustaendig ist"
    reference = "SR 231.11 Art. 20d Abs. 2"


class bazg_gibt_daten_an_ige(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BAZG die erforderlichen Daten an das IGE bekanntgibt"
    reference = "SR 231.11 Art. 20d Abs. 2"

    def formula(person, period, parameters):
        return person('ige_zustaendig_fuer_vollzug', period)
