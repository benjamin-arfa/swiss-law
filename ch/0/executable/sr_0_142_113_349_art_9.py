"""SR 0.142.113.349 Art. 9

Generated from: ch/0/de/0.142.113.349.md
"""

from openfisca_core.model_api import *

class refugees_may_not_be_affected(Variable):
    value_type = bool
    entity = Institution
    definition_period = YEAR
    label = "Exemption from AHVG provisions for refugees (Art. 9 SR 0.142.113.349)"

    def formula(institution, period, parameters):
        # The Swiss government has ratified the 1967 Refugee Protocol on January 31, 1967 (SR 0.142.301)
        effective_date = "1967-01-31"
        return (True, effective_date)
