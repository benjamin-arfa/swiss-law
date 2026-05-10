"""SR 0.142.111.639 Art. 5

Generated from: ch/0/de/0.142.111.639.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Note: Since this variable isn't tied to an individual person, the 'variables' should
# be placed under the 'model' declaration like so:
# entities = ...
# variables = ...
# periods = ...

class transfer_deadline_response(Variable):
    value_type = float
    entity = None  # This is a country variable and should be changed later.
    definition_period = MONTH
    label = "Transfer deadline after request for taking charge (Art. 5 SR 0.142.111.639)"

    def formula( country, period, parameters ):
        maximum_deadline = parameters(country, period).asylum_maximum_transfer_deadline
        response_time = parameters(country, period).asylum_response_time
        return (response_time + maximum_deadline)

class transfer_deadline_extension(Variable):
    value_type = float
    entity = None
    definition_period = MONTH
    label = "Maximum transfer deadline extension in months (Art. 5 SR 0.142.111.639)"

    def formula( country, period, parameters ):
        return parameters(country, period).asylum_maximum_transfer_extension
