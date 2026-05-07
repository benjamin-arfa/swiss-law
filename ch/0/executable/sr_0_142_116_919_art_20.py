"""SR 0.142.116.919 Art. 20

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class transport_costs(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Transportation costs for job seekers (Art. 20 SR 0.142.116.919)"

    def formula(person, period, parameters):
        return (  # Cost associated with getting to border state and possibly returning
            # Costs of crossing borders (to be parameterized, may include visa costs)
            # Costs associated with travel, food, accommodation etc.
        )
Parameters (not included as per the question's requirements, but would typically include entries for visa costs, travel costs, accommodation costs)
