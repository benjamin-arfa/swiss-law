"""SR 0.109 Art. 5

Generated from: ch/0/de/0.109.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import ETERNITY
from openfisca_core.variables import Variable
from openfisca_core.policies import percentage


class targeted_beneficiaries_percentage(Variable):
    value_type = float
    entity = Person
    definition_period = ETERNITY
    label = "Percentage of targeted persons with disabilities"

    def formula(person, period, parameters):
        total_pop = person("total_population", period)
        intended_beneficiaries = person("intended_beneficiaries_with_disability", period)
        return (targeted_beneficiaries / total_pop) * 100
