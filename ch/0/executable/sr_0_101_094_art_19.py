"""SR 0.101.094 Art. 19

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class EntryIntoForceDateVariable(Variable):
    value_type = date
    entity = person
    definition_period = MONTH
    reference = "SR 0.101.094 Art. 19"

    parameters = [
        ("consent_date", date, {}),
        ("entry_into_force_month_offset", integer, {"default": 3}),
        # assuming a variable for consent date for each contracting party
        ("contracting_party_{party_id}.consent_date", date, {}),
    ]

    def formula(person, period, parameters):
        consent_dates = [parameters(period).get(f"contracting_party_{party_id}.consent_date") for party_id in range(1, 11)]  # assuming 10 contracting parties
        all_parties_consented = all([cd for cd in consent_dates])
        if all_parties_consented:
            entry_into_force_month = parameters(period).entry_into_force_month_offset + (period.start_date.year - parameters(period).consent_date.year)
            entry_into_force_month += (period.start_date.month - parameters(period).consent_date.month) // 3 * 3  # round down to the closest multiple of 3
            return periods.period(start=period.start_date.replace(month=1, day=1) + relativedelta(months=entry_into_force_month), end=period.start_date.replace(month=1, day=1) + relativedelta(months=entry_into_force_month))
        else:
            return period.start_date
