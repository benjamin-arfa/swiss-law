"""SR 0.142.116.712 Art. 7

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class notification_entry_into_force(Variable):
    value_type = date
    entity = None # could be contract or legal_entity, but seems like it's not defined
    definition_period = NONE # doesn't seem to depend on time
    label = "Entry into force date for notification of change (Art. 7 SR 0.142.116.712)"
    # the only purpose of this variable is to provide a formula for when a notification is recognized.

    def formula(e):

        contracts = e.contract  # this depends on how contracts are structured in your database/file

        def get_second_notification_date(contract_id):
            # Assuming a notification is represented by a notification_date
            contract_notification_dates = e.contract_notification_dates[...]
            contract_notification_dates = contract_notification_dates[contract_id]
            dates = [x.date for x in contract_notification_dates if x.both_parties_confirmed]
            # It seems we would generally expect 2 (or less) dates
            if len(dates) < 2:
                raise Exception("We are missing a confirmation from the second party in a notification")

            # We are only concerned with the second date
            return dates[1]

        return get_second_notification_date(e.contract_id)
