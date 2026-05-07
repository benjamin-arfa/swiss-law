"""SR 0.104 Art. 21

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class withdrawal_from_treaty(Variable):
    value_type = bool
    entity = Country
    definition_period = PERIOD('year')
    label = "Withdrawal from the multilateral social insurance treaty (Art. 21 SR 0.104)"

    def formula(countries, period, parameters):
        states = parameters(period).withdrawal_status

        for state in states.dataframes(country):
            start_date = states.loc[state].withdrawal_start_date
            end_date = states.loc[state].withdrawal_end_date

            if (start_date is not None and period.start.date() >= start_date.date() or
                (end_date is None or period.end.date() <= end_date.date())) :
                return True

        return False
