"""SR 0.142.116.659 Art. 14

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class return_details(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Details of return process (Art. 14 SR 0.142.116.659)"

    def formula(person, period, parameters):
        return_date = parameters(period).return_details.return_date
        return_place = parameters(period).return_details.return_place
        escort_officers = parameters(period).return_details.escort_officers
        return f"Return on the date {return_date} at the place {return_place} with {escort_officers} officers."
