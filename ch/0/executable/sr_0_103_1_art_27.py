"""SR 0.103.1 Art. 27

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_entry_date(Variable):
    value_type = date
    label = "Date when the treaty entered into effect"

    def formula(e, period, parameters):
        # This function returns the date when the treaty entered into effect, 
        # which depends on the number of countries that have ratified or joined the treaty.
        # However, due to the complexity of this problem and the absence of actual calendar events in OpenFisca,
        # this example is simplified and only considers the case when the 35th country has ratified or joined the treaty.
        num_countries = 30  # current number of countries that have ratified or joined the treaty
        days_to_pass = num_countries * 3 * 30  # three months in days
        treaty_entry_date = e.date + pd.offsets.Day(days_to_pass)
        return treaty_entry_date
