"""SR 0.131.334.9 Art. 16

Generated from: ch/0/de/0.131.334.9.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person

class contract_termination_date(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Date of contract termination"

def formula(person, period, parameters):
    start_date = person("contract_start_date", period)
    notice_period = 6 * MONTH
    return start_date + notice_period
