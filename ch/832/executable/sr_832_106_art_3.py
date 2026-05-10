"""SR 832.106 Art. 3

Generated from: ch/832/de/832.106.md

After a municipality fusion, the premium region of each former
municipality remains unchanged on its territory until the new
municipality is assigned a region in the appendix.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gemeinde_fusioniert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gemeinde aus einer Fusion hervorgegangen ist"
    reference = "SR 832.106 Art. 3"


class neue_gemeinde_im_anhang_eingeteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die fusionierte Gemeinde im Anhang in eine Praemienregion eingeteilt wurde"
    reference = "SR 832.106 Art. 3"


class praemienregion_nach_fusion_unveraendert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Praemienregion der frueheren Gemeinde nach Fusion unveraendert bleibt"
    reference = "SR 832.106 Art. 3"

    def formula(person, period, parameters):
        fusioniert = person('gemeinde_fusioniert', period)
        eingeteilt = person('neue_gemeinde_im_anhang_eingeteilt', period)
        # Region stays unchanged if municipality was fused but not yet reassigned
        return fusioniert * not_(eingeteilt)
