"""SR 0.142.117.437 Art. 1

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class is_eligible_foreign_worker(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for work exchange treaty between Switzerland and Czech Republic"

    def formula(person, period, parameters):
        host_country = parameters(period).geography.host_country
        foreign_worker_laws = parameters(period).laws.foreign_worker_laws[host_country]
        occupation = person("occupation", period)
        is_eligible_occupation = foreign_worker_laws.is_eligible_occupation(occupation)
        has_work visa = person("has_work Visa", period)

        return is_eligible_occupation & has_work visa
