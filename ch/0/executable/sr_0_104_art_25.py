"""SR 0.104 Art. 25

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class international_agreements_signed(Variable):
    value_type = int
    entity = Mesh
    definition_period = YEAR
    label = "Number of international agreements signed by government (SR 0.104 Art. 25)"

    def formula(municipality, period, parameters):
        return 0  # placeholder value
