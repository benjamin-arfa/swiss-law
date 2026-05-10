"""SR 151.31 Art. 7

Generated from: ch/151/de/151.31.md

Massgebliche Kosten: Berechnung der 5%-Schwelle basierend auf
Versicherungswert vor Erneuerung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class versicherungswert_vor_erneuerung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungswert des Gebaeudes vor der Erneuerung"
    reference = "SR 151.31 Art. 7 Abs. 1"


class baukosten_ohne_behindertenmassnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Voraussichtliche Baukosten ohne besondere Massnahmen fuer Behinderte"
    reference = "SR 151.31 Art. 7 Abs. 2"


class max_anpassungskosten_versicherungswert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anpassungskosten (5% des Versicherungswerts vor Erneuerung)"
    reference = "SR 151.31 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('versicherungswert_vor_erneuerung', period) * 0.05


class max_anpassungskosten_erneuerung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anpassungskosten (20% der Erneuerungskosten ohne Behindertenmassnahmen)"
    reference = "SR 151.31 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return person('baukosten_ohne_behindertenmassnahmen', period) * 0.20
