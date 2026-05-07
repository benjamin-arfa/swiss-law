"""SR 0.142.116.907 Art. 4

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class valid_stagiaire_activity(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Approved activity for stagiaire (Art. 4 SR 0.142.116.907)"

    def formula(person, period, parameters):
        return True  # Simple base case, adjust to actual parameters
        # Possible extension with parameters to influence zuständige Behörde's decision
