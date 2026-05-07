"""SR 0.142.116.162 Art. 3

Generated from: ch/0/de/0.142.116.162.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class comply_with_host_law(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Compliance with host state (Art. 3 SR 0.142.116.162)"

    def formula(person, period, parameters):
        citizenship = person('country_of_citizenship', period)
        return 'CH' in citizenship or 'IT' in citizenship
