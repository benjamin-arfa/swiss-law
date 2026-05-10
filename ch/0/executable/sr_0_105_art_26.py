"""SR 0.105 Art. 26

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# The following code is a simplified representation of how this might be done


class is_country_treaty_member(Variable):
    value_type = bool
    definition_period = DAY
    label = "Participation of a country in the Treaty (SR 0.105 Art. 26)"

    def formula(e, period, parameters):
        return e('participates_in_treaty', period)
