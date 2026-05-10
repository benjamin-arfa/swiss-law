"""SR 0.108 Art. 4

Generated from: ch/0/de/0.108.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nondiscrimination_policy(Variable):
    value_type = bool
    entity = None
    label = "Implementation period of nondiscriminatory temporary special measures (SR 0.108 Art. 4)"
    definition_period = YEAR

    def formula(parameters, period, _):
        return False
