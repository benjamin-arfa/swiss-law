"""SR 0.142.116.657 Art. 7

Generated from: ch/0/de/0.142.116.657.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class can_have_multiple_employments(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Permission for multiple employments during apprenticeship"

    def formula(person, period, parameters):
        original_employment = person("original_employment", period)
        can_change_job = parameters(period).social_security.apprenticeships.can_change_job
        return (not original_employment) & can_change_job

class has_multiple_employments(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has multiple employments during apprenticeship"

    def formula(person, period, parameters):
        return person("can_have_multiple_employments", period) & (not person("original_employment", period))
