"""SR 0.102 Art. 16

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries import countries

class territories_convention_applicable(Variable):
    value_type = bool
    entity = Country
    definition_period = None
    label = "Territories to which the Convention is applied"

    def formula(country, period, parameters):
        return country("territory_choice", period)

class territory_choice(Variable):
    value_type = list
    entity = Country
    definition_period = None

    def formula(country, period, parameters):
        return [
            "CH-VD",  # Vaud, which is a canton in Switzerland
            "CH-NE",  # Neuchâtel, which is a canton in Switzerland
            "FR-BFC",  # BFC, which is a region in France
            # Add other territories here...
        ]
