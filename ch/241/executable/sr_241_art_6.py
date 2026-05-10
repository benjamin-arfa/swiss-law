"""SR 241 Art. 6

Generated from: ch/de/241.md

Violation of manufacturing and business secrets.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class geheimnisverrat_fabrikation_geschaeft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Fabrikations- oder Geschaeftsgeheimnisse unrechtmaessig verwertet oder mitgeteilt werden"
    reference = "SR 241 Art. 6"
