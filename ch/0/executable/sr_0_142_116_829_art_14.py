"""SR 0.142.116.829 Art. 14

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person

# Define a generic variable that will be updated with real data as it becomes available
class international_transfer_request_made(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "International transfer request made for person"

    def formula(person, period, parameters):
        return False  # This variable is for reference purposes only, not to be populated
