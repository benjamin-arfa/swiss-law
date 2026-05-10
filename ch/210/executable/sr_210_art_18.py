"""SR 210 Art. 18

Generated from: ch/de/210.md

Fehlen der Urteilsfaehigkeit: Wer nicht urteilsfaehig ist, vermag unter
Vorbehalt der gesetzlichen Ausnahmen durch seine Handlungen keine rechtliche
Wirkung herbeizufuehren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kann_rechtliche_wirkung_herbeifuehren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person durch ihre Handlungen rechtliche Wirkung herbeifuehren kann (Art. 18 ZGB)"
    reference = "SR 210 Art. 18"

    def formula(person, period, parameters):
        # Wer nicht urteilsfaehig ist, kann grundsaetzlich keine
        # rechtliche Wirkung herbeifuehren (Vorbehalt gesetzlicher Ausnahmen)
        ist_urteilsfaehig = person('ist_urteilsfaehig', period)
        hat_gesetzliche_ausnahme = person('hat_gesetzliche_ausnahme_art18', period)
        return ist_urteilsfaehig + hat_gesetzliche_ausnahme > 0


class hat_gesetzliche_ausnahme_art18(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine gesetzliche Ausnahme nach Art. 18 ZGB vorliegt"
    reference = "SR 210 Art. 18"
