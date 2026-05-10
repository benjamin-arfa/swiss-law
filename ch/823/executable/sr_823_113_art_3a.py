"""SR 823.113 Art. 3a

Generated from: ch/823/de/823.113.md

Überwälzbarkeit der Mehrwertsteuer:
- Die MWST auf der Provision kann auf den Stellensuchenden überwälzt werden
- Auch wenn dadurch die Provisionshöchstgrenze überschritten wird
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermittlungsprovision_vor_mwst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermittlungsprovision vor Mehrwertsteuer"
    reference = "SR 823.113 Art. 3a"


class mwst_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwendbarer Mehrwertsteuersatz"
    reference = "SR 823.113 Art. 3a"


class vermittlungsprovision_inkl_mwst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermittlungsprovision inkl. überwälzter Mehrwertsteuer"
    reference = "SR 823.113 Art. 3a"

    def formula(person, period, parameters):
        provision = person('vermittlungsprovision_vor_mwst', period)
        mwst = person('mwst_satz', period)
        # MWST darf überwälzt werden, auch über Provisionshöchstgrenze
        return provision * (1 + mwst)
