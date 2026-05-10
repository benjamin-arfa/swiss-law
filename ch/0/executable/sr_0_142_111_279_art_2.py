"""SR 0.142.111.279 Art. 2

Generated from: ch/0/de/0.142.111.279.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nationality_verified(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Nationality verification status (Art. 2 SR 0.142.111.279)"

    def formula(person, period, parameters):
        presented_documents = person("presented_documents", period)
        diplomatic_support = person("diplomatic_support", period)
        national_verifications_means = parameters(period).nationality_verification_means
        return (presented_documents | diplomatic_support) & any(value for value in national_verifications_means)
