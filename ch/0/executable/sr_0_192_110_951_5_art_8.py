"""SR 0.192.110.951.5 Art. 8

Generated from: ch/0/de/0.192.110.951.5.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class potentially_expellable_opcw_personal(Variable):
    value_type = bool
    entity = Person
    definition_period = DUMMY_PERIOD
    label = "Potential OPCW personnel subject to Article 8 of Bilateral Agreement with OPCW"

    def formula(person, period, parameters):
        return person("is_opcw_personnel", period) & (person("activity_type") != "official_activities")
