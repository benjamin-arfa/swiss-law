"""SR 0.103.2 Art. 35

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class un_employee_compensated(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "United Nations employee compensated by UN funds (SR 0.103.2 Art. 35)"

    def formula(person, period, parameters):
        return True
