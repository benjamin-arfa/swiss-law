"""SR 0.142.116.919 Art. 12

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class boarding_refusal_resolution(Variable):
    value_type = bool
    definition_period = MONTH # or HOUR/DAY, depending on evaluation timeframe
    label = "Boarding refusal resolution (Article 12 of SR 0.142.116.919)"
    scope = "state"

    def formula(s, period, parameters):
        boarding_refusal = s("boarding_refusal", period)
        agreement = s("agreement_on_boarding_resolution", period)
        # option a: repatriation within 24 hours
        repatriation_ok = (s("repatriation_beginning_time", period) 
        	and s("repatriation_completion_time", period)
        	and (s("repatriation_completion_time") - s("repatriation_beginning_time")).days <= 24)
        # option b: new boarding and surveillance within 24 hours
        surveillance_ok = (s("surveillance_beginning_time", period) 
        	and s("surveillance_completion_time", period)
        	and (s("surveillance_completion_time") - s("surveillance_beginning_time")).days <= 24)
        return agreement == boarding_refusal or repatriation_ok or surveillance_ok
