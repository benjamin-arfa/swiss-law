"""SR 0.106 Art. 18

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *


class european_human_rights_member(Variable):
    value_type = bool
    definition_period = YEAR
    label = "European human rights convention member (Art. 18 of the European Human Rights Convention)"

    def formula(ehr_country, period, parameters):
        invitee_or_member = ehr_country("invitee_or_member“, period)
        return invitee_or_member
