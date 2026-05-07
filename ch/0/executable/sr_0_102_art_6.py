"""SR 0.102 Art. 6

Generated from: ch/0/de/0.102.md
"""

There is no direct implementation of this legal article in OpenFisca yet.
However we will define a variable to capture the concept of hiring staff based on merit.
from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class staff_recall_hire(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label: str = "Staff recall based on performance (Art. 6 para 2 SR 0.102)"

    def formula(person, period, parameters):
        return person("performance", period)
