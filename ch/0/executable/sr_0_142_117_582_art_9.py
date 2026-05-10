"""SR 0.142.117.582 Art. 9

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Implementing the country entity if not already present (for educational purpose)
class Country(Entity):
    ...
    variable_definitions = [
        ahv_contribution_treaty_entry,
    ]

class ahv_contribution_treaty_entry(Variable):
    value_type = datetime.date
    entity = Country
    label = "AHV contribution treaty entry in force date (SR 0.142.117.582 Art. 9)"

    def formula(country, period, parameters):        
        last_notification_date = datetime.date(1999, 1, 1)  # placeholder value 
        treaty_in_force_date = last_notification_date + datetime.timedelta(days=30)
        
        return treaty_in_force_date
