"""SR 0.109 Art. 5

Generated from: ch/0/de/0.109.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class targeted_beneficiaries_percentage(Variable):
    value_type = float
    entity = Person
    definition_period = ETERNITY
    label = "Percentage of targeted persons with disabilities"

    def formula(person, period, parameters):
        total_pop = person("total_population", period)
        intended_beneficiaries = person("intended_beneficiaries_with_disability", period)
        return (targeted_beneficiaries / total_pop) * 100
