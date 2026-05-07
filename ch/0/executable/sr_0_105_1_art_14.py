"""SR 0.105.1 Art. 14

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *

class government_prison_access_rights(Variable):
    value_type = bool
    entity = Country
    definition_period = ANY
    label = 'Swiss government grant of access rights to prison visiting authorities'

    def formula(countries, period, parameters):
      government_authority = parameters(countries, period).miscellaneous.committee_for_prevention.access_rights
      return (government_authority == "unrestricted_access")
