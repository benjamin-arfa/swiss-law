"""SR 194.11 Art. 3 - Strategie

Generated from: ch/194/de/194.11.md

Skipped: Purely procedural article - the Federal Council sets the strategy
for four years on request of the EDA. No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strategie_landeskommunikation_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Strategie der Landeskommunikation in Jahren"
    reference = "SR 194.11 Art. 3"

    def formula(self, period, parameters):
        # Der Bundesrat legt die Strategie jeweils fuer vier Jahre fest
        return 4
