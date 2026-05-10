"""SR 831.30 Art. 8

Generated from: ch/831/de/831.30.md

Art. 8: Verweigerung der Ergaenzungsleistung - EL is permanently or
temporarily denied if a pension is denied pursuant to Art. 21 Abs. 1 or 2
ATSG (due to the insured person's own fault/negligence).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_rente_verweigert_atsg_21(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rente verweigert gemaess Art. 21 Abs. 1 oder 2 ATSG"
    reference = "SR 831.30 Art. 8"


class el_verweigerung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Verweigerung der Ergaenzungsleistung (Art. 8 ELG)"
    reference = "SR 831.30 Art. 8"

    def formula(person, period, parameters):
        return person('el_rente_verweigert_atsg_21', period)
