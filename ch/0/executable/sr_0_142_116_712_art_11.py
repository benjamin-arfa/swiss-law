"""SR 0.142.116.712 Art. 11

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_termination_date(Variable):
    value_type = date
    default_population = 'countries'
    definition_period = YEAR
    label = "Date of termination of agreement between Switzerland and St. Vincent and the Grenadines (Art. 11 SR 0.142.116.712)"

    def formula(countries, period, parameters):
        agreement_start_date = '2013-03-14'
        agreement_termination_condition = parameters(period).economy.agreements.termination_condition
        notification_days = parameters(period).economy.agreements.notification_days
        notification_start_date = '0001-01-01'
        # Compute the date based on notification logic and return None if no termination is known
        # This should be adapted to match the requirements of your OpenFisca model.
