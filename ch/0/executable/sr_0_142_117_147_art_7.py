"""SR 0.142.117.147 Art. 7

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class stagiaires_exchange_facilitation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Stagiaires exchange facilitation agreement (SR 0.142.117.147, Art. 7)"

    def formula(person, period, parameters):
        return True
