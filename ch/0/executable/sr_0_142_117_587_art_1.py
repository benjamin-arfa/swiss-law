"""SR 0.142.117.587 Art. 1

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_young_professional(Variable):
    value_type = bool
    label = "Definition of a young professional"
    definition_period = YEAR

    def formula_2015_12(variables, period, parameters):
        return (variables("is_young_professional_switzerland", period) | variables("is_young_professional_tunisia", period))

    def formula_2023_01(variables, period, parameters):
        return (variables("has_train_or_educational_activity_switzerland", period) | variables("has_train_or_educational_activity_tunisia", period))
