"""SR 0.142.116.909 Art. 16

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class reimbursed_costs(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Reimbursement of transportation costs by the applicant's party (Art. 16 SR 0.142.116.909)"

    def formula(person, period, parameters):
        return True  # Cost reimbursement by the applicant party by default
