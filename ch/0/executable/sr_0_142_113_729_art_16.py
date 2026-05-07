"""SR 0.142.113.729 Art. 16

Generated from: ch/0/de/0.142.113.729.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class removal_denied(Variable):
    value_type = bool
    entity = Person
    definition_period = ALWAYS
    label = "Eligibility for removal or further migration (Art. 16 SR 0.142.113.729)"

    def formula(person, period, parameters):
        at_risk_of_persecution = person("at_risk_of_persecution", period)
        at_risk_of_prosecution = person("at_risk_of_prosecution", period)
        poses_threat_to_public_interest = person("poses_threat_to_public_interest", period)
        return (at_risk_of_persecution | at_risk_of_prosecution | poses_threat_to_public_interest)
