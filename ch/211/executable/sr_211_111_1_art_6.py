"""SR 211.111.1 Art. 6

Generated from: ch/211/de/211.111.1.md

Sterilisation von Personen unter umfassender Beistandschaft: Zusaetzlich
zur Zustimmung der Person braucht es die Zustimmung des gesetzlichen
Vertreters und der Erwachsenenschutzbehoerde.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class steht_unter_umfassender_beistandschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person unter umfassender Beistandschaft steht"
    reference = "SR 211.111.1 Art. 6 Abs. 1"


class zustimmung_gesetzlicher_vertreter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung des gesetzlichen Vertreters vorliegt"
    reference = "SR 211.111.1 Art. 6 Abs. 1"


class zustimmung_erwachsenenschutzbehoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung der Erwachsenenschutzbehoerde vorliegt"
    reference = "SR 211.111.1 Art. 6 Abs. 2 lit. b"


class sterilisation_unter_beistandschaft_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sterilisation einer Person unter umfassender Beistandschaft zulaessig ist"
    reference = "SR 211.111.1 Art. 6"

    def formula(person, period, parameters):
        ueber_18 = person('alter', period) >= 18
        urteilsfaehig = person('ist_urteilsfaehig', period)
        beistandschaft = person('steht_unter_umfassender_beistandschaft', period)
        informiert = person('ist_umfassend_informiert', period)
        zugestimmt = person('hat_frei_schriftlich_zugestimmt', period)
        vertreter = person('zustimmung_gesetzlicher_vertreter', period)
        behoerde = person('zustimmung_erwachsenenschutzbehoerde', period)
        return ueber_18 * urteilsfaehig * beistandschaft * informiert * zugestimmt * vertreter * behoerde
