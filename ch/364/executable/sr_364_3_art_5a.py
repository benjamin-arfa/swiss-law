"""SR 364.3 Art. 5a

Generated from: ch/364/de/364.3.md

Bewaffnung von Angestellten der Militaerverwaltung des Bundes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class angestellter_gruppe_verteidigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ziviler Angestellter der Gruppe Verteidigung"
    reference = "SR 364.3 Art. 5a Abs. 1"


class besondere_gefaehrdung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist im Rahmen dienstlicher Aufgaben besonderen Gefaehrdungen ausgesetzt"
    reference = "SR 364.3 Art. 5a Abs. 1"


class hinderungsgruende_dienstwaffe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hinderungsgruende zum Tragen einer Dienstwaffe liegen vor (Selbst-/Drittgefaehrdung)"
    reference = "SR 364.3 Art. 5a Abs. 3"


class grundausbildung_absolviert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Grundausbildung gemaess Vorgaben der Gruppe Verteidigung absolviert"
    reference = "SR 364.3 Art. 5a Abs. 6 Bst. a"


class jaehrliche_ausbildungskurse_absolviert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlich an mehreren Ausbildungskursen teilgenommen"
    reference = "SR 364.3 Art. 5a Abs. 6 Bst. b"


class berechtigt_dienstwaffe_tragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Berechtigt zum Tragen einer Dienstwaffe"
    reference = "SR 364.3 Art. 5a Abs. 1"

    def formula(person, period, parameters):
        angestellt = person('angestellter_gruppe_verteidigung', period)
        gefaehrdet = person('besondere_gefaehrdung', period)
        hinderung = person('hinderungsgruende_dienstwaffe', period)
        ausbildung = person('grundausbildung_absolviert', period)
        kurse = person('jaehrliche_ausbildungskurse_absolviert', period)
        return angestellt * gefaehrdet * not_(hinderung) * ausbildung * kurse
