"""SR 0.103.2 Art. 8

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class forced_labour(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Forced labor status (Art. 8 SR 0.103.2)"

    def formula(person, period, parameters):
        # Check each exclusion condition
        is_prisoner = (person("sentence_start_date", period) <= period.start) & \
                     ((period.end - person("sentence_start_date")) + 1 < person("sentence_duration", period))
        is_conscientious_objector = person("is_conscientious_objector", period)
        is_military_service = person("is_military_service", period)
        is_civic_duty = person("is_civic_duty", period)
        is_emergency_response = person("is_emergency_response", period)
        is_servitude = person("is_servitude", period)

        return not(is_prisoner | is_conscientious_objector | is_military_service | is_civic_duty | is_emergency_response | is_servitude)
