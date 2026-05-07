"""SR 0.103.3 Art. 3

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable


class prosecute_foreign_actions(Variable):
    value_type = bool
    entity = World
    definition_period = YEAR
    label = "Prosecute foreign actions in line with SR 0.103.3 (Art. 3)"

    def formula(world, period, parameters):
        prosecution_conducted = world("prosecution_conducted_foreign_actions", period)
        investigation_completed = world("foreign_actions_investigation_completed", period)

        return (prosecution_conducted & investigation_completed)
