"""SR 0.142.116.727 Art. 2

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class young_skilled_worker(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Young skilled worker status (Art. 2 SR 0.142.116.727)"

    def formula(person, period, parameters):
        birth_date = person("birth_date", period)
        current_age = (period.date - birth_date).days / 365.25
        is_young = current_age >= 18 and current_age <= 35

        vocational_training_diploma = person("vocational_training_diploma", period)
        completed_vocational_training = person("years_of_vocational_training_completeness", period)
        completed_training = completed_vocational_training >= 2

        return vocational_training_diploma and completed_training and is_young
