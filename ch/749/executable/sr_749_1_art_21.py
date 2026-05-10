"""SR 749.1 Art. 21

Generated from: ch/749/fr/749.1.md

Art. 21: Excavation material disposal.
- al. 2: Canton must designate disposal sites within 5 years of plan approval.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ltsm_delai_designation_sites_elimination(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Deadline for canton to designate material disposal sites (years from plan approval)"
    reference = "SR 749.1 Art. 21 al. 2"

    def formula(person, period, parameters):
        return parameters(period).sr_749_1.delai_designation_sites_elimination
