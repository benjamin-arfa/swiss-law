"""SR 442.125.2 Art. 8

Generated from: ch/442/de/442.125.2.md

Bemessung Betriebsbeitraege: Max 50% der Kosten fuer Geschaeftstaetigkeit.
Freiwilligenarbeit kann als Eigenleistung bis 10% angerechnet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_geschaeftstaetigkeit_immateriell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer laufende Geschaeftstaetigkeit (CHF)"
    reference = "SR 442.125.2 Art. 8 Abs. 1"


class freiwilligenarbeit_betrag_immateriell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wert der Freiwilligenarbeit als Eigenleistung (CHF)"
    reference = "SR 442.125.2 Art. 8 Abs. 2"


class max_betriebsbeitrag_immateriell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Betriebsbeitrag fuer immaterielles Kulturerbe (max 50%)"
    reference = "SR 442.125.2 Art. 8"

    def formula(person, period, parameters):
        kosten = person('kosten_geschaeftstaetigkeit_immateriell', period)
        return kosten * 0.50


class max_freiwilligenarbeit_anrechenbar_betr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximal anrechenbare Freiwilligenarbeit (10% der Kosten)"
    reference = "SR 442.125.2 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('kosten_geschaeftstaetigkeit_immateriell', period)
        freiwillig = person('freiwilligenarbeit_betrag_immateriell', period)
        max_anrechenbar = kosten * 0.10
        import numpy as np
        return np.minimum(freiwillig, max_anrechenbar)
