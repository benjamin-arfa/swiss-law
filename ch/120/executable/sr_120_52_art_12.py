"""SR 120.52 Art. 12

Generated from: ch/120/de/120.52.md

Aufbewahrungsdauer und Loeschung der Daten: Retention and deletion rules.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_ablauf_massnahme(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit Ablauf der Massnahme"
    reference = "SR 120.52 Art. 12"


class weitere_massnahme_eingetragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob waehrend der 3 Jahre eine weitere Massnahme eingetragen wurde"
    reference = "SR 120.52 Art. 12 Abs. 2"


class hoogan_daten_zu_loeschen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die HOOGAN-Daten geloescht werden muessen"
    reference = "SR 120.52 Art. 12"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_ablauf_massnahme', period)
        weitere = person('weitere_massnahme_eingetragen', period)

        # Abs. 1: Loeschung 3 Jahre nach Ablauf der Massnahme
        # Abs. 2: Verlaengerung bei weiterer Massnahme
        # Abs. 3: Absolute Frist von 10 Jahren
        absolut = jahre >= 10
        normal = not_(weitere) * (jahre >= 3)

        return absolut + normal > 0
