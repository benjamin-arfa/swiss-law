"""SR 0.142.117.432 Art. 4

Generated from: ch/0/de/0.142.117.432.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class inadmissible_to_entry(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Reason for being inadmissible to entry (Art. 4 SR 0.142.117.432)"

    def formula(person, period, parameters):
        ineligibility_reasons = parameters(period).eligibility_reasons
        reasons = ["public_order_and_security", "illegalрезidense"]
        return person("reason_for_inadmissibility", period).isin(reasons) | person("reason_for_inadmissibility", period) in ineligibility_reasons
