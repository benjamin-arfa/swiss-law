"""SR 0.102 Art. 8

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class administrative_oversight_compliance(Variable):
    value_type = bool
    definition_period = MONTH
    label = "Administrative oversight compliance (Art. 8 SR 0.102)"

    def formula(person, period, parameters):
        regulatory_impact = person("regulatory_impact", period)
        proportionality = parameters(period).administrative_rules.proportionality
        return regulatory_impact <= proportionality
