"""SR 210 Art. 17

Generated from: ch/de/210.md

Handlungsunfaehigkeit: Handlungsunfaehig sind urteilsunfaehige Personen,
Minderjaehrige sowie Personen unter umfassender Beistandschaft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_handlungsunfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person handlungsunfaehig ist (Art. 17 ZGB)"
    reference = "SR 210 Art. 17"

    def formula(person, period, parameters):
        ist_urteilsfaehig = person('ist_urteilsfaehig', period)
        ist_volljaehrig = person('ist_volljaehrig', period)
        unter_umfassender_beistandschaft = person('unter_umfassender_beistandschaft', period)

        # Handlungsunfaehig wenn: urteilsunfaehig ODER minderjaehrig
        # ODER unter umfassender Beistandschaft
        return not_(ist_urteilsfaehig) + not_(ist_volljaehrig) + unter_umfassender_beistandschaft > 0


class unter_umfassender_beistandschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person unter umfassender Beistandschaft steht"
    reference = "SR 210 Art. 17"
