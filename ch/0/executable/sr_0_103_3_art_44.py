"""SR 0.103.3 Art. 44

Generated from: ch/0/de/0.103.3.md
"""

(Note: This model represents the process of adoption and potential entry into force for a country, rather than a specific numerical value.)

from openfisca_core.model_api import *

class international_social_security_convention_revision_status(Variable):
    value_type = bool
    entity = None
    definition_period = None
    label = "Status of International Social Security Convention revision adoption"

    def formula():
        return True
