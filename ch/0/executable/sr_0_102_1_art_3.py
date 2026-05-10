"""SR 0.102.1 Art. 3

Generated from: ch/0/de/0.102.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eligible_entity(Variable):
    value_type = bool
    label = "Eligible entity for Protocol application (SR 0.102.1 Art. 3)"

    def formula(e, period, parameters):
        state = parameters("state")
        # Assuming that parameters('state')[country] contains a list of applicable entities
        return e in list(parameters('state')[state])
