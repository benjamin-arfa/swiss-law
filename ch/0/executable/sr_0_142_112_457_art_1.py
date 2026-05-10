"""SR 0.142.112.457 Art. 1

Generated from: ch/0/de/0.142.112.457.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_training_period(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Training period under the bi-lateral agreement (SR 0.142.112.457)"

    def formula(person, period, parameters):
        started_training = person("training_start_date", period)
        training_period_exists = person("training_period_exists", period)
        return (training_period_exists == 1) & (period > started_training)
