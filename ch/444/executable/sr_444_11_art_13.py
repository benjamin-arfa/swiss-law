"""SR 444.11 Art. 13

Generated from: ch/444/de/444.11.md

Finanzhilfen Wiedererlangung: Max 50'000 CHF. Nur an staatliche Behoerden
und internationale Organisationen. Vertragsstaat muss eigene Leistung erbringen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_staatliche_behoerde_oder_int_org(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine staatliche Behoerde oder int. Organisation handelt"
    reference = "SR 444.11 Art. 13 Abs. 1"


class vertragsstaat_eigene_leistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Vertragsstaat eine seiner Finanzkraft entsprechende Eigenleistung erbringt"
    reference = "SR 444.11 Art. 13 Abs. 3"


class anspruch_finanzhilfe_wiedererlangung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf Finanzhilfe zur Wiedererlangung besteht"
    reference = "SR 444.11 Art. 13"

    def formula(person, period, parameters):
        behoerde = person('ist_staatliche_behoerde_oder_int_org', period)
        eigenleistung = person('vertragsstaat_eigene_leistung', period)
        return behoerde * eigenleistung


class max_finanzhilfe_wiedererlangung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Finanzhilfe Wiedererlangung kulturelles Erbe (50'000 CHF)"
    reference = "SR 444.11 Art. 13 Abs. 2"
    default_value = 50000
