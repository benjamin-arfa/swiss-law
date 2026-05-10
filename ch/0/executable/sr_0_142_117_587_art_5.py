"""SR 0.142.117.587 Art. 5

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class allowed_job_change(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allowed job change for young professionals (Art. 5 SR 0.142.117.587)"

    def formula(person, period, parameters):
        age = (period.start.date() - person("birth_date")).days / 365.25
        return (age <= 30) & ((person("current_employment", period).occupation == person("desired_employment", period).occupation) | person("change_job_permission", period).allowed)
