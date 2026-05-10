"""SR 0.131.334.9 Art. 16

Generated from: ch/0/de/0.131.334.9.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class contract_termination_date(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Date of contract termination"

def formula(person, period, parameters):
    start_date = person("contract_start_date", period)
    notice_period = 6 * MONTH
    return start_date + notice_period
