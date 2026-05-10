"""SR 0.142.117.587 Art. 2

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class young_professional(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Young professional (Art. 2 SR 0.142.117.587)"

    def formula(person, period, parameters):
        born_on = person("birth_date", period)
        age = (period.date - born_on).days / 365.25
        min_age = parameters(period).social_security.young_professional.min_age
        max_age = parameters(period).social_security.young_professional.max_age
        is_documented = person("has_vocational_training_document", period)

        vocational_training = parameters(period).social_security.young_professional.vocational_training
        has_min_training = person("has_vocational_training_duration", period) >= vocational_training
        return (age >= min_age) & (age <= max_age) & is_documented & (has_min_training | person("has_university_degree", period))
