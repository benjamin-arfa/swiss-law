"""SR 0.142.117.437 Art. 7

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class quota_beneficiary(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bilateral trainee quota beneficiary"

    def formula(person, period, parameters):
        return person("trainee_quota_applications", period) <= parameters(period).trainee_quotaquota_size
