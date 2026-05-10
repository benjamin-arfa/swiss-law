"""SR 0.142.117.149 Art. 9

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportation_cost(Variable):
    value_type = float
    entity = Treaty
    label = "Transportation costs for treaty parties (Art. 9 SR 0.142.117.149)"

    def formula(treaty, period, parameters):
        return 0
