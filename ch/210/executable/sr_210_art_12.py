"""SR 210 Art. 12

Generated from: ch/de/210.md

Handlungsfaehigkeit: Wer handlungsfaehig ist, hat die Faehigkeit, durch
seine Handlungen Rechte und Pflichten zu begruenden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_handlungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person handlungsfaehig ist (Art. 12-13 ZGB)"
    reference = "SR 210 Art. 12, Art. 13"

    def formula(person, period, parameters):
        # Art. 13: Handlungsfaehigkeit besitzt, wer volljaehrig und
        # urteilsfaehig ist.
        ist_volljaehrig = person('ist_volljaehrig', period)
        ist_urteilsfaehig = person('ist_urteilsfaehig', period)
        return ist_volljaehrig * ist_urteilsfaehig
