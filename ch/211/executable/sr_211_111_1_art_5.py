"""SR 211.111.1 Art. 5

Generated from: ch/211/de/211.111.1.md

Sterilisation Urteilsfaehiger: Zulaessig wenn umfassend informiert und
freie schriftliche Zustimmung vorliegt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_urteilsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person urteilsfaehig ist"
    reference = "SR 211.111.1 Art. 5 Abs. 1"


class ist_umfassend_informiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ueber den Eingriff umfassend informiert worden ist"
    reference = "SR 211.111.1 Art. 5 Abs. 1"


class hat_frei_schriftlich_zugestimmt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person dem Eingriff frei und schriftlich zugestimmt hat"
    reference = "SR 211.111.1 Art. 5 Abs. 1"


class sterilisation_urteilsfaehiger_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sterilisation einer urteilsfaehigen Person ueber 18 Jahren zulaessig ist"
    reference = "SR 211.111.1 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        ueber_18 = person('alter', period) >= 18
        urteilsfaehig = person('ist_urteilsfaehig', period)
        informiert = person('ist_umfassend_informiert', period)
        zugestimmt = person('hat_frei_schriftlich_zugestimmt', period)
        return ueber_18 * urteilsfaehig * informiert * zugestimmt
