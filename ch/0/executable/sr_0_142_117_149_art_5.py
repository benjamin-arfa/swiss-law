"""SR 0.142.117.149 Art. 5

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class consent_request_response_deadline(Variable):
    value_type = date
    variable_label = u"Date of response to return request"

    def formula(person, period, parameters):
        return person("request_date", period) + 15

class pickup_deadline_after_consent(Variable):
    value_type = date
    variable_label = u"Date of pickup after consent granted (Art. 5 para. 2 SR 0.142.117.149)"
    entity = Person

    def formula(person, period, parameters):
        consent_date = person("consent_date", period)
        if consent_date is not None:
            return consent_date + 30
        return consent_date
