"""SR 0.142.117.439 Art. 3

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class admitted_on_reentry_condition(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Condition for admission on re-entry (Article 3 of SR 0.142.117.439)"

    def formula(person, period, parameters):
        nationality = person("nationality", period)
        thirty_days_ago = period.last_month
        reentry_date = person("reentry_date", period)
        thirty_days_passed = (reentry_date > thirty_days_ago).astype(int)
        return (nationality == "requested_country_nationality") & thirty_days_passed
