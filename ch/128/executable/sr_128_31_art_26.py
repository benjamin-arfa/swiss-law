"""SR 128.31 Art. 26

Generated from: ch/128/de/128.31.md

Ordentliche Wiederholung: Defines the deadlines for routine repetition of
personnel security checks based on the check level and result.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_grundsicherheitspruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Grundsicherheitspruefung handelt"
    reference = "SR 128.31 Art. 26"


class ist_erweiterte_pruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine erweiterte Personensicherheitspruefung handelt"
    reference = "SR 128.31 Art. 26"


class sicherheitserklaerung_positiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Sicherheitserklaerung nach Art. 39 Abs. 1 Bst. a ISG ausgestellt wurde"
    reference = "SR 128.31 Art. 26 Abs. 1"


class funktion_armee_zivilschutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Funktion der Armee oder des Zivilschutzes handelt"
    reference = "SR 128.31 Art. 26 Abs. 3"


class voraussichtliche_restdauer_funktion_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Voraussichtliche Restdauer der Funktionsausuebung in Jahren"
    reference = "SR 128.31 Art. 26 Abs. 3"


class wiederholungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximalfrist fuer die ordentliche Wiederholung der Pruefung in Jahren"
    reference = "SR 128.31 Art. 26"

    def formula(person, period, parameters):
        import numpy as np
        grund = person('ist_grundsicherheitspruefung', period)
        erweitert = person('ist_erweiterte_pruefung', period)
        positiv = person('sicherheitserklaerung_positiv', period)
        # Positive: Grundsicherheit = 10 Jahre, erweitert = 5 Jahre
        # Nicht positiv (Abs. 1bis): Grundsicherheit = 5 Jahre, erweitert = 3 Jahre
        return np.where(
            positiv,
            np.where(grund, 10, np.where(erweitert, 5, 0)),
            np.where(grund, 5, np.where(erweitert, 3, 0))
        )


class grundsicherheitspruefung_wiederholung_entfaellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ordentliche Wiederholung der Grundsicherheitspruefung entfaellt"
    reference = "SR 128.31 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        armee = person('funktion_armee_zivilschutz', period)
        restdauer = person('voraussichtliche_restdauer_funktion_jahre', period)
        grund = person('ist_grundsicherheitspruefung', period)
        return armee * grund * (restdauer < 5)
