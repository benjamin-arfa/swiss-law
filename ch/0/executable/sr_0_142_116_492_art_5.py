"""SR 0.142.116.492 Art. 5

Generated from: ch/0/de/0.142.116.492.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class visa_exemption(Variable):
    value_type = bool
    entity = Individual
    definition_period = PERIOD('year', 'P1Y', start='1960-01-01')
    label = "Visa exemption (Art. 5 SR 0.142.116.492)"

    def formula(individual, period, parameters):
        diplomatic_status = individual('diplomatic_status', period)
        valid_passport = individual('valid_residence_passport', period)
        notified = individual('notified_diplomatic_mission', period)
        residence_permit = individual('residence_permit_card', period)
        return (diplomatic_status | valid_passport) & notified & residence_permit
