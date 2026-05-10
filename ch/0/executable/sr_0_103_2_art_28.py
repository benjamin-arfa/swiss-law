"""SR 0.103.2 Art. 28

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class human_rights_committee_size(Variable):
    value_type = int
    entity = Country
    definition_period = YEAR
    label = "Size of the Human Rights Committee (Art. 28 SR 0.103.2)"

    def formula(country, period, parameters):
        return 18
