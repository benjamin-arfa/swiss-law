"""SR 0.142.116.907 Art. 2

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trainee_permit_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for trainee permit (Art. 2 SR 0.142.116.907)"

    def formula(person, period, parameters):
        employment_start = person("employment_start", period)
        employment_end = person("employment_end", period)
        permit_durations = person("trainee_permit_duration", period)
        training_durations = person("stay_duration", period)

        if period.start.date() >= employment_start and period.start.date() <= employment_end:
            if employment_start < employment_end:
                training_duration = min(period.duration, permit_durations) + employment_duration
            else:
                training_duration = 0

        elif period.start.date() < employment_start:
            training_duration = 0

        elif period.start.date() > employment_end:
            training_duration = 0

        else:
            training_duration = 0

        return training_duration >= 0

class employment_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Employment duration (job start to end)"

    def formula(person, period, parameters):
        employment_start = person("employment_start", period)
        employment_end = person("employment_end", period)
        current_date = period.start.date()

        if current_date >= employment_start and current_date <= employment_end:
            return (employment_end - employment_start).days / 30

        elif current_date < employment_start:
            return 0

        else:
            return 0

class training_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Training duration"

    def formula(person, period, parameters):
        training_start = person("training_start", period)
        training_end = person("training_end", period)

        return (training_end - training_start).days / 30
