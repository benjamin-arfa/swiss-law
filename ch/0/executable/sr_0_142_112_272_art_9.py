"""SR 0.142.112.272 Art. 9

Generated from: ch/0/de/0.142.112.272.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class ahv_dispute_resolution(Variable):
    value_type = bool
    entity = None  # This variable is independent of individuals/persons
    definition_period = None  # It doesn't depend on time
    label = "Existence of disagreement on AHV interpretation or application"

    def formula(e, period, parameters):
        return True  # This always returns True; the logic is not about disputes, but about the existence of a treaty
