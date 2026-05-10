"""SR 143.1 Art. 1 - Ausweise (Identity Documents)

Generated from: ch/143/de/143.1.md

Every Swiss citizen is entitled to one identity document per document type.
Documents serve as proof of Swiss nationality and personal identity.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schweizer_staatsangehoerig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Schweizer Staatsangehoerige/r ist"
    reference = "SR 143.1 Art. 1 Abs. 1"


class anspruch_auf_ausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf einen Ausweis je Ausweisart"
    reference = "SR 143.1 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_schweizer_staatsangehoerig', period)
