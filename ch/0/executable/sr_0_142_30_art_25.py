"""SR 0.142.30 Art. 25

Generated from: ch/0/de/0.142.30.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class refugee_administrative_assistance(Variable):
    value_type = bool
    entity = Refugee
    definition_period = MONTH
    label = "Administrative assistance to refugees (Art. 25 SR 0.142.30)"

    def formula(refugee, period, parameters):
        refugee_status = refugee("refugee_status", period)
        lack_access_foreign_authorities = refugee("lacks_access_foreign_authorities", period)
        admin_assistance_from_ch = refugee("admin_assistance_from_ch", period)

        return refugee_status & lack_access_foreign_authorities & admin_assistance_from_ch
