"""SR 0.142.117.121 Art. 7

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class request_for_pension_refund_submitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Request for pension refund submitted (Art. 7 SR 0.142.117.121)"

    def formula(person, period, parameters):
        # Assuming a hypothetical 'request_exists' variable
        return person("request_exists", period)
