"""SR 0.103.2 Art. 24

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Child


class child_acquired_name(Variable):
    value_type = bool
    entity = Child
    definition_period = YEAR
    label = "Child has acquired a name (Art. 24 SR)"

    def formula(child, period, parameters):
        birth_registration = child("birth_registration", period)
        name_acquired = child("name_acquired", period)
        return birth_registration & name_acquired
