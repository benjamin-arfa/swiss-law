"""SR 442.125.2 Art. 9

Generated from: ch/442/de/442.125.2.md

Bemessung Projektbeitraege: Max 50% der Kosten pro Projekt.
Freiwilligenarbeit max 10% der Gesamtkosten anrechenbar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_projekt_immateriell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten pro Projekt immaterielles Kulturerbe (CHF)"
    reference = "SR 442.125.2 Art. 9 Abs. 1"


class max_projektbeitrag_immateriell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Projektbeitrag immaterielles Kulturerbe (max 50%)"
    reference = "SR 442.125.2 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        kosten = person('kosten_projekt_immateriell', period)
        return kosten * 0.50
