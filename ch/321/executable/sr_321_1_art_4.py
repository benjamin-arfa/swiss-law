"""SR 321.1 Art. 4

Generated from: ch/321/de/321.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class anspruch_auf_schadenersatz_rehabilitierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Rehabilitierung begruendet einen Anspruch auf Schadenersatz oder Genugtuung (stets verneint)"
    reference = "SR 321.1 Art. 4"
    default_value = False
