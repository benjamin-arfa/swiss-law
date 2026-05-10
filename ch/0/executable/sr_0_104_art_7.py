"""SR 0.104 Art. 7

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Import necessary modules from OpenFisca


# Define an entity for the variable



# Define a new variable
class international_cooperation(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "International cooperation for combating racial discrimination"

    def formula(countries, period, parameters):
        return countries("signed_art_7", period)

# Another variable
class human_rights_promotion(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Promotion of human rights and social inclusion"

    def formula(countries, period, parameters):
        return countries("signed_human_rights_declaration", period)
