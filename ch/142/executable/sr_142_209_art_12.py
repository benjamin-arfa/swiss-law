"""SR 142.209 Art. 12

Generated from: ch/142/de/142.209.md

Visumgebuehren:
- Standard-Visumgesuch: 90 EUR
- Visum fuer Kinder 6-12 Jahre: 45 EUR
Ermaessigung oder Erlass moeglich bei kulturellen, sportlichen,
aussenpolitischen Interessen oder humanitaeren Gruenden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_visumantragsteller(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der Person, die das Visum beantragt"
    reference = "SR 142.209 Art. 12"


class visumgebuehr_eur(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Visumgebuehr in EUR"
    reference = "SR 142.209 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_visumantragsteller', period)
        # Kinder 6-12: 45 EUR, ab 13: 90 EUR
        return where((alter >= 6) * (alter <= 12), 45.0, 90.0)
