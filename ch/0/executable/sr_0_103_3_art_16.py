"""SR 0.103.3 Art. 16

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca-switzerland.entities import Person


class ahv_human_rights_risk(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Assessed risk of human rights violations (Art. 16 SR 0.103.3)"

    def formula(person, period, parameters):
        country = parameters('country_of_residence')
        risk_level = parameters('state_human_rights_risk_level', country)

        countries_under_intensive_monitoring = parameters('countries_under_intensive_monitoring')
        systematic_human_rights_abuses = parameters('systematic_human_rights_abuses')

        return risk_level > 0 or (country in countries_under_intensive_monitoring) or systematic_human_rights_abuses
