"""SR 0.104 Art. 4

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# This is not a traditional OpenFisca variable, as it describes a social or legal concept rather than a financial variable.
# However, we can define a "dummy" variable to represent the presence or absence of such a policy:


class promotes_racial_discrimination(Variable):
    value_type = bool
    entity = Household  # Assuming this applies to a household or government entity
    definition_period = YEAR
    label = "Promotes racial discrimination, contrary to Art. 4 of SR 0.104"

    def formula(household, period, parameters):
        return False
