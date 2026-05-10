"""SR 0.142.116.909 Art. 2

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nationality_verified(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Nationality verified for passport substitute request (Art. 2 SR 0.142.116.909)"

    def formula(person, period, parameters):
        nationality_documents_verified = person("nationality_documents_verified", period)
        nationality_verified_interview = person("nationality_verified_interview", period)

        return nationality_documents_verified | nationality_verified_interview
