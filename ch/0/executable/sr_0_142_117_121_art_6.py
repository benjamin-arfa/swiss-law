"""SR 0.142.117.121 Art. 6

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person
import numpy as np


class extradition_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Transfer of 3rd country nationals and stateless individuals is eligible"

    def formula(person, period, parameters):
        entry_date = person("entry_date", period)
        current_date = period.date

        duration_in_days = (current_date - entry_date).days
        condition_1 = not person("resides_in_switzerland", period) | not person("works_in_switzerland", period)
        condition_2 = person("visa_or_residence_permit_from_requesting_state", period)
        condition_3 = duration_in_days > 365
        condition_4 = person("has_residence_permit_before_or_after_entry", period)
        condition_5 = (np.floor((current_date.year - entry_date.year)*12 + np.mod((current_date - entry_date).days,365 + 1)/365) > 12) & not person("has_residence_permit_before_or_after_entry", period)
        condition_6 = (person("transited_through_international_airport", period))
        condition = condition_1 & (condition_2 | condition_5 | condition_3 | condition_6 | (not condition_4))

        return condition
