"""SR 0.103.2 Art. 43

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class un_related_benefits(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = UN-related benefits (Art. 43 SR 0.103.2)

    def formula(person, period, parameters):
        return False  # Variable currently always evaluates to False
