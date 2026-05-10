"""SR 0.142.117.121 Art. 20

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Create a custom event
class amendment_effective_date(Event):
    value_type = date
    starts_on = "2024-01-01"
    description = "Date when amendments to the agreement come into effect"

# No entity-specific variable is implied by Art. 20
# However, the date might be useful in some context in government entity
# To illustrate the possibility:
class amendment_effective_date_in_government(Person):
    value_type = date
    entity = Government
    definition_period = YEAR
    label = "Date when amendments to the agreement come into effect in this Government"

    def formula(government, period, parameters):
        return government("amendment_effective_date", period)
