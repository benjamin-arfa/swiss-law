"""SR 442.1 Art. 12a

Generated from: ch/442/de/442.1.md

Tarife an Musikschulen: Tarife fuer Kinder und Jugendliche bis Sekundarstufe II
muessen deutlich unter den Erwachsenentarifen liegen. Wirtschaftliche Situation
und musikalische Begabung sind zu beruecksichtigen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_kind_oder_jugendlicher_bis_sek_ii(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein Kind oder Jugendlicher bis Abschluss Sekundarstufe II ist"
    reference = "SR 442.1 Art. 12a Abs. 1"


class musikschule_von_kanton_oder_gemeinde_unterstuetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Musikschule von Kantonen oder Gemeinden unterstuetzt wird"
    reference = "SR 442.1 Art. 12a Abs. 1"


class tarif_erwachsene(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tarif fuer Erwachsene an der Musikschule (CHF)"
    reference = "SR 442.1 Art. 12a Abs. 1"


class musikalisch_begabt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als musikalisch begabt eingestuft wird"
    reference = "SR 442.1 Art. 12a Abs. 2"


class anspruch_reduzierter_musikschultarif(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf deutlich reduzierten Musikschultarif besteht"
    reference = "SR 442.1 Art. 12a Abs. 1"

    def formula(person, period, parameters):
        kind = person('ist_kind_oder_jugendlicher_bis_sek_ii', period)
        unterstuetzt = person('musikschule_von_kanton_oder_gemeinde_unterstuetzt', period)
        return kind * unterstuetzt
