"""SR 0.142.116.659 Art. 2

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class russia_deportation_status(Variable):
    value_type = str
    entity = Person
    definition_period = MONTH
    label = "Russian deportation status (Art. 2 SR 0.142.116.659)"

    def formula(person, period, parameters):
        last_application = person("last_deportation_request_date", period)
        return "pending_deportation" if last_application else "unknown_status"
