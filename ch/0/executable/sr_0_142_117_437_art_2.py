"""SR 0.142.117.437 Art. 2

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stagiaire_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility of person as stagiaire (Art. 2 SR 0.142.117.437)"

    def formula(person, period, parameters):
        age = (period.date - person("birth_date")).days / 365.25
        return age >= 18
