"""SR 121.3 Art. 2

Generated from: ch/121/de/121.3.md

Zuordnung und Sitz: AB-ND is administratively assigned to the General Secretariat
of the Federal Department of Defence, Civil Protection and Sport (GS-VBS) and
has its seat in Bern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ab_nd_administrativ_gs_vbs_zugeordnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die AB-ND dem Generalsekretariat VBS administrativ zugeordnet ist"
    reference = "SR 121.3 Art. 2"


class ab_nd_sitz_bern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die AB-ND ihren Sitz in Bern hat"
    reference = "SR 121.3 Art. 2"


class ab_nd_ordnungsgemaess_eingerichtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die AB-ND ordnungsgemaess eingerichtet ist"
    reference = "SR 121.3 Art. 2"

    def formula(person, period, parameters):
        zuordnung = person('ab_nd_administrativ_gs_vbs_zugeordnet', period)
        sitz = person('ab_nd_sitz_bern', period)
        return zuordnung & sitz
