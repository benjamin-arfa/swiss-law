"""SR 0.103.3 Art. 41

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
entity = Country


class convention_applicability(Variable):
    value_type = bool
    entity = entity
    definition_period = YEAR
    label = "Convention applicability status (Art. 41 SR 0.103.3)"

    def formula(countries, period, parameters):
        return True
