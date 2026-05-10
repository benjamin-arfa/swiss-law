"""SR 0.142.37 Art. 10

Generated from: ch/0/de/0.142.37.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class refugee_visa_status(Variable):
    value_type = bool
    entity = Government
    definition_period = None
    label = "Refugee visa status (Art. 10 SR 0.142.37)"

    def formula(government, period, parameters):
        return government("prepared_to_accept_refugee", period)
