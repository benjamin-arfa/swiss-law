"""SR 0.142.117.147 Art. 4

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class apprenticeship_compensation(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Compensation for apprenticeship training (Art. 4 of apprenticeship act)"

    def formula(person, period, parameters):
        return person("apprenticeship_training_compensation", period)
