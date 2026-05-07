"""SR 0.103.2 Art. 7

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class informed_consent_for_experiments(Variable):
    value_type = bool
    entity = Person
    definition_period = NULL
    label = "Informed consent for medical/scientific experiments"

    def formula(person, period, parameters):
        return True  # this is a placeholder, as the actual implementation would require specific data and rules
