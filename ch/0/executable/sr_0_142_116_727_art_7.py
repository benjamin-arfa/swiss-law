"""SR 0.142.116.727 Art. 7

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *

class residence_permit_status(Variable):
    value_type = str
    entity = Person
    definition_period = MONTH
    label = "Residence permit status of the person (Art. 7 SR 0.142.116.727)"

    def formula(person, period, parameters):
        # Based on actual implementation details that would depend on real data sources
        # For demonstration purposes, return the person's nationality
        nationality = person("nationality", period)
        return nationality
