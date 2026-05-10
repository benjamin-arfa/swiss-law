"""SR 0.142.116.659 Art. 12

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class enforcement_request_deadline(Variable):
    value_type = int
    entity = superEntity
    definition_period = PERIOD
    label = "Deadline for responding to an enforcement request (Art. 12 SR 0.142.116.659)"

    def formula(superEntity, period, parameters):
        return 25 if parameters(period).enforcement_request.response_period == "standard" else 60

class repatriation_deadline(Variable):
    value_type = int
    entity = superEntity
    definition_period = PERIOD
    label = "Repatriation deadline (Art. 12 SR 0.142.116.659)"

    def formula(superEntity, period, parameters):
        return 90 if parameters(period).repatriation_delay == "standard" else parameters(period).repatriation_delay.extended_value

class repatriation_delay_extension(Variable):
    value_type = float
    entity = superEntity
    definition_period = PERIOD
    label = "Extension for repatriation delay due to procedural or technical reasons (Art. 12 SR 0.142.116.659)"

    def formula(superEntity, period, parameters):
        return parameters(period).repatriation_delay.extension_value
