"""SR 0.107 Art. 46

Generated from: ch/0/de/0.107.md
"""

from openfisca_core.model_api import *

class convention_signature_state(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Signature status for the AHV Convention (SR 0.107, Art. 46)"

    def formula(country, period, parameters):
        return country.is_signatory_parameter("AHV_convention")

[/openfisca_variable]
