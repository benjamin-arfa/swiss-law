"""SR 0.142.391 Art. 6

Generated from: ch/0/de/0.142.391.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class transportation_by_own_vehicle(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Transport by own vehicle (Art. 6 SR 0.142.391)"

    def formula(person, period, parameters):
        return True
