"""SR 0.101.093 Art. 2

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class DeviationProhibited(Variable):
    label = "Deviation from the protocol is prohibited"
    definition_period = "P1Y"
    reference = "SR 0.101.093 Art. 2"

    def formula(var, self, period, parameters):
        return 1
