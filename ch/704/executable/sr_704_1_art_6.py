"""SR 704.1 Art. 6

Generated from: ch/704/de/704.1.md

Ungeeignete Wanderwegbelaege: Bitumen, tar or cement-bound surface
coatings are unsuitable for hiking paths.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wanderweg_belag_bitumen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Wanderwegbelag bitumengebunden ist"
    reference = "SR 704.1 Art. 6"


class wanderweg_belag_teer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Wanderwegbelag teergebunden ist"
    reference = "SR 704.1 Art. 6"


class wanderweg_belag_zement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Wanderwegbelag zementgebunden ist"
    reference = "SR 704.1 Art. 6"


class wanderweg_belag_ungeeignet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Wanderwegbelag ungeeignet ist"
    reference = "SR 704.1 Art. 6"

    def formula(person, period, parameters):
        return (
            person('wanderweg_belag_bitumen', period) +
            person('wanderweg_belag_teer', period) +
            person('wanderweg_belag_zement', period)
        ) > 0
