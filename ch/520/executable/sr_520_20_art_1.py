"""SR 520.20 Art. 1

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 1 (as amended 1 Jan 2024): Scope - this ordinance regulates the
# requisition of protective shelters and bed places for managing asylum
# emergencies.


class schutzanlage_requirierbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Schutzanlage ist grundsaetzlich requirierbar nach VRSL"
    reference = "SR 520.20 Art. 1"


class liegestelle_requirierbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Liegestelle aus oeffentlichem Schutzraum ist requirierbar nach VRSL"
    reference = "SR 520.20 Art. 1"
