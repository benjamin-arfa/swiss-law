"""SR 0.142.117.121 Art. 21

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_period_type(Variable):
    value_type = str
    entity = Period
    definition_period = ETERNITY
    label = "Period type under international agreements (Art. 21 SR 0.142.117.121)"

    def formula(period, parameters):
        # Implementation not required for the variable, as this task seems to be about classification
        # Assuming that the agreement type can be determined dynamically in the code, it can be directly returned here
        return "Diplomatic Agreement"
