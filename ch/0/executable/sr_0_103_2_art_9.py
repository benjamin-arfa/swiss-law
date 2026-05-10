"""SR 0.103.2 Art. 9

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class compensation_for_unfair_detention(Variable):
    value_type = float
    label = "Compensation for unfair detention (Art. 9 of the Constitution)"
    entity = Person
    definition_period = YEAR
    description = "Compensation support for individuals who were unfairly detained."

    def formula(person, period, parameters):
        return person('unfair_detention_duration', period) * parameters(period).compensation_for_unfair_detention.rate

class unfair_detention_duration(Variable):
    value_type = int
    label = "Unfair detention duration (days) (Art. 9 of the Constitution)"
    entity = Person
    definition_period = MONTH
    description = "The duration of unfair detention in days."

    def formula(person, period, parameters):
        release_date = person('release_date', period)
        incarceration_start = person('incarceration_start', period)
        return (release_date - incarceration_start).days
