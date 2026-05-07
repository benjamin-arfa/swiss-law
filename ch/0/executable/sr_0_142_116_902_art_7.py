"""SR 0.142.116.902 Art. 7

Generated from: ch/0/de/0.142.116.902.md
"""

If we interpret Art. 7 as a condition affecting the eligibility of individuals to receive benefits from one state while residing in the other, possible representations could involve:
* `resident_state_id`: An entity attribute representing the state where the individual resides.
* `benefits_eligibility`: A variable indicating whether an individual is eligible to receive benefits from their home state (i.e., the state they possess citizenship of) when residing in the other state.

Here is some simplified example code for these variables:

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person

class resident_state_id(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "State where the person resides"

    def formula(person, period, parameters):
        return person("residence_state_code", period)

class benefits_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Benefits eligibility while residing in another state (Art. 7 international agreement)"

    def formula(person, period, parameters):
        home_state_id = parameters(period).citizenship.home_state_id
        current_residence_id = person("residence_state_code", period)
        
        return (current_residence_id == home_state_id)
