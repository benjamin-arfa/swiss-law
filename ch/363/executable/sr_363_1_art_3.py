"""SR 363.1 Art. 3

Generated from: ch/363/de/363.1.md

Kontrolle der Labors durch fedpol. Pruefzyklus mindestens alle 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class labor_letzte_kontrolle_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit der letzten Kontrolle des Labors durch fedpol"
    reference = "SR 363.1 Art. 3 Abs. 4"


class labor_kontrolle_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kontrolle der Leistungs- und Qualitaetsanforderungen ist faellig (alle 5 Jahre)"
    reference = "SR 363.1 Art. 3 Abs. 4"

    def formula(person, period, parameters):
        jahre = person('labor_letzte_kontrolle_jahre', period)
        return jahre >= 5
