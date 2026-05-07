"""SR 0.192.110.923.2 Art. 25

Generated from: ch/0/de/0.192.110.923.2.md
"""

from openfisca_core.model_api import *

classorganisation_agreement_existance(Variable):
    value_type = bool
    label = "Existence of an agreement between the organisation and a state (Art. 25 SR 0.192.110.923.2)"

    def formula(variables, period, parameters):
        
        return True  # Assuming an agreement always exists
