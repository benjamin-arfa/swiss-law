"""SR 211.111.1 Art. 4

Generated from: ch/211/de/211.111.1.md

Sterilisation voruebergehend Urteilsunfaehiger: Verboten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_voruebergehend_urteilsunfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person voruebergehend urteilsunfaehig ist"
    reference = "SR 211.111.1 Art. 4"


class sterilisation_voruebergehend_urteilsunfaehiger_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sterilisation verboten ist weil die Person voruebergehend urteilsunfaehig ist"
    reference = "SR 211.111.1 Art. 4"

    def formula(person, period, parameters):
        ueber_18 = person('alter', period) >= 18
        voruebergehend = person('ist_voruebergehend_urteilsunfaehig', period)
        return ueber_18 * voruebergehend
