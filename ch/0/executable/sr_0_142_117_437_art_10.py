"""SR 0.142.117.437 Art. 10

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entry_into_force(Variable):
    value_type = date
    scope3 = 'month'
    label = "Entry into force of the treaty (SR 0.142.117.437 Art. 10)"

    def formula(periods, parameters):
        return parameters(periods).international_agreements.entry_into_force
