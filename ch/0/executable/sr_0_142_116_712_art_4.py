"""SR 0.142.116.712 Art. 4

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable


class entry_denial(Variable):
    value_type = bool
    definition_period = YEAR
    label = "Denial of entry or residence (Art. 4 SR 0.142.116.712)"

    def formula(person, period, parameters):
        return False  # Article 4 defines a right, doesn't introduce any conditions for its implementation
