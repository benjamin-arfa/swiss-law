"""SR 510.518 Art. 4 - Verbot des Photographierens, Filmens etc.

Generated from: ch/510/de/510.518.md

Jedes Photographieren, Filmen, Zeichnen, Vermessen oder sonstiges Aufnehmen
der militaerischen Anlagen sowie jedes unbefugte Betreten ist verboten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_bewilligung_aufnahme_mil_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine ausdrueckliche Bewilligung zur Aufnahme von militaerischen Anlagen vorliegt"
    reference = "SR 510.518 Art. 4 Abs. 2"


class aufnahme_mil_anlage_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Photographieren, Filmen, Zeichnen, Vermessen oder sonstiges Aufnehmen der militaerischen Anlage verboten ist"
    reference = "SR 510.518 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return not_(person('hat_bewilligung_aufnahme_mil_anlage', period))


class unbefugtes_betreten_mil_anlage_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das unbefugte Betreten der militaerischen Anlage verboten ist"
    reference = "SR 510.518 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return True
