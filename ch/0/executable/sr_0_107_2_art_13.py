"""SR 0.107.2 Art. 13

Generated from: ch/0/de/0.107.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_country_status(Variable):
    value_type = bool
    label = "Status regarding AHV/IV/EO for the country of residence (not possible to automatically implement)"

    def formula(person, period, parameters):
        return False  # Not possible to automatically implement
