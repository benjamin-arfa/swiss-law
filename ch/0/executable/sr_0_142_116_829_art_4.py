"""SR 0.142.116.829 Art. 4

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_repatriation_candidate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is subject to repatriation (Art. 4 SR 0.142.116.829)"

    def formula(person, period, parameters):
        is_swiss = person("has_swiss_citizenship", period)

        residing_in_Republic_of_Serbia = person("residing_in_Republic_of_Serbia", period)
        meets_requirements = residing_in_Republic_of_Serbia

        is_unaccompanied_minor_child = (person("is_unaccompanied_minor_child", period)) & \
                                      (~person("has_own_residency_permit", period))

        is_spouse_with_other_nationality = (person("is_spouse_with_other_nationality", period)) & \
                                         ((~person("has_own_residency_permit", period)) | \
                                         (~person("is_spouse", period)))

        has_abandoned_swiss_citizenship = person("has_abandoned_swiss_citizenship", period)

        return (is_swiss &  meets_requirements) | \
               is_unaccompanied_minor_child | \
               is_spouse_with_other_nationality | \
               has_abandoned_swiss_citizenship
