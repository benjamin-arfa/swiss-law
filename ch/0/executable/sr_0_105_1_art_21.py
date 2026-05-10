"""SR 0.105.1 Art. 21

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class no_sanctions_for_reporting_to_npm(Variable):
    value_type = bool
    entity = Person
    label = "No sanctions for reporting to national prevention mechanism"

    def formula(person, period, parameters):
        reporting_to_npm = person("reported_to_npm", period)
        return reporting_to_npm == 0

class explicit_consent_required_for_personal_data(Variable):
    value_type = bool
    entity = Person
    label = "Explicit consent required for personal data sharing"

    def formula(person, period, parameters):
        personal_data_shared = person("personal_data_shared", period)
        return personal_data_shared == 0
