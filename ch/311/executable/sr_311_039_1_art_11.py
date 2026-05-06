"""SR 311.039.1 Art. 11

Generated from: ch/311/de/311.039.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class leistungsvertrag_max_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer eines Leistungsvertrags (4 Jahre)"
    reference = "SR 311.039.1 Art. 11 Abs. 4"
    default_value = 4
