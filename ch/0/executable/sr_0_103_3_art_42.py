"""SR 0.103.3 Art. 42

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class ahv_signatory_optout(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "AHV signatory opt-out declaration status (Art. 42 SR 0.103.3)"
    metadata:
        alias: "ahv_signatory_optout"

    def formula(country, period, parameters):
        is_signatory = country("is_signatory_to_ahv_treaty", period)
        parameters_dict = parameters(period)
        signatory_optout_status = parameters_dict.country_optout_status.get(country.code)

        return is_signatory & signatory_optout_status
