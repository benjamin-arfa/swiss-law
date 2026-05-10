"""SR 194.2 Art. 7 - Finanzierung

Generated from: ch/194/de/194.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzierung_bewilligungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Die Bundesversammlung bewilligt jeweils fuer vier Jahre den Hoechstbetrag"
    reference = "SR 194.2 Art. 7"

    def formula(self, period, parameters):
        return 4
