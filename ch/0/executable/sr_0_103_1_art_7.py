"""SR 0.103.1 Art. 7

Generated from: ch/0/de/0.103.1.md
"""

]
from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class minimum_wage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Guaranteed minimum monthly salary (Art. 7a SR 0.103.1)"

    def formula(person, period, parameters):
        return parameters(period).social_security.minimum_wage

class equal_pay(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Equal pay for equal work in public and private sector (Art. 7a SR 0.103.1)"

    def formula(person, period, parameters):
        job_type = person("job_type", period)
        return job_type == "public"
