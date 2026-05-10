"""SR 0.142.117.147 Art. 2

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eligible_stagiaire(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility as stagiaire/Trainee (Art. 2 SR 0.142.117.147)"

    def formula(person, period, parameters):
        born_on = person("birth_date", period)

        min_age = 18
        max_age = 30

        age = (period.date - born_on).days / 365.25

        return (age >= min_age) & (age <= max_age)
