"""SR 0.101.094 Art. 1

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class art_101094_1(Variable):
    value_type = bool
    label = "Benefit due to article SR 0.101.094 Art. 1"
    definition_period = ETERNITY

    add_description = 'benefit granted due to article SR 0.101.094 Art. 1'

    def formula_2020_01(definition_process, period, datasets, parameters):
        # Assuming the benefit applies if the person is above the threshold
        # This is a placeholder value and should be replaced with the correct
        # threshold in the formula
        threshold = parameters(period).art_101094_1_threshold
        return 1 - 1 * (datasets('person').available_vars() < threshold)
