"""SR 0.120 Art. 84

Generated from: ch/0/de/0.120.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Entity, EntityDivision


class admin_involvement_in_security_matters(Variable):
    value_type = bool
    entity = EntityDivision
    definition_period = YEAR
    label = "Administering Authority use of Trust Territory resources"

    def formula(entity, period, parameters):
        mandate_purpose = parameters(period).international_affairs.sr_mandate_purpose
        assistance_requested_from_tt = parameters(period).international_affairs.assistance_requested_from_tt
        return (mandate_purpose == "preserve_world_peace") & (assistance_requested_from_tt == True)
        # further details would require more specific data.
