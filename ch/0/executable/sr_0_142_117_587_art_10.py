"""SR 0.142.117.587 Art. 10

Generated from: ch/0/de/0.142.117.587.md
"""

1. Assuming a `treaty` entity, we could define the treaty start date and end date as follows:

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class treaty_start_date(Variable):
    value_type = date
    entity = Treaty
    definition_period = YEARS
    label = "Start date of the treaty"


class treaty_end_date(Variable):
    value_type = date
    entity = Treaty
    definition_period = YEARS
    label = "End date of the treaty"

2. To implement the treaty's termination conditions, we might need to consult additional legal texts or legislation. If the treaty can be terminated after six months, we could introduce a variable representing the earliest possible end date.

class earliest_termination_date(Variable):
    value_type = date
    entity = Treaty
    definition_period = YEARS
    depends_on = ["termination_notice_date"]
    label = "Earliest possible termination date"

    def formula(self, period, parameters, treaty):
        termination_notice_date = treaty("termination_notice_date", period)
        if termination_notice_date is not None:
            return termination_notice_date + duration(days=180)
        else:
            return self.start_date

3. The termination notice date is a key concept for calculating the earliest possible termination date. This requires knowledge about when and how formal notice must be given.

class termination_notice_date(Variable):
    value_type = date
    entity = Treaty
    definition_period = YEARS
    label = "Date of termination notice"

    def formula(self, period, parameters, treaty):
        # This is speculative based on normal practices for international agreements
        if self.todays_date() - self.start_date <= duration(days=183):
            return self.start_date + duration(days=-183)
        else:
            return None

4. This is a speculative implementation as there is no specific legal background given. In reality, consultation of relevant law texts would be required for precise implementation.
