"""SR 442.132.3 Art. 4

Generated from: ch/442/de/442.132.3.md

Lohn Pro Helvetia Personal: Lohn in 13 Teilen. Max 5'000 CHF Praemie pro Person.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahreslohn_pro_helvetia(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahreslohn bei Pro Helvetia (CHF)"
    reference = "SR 442.132.3 Art. 4 Abs. 1"


class beschaeftigungsgrad(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschaeftigungsgrad (0-1)"
    reference = "SR 442.132.3 Art. 4 Abs. 3"
    default_value = 1.0


class monatslohn_pro_helvetia(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monatslohn bei Pro Helvetia (1/13 des Jahreslohns)"
    reference = "SR 442.132.3 Art. 4 Abs. 5"

    def formula(person, period, parameters):
        jahreslohn = person('jahreslohn_pro_helvetia', period.this_year)
        grad = person('beschaeftigungsgrad', period.this_year)
        return jahreslohn * grad / 13


class max_praemie_pro_helvetia(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Praemie fuer herausragende Leistungen (5'000 CHF)"
    reference = "SR 442.132.3 Art. 4 Abs. 6"
    default_value = 5000
