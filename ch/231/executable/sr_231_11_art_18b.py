"""SR 231.11 Art. 18b

Generated from: ch/231/de/231.11.md

Antrag auf Hilfeleistung: BAZG entscheidet innert 40 Tagen.
Genehmigter Antrag gilt 2 Jahre und kann erneuert werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antrag_hilfeleistung_gestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Antrag auf Hilfeleistung beim BAZG gestellt wurde"
    reference = "SR 231.11 Art. 18b Abs. 1"


class unterlagen_vollstaendig_datum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum, ab dem die Unterlagen vollstaendig vorliegen"
    reference = "SR 231.11 Art. 18b Abs. 2"


class bazg_entscheidungsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer den Entscheid des BAZG in Tagen (40 Tage)"
    reference = "SR 231.11 Art. 18b Abs. 2"

    def formula(person, period, parameters):
        return 40


class antrag_geltungsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Geltungsdauer des genehmigten Antrags in Jahren (2 Jahre)"
    reference = "SR 231.11 Art. 18b Abs. 3"

    def formula(person, period, parameters):
        return 2


class antrag_kuerzere_geltungsdauer_beantragt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Antrag fuer eine kuerzere Geltungsdauer gestellt wird"
    reference = "SR 231.11 Art. 18b Abs. 3"
