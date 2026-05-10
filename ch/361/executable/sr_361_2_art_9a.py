"""SR 361.2 Art. 9a

Generated from: ch/361/de/361.2.md

Protokollierung der Loeschmutationen: Aufbewahrung 1 Jahr.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ipas_loeschmutationen_aufbewahrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsdauer der Loeschmutationen in Jahren"
    reference = "SR 361.2 Art. 9a"

    def formula(person, period, parameters):
        return person('ipas_loeschmutationen_aufbewahrung_jahre', period) * 0 + 1
