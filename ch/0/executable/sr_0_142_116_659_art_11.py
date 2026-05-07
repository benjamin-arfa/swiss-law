"""SR 0.142.116.659 Art. 11

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class extradite_compliance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Compliance with Art. 11 on extraditing mistakenly extradited persons"

    def formula(person, period, parameters):
        entry_date = person("date_of_entry", period)
        current_date = period.date
        timedelta = current_date - entry_date
        return timedelta >= period.duration * 30
