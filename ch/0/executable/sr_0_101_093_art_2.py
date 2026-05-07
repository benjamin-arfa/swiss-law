"""SR 0.101.093 Art. 2

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.variables import Variable


class DeviationProhibited(Variable):
    label = "Deviation from the protocol is prohibited"
    definition_period = "P1Y"
    reference = "SR 0.101.093 Art. 2"

    def formula(var, self, period, parameters):
        return 1
