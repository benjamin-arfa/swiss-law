"""SR 0.142.111.367 Art. 5

Generated from: ch/0/de/0.142.111.367.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class foreign_worker_cap(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Cap on foreign worker admissions (Art. 5)"

    def formula(hOUSEHOLD, period, parameters):
        return 400
