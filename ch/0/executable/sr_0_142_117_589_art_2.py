"""SR 0.142.117.589 Art. 2

Generated from: ch/0/de/0.142.117.589.md
"""

from openfisca_core.model_api import *

class extradition_definitions(Variable):
    value_type = str
    label = "Extradition treaty definitions (SR 0.142.117.589 Art. 2)"

    def formula(person, period, parameters):
        return "Definitions of the above-mentioned terms are used in this variable."
