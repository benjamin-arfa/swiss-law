"""SR 171.117 Art. 7

Generated from: ch/171/de/171.117.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class amtsdauer_delegationspraesidium(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Präsidentin oder des Präsidenten einer Delegation in Jahren"
    reference = "SR 171.117 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return 2
