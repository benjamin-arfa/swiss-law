"""SR 0.142.115.192 Art. 11

Generated from: ch/0/de/0.142.115.192.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_li_extending_coverage(Variable):
    value_type = bool
    entity = Resident
    definition_period = YEAR
    label = "Extended coverage AHV insurance to Liechtenstein (SR 0.142.115.192 Art. 11)"

    def formula(resident, period, parameters):
        is_li_resident = resident("is_li_resident", period)
        is_swiss_resident = resident("is_swiss_resident", period)
        return is_li_resident | is_swiss_resident & is_li_resident
