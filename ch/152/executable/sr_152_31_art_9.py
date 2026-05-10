"""SR 152.31 Art. 9

Generated from: ch/152/de/152.31.md

Special needs of the media: authorities take account of time urgency
of media reporting when processing access requests from media professionals.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_medienschaffende_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die gesuchstellende Person Medienschaffende ist"
    reference = "SR 152.31 Art. 9"


class zeitliche_dringlichkeit_berichterstattung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob zeitliche Dringlichkeit der Berichterstattung vorliegt"
    reference = "SR 152.31 Art. 9"


class beruecksichtigung_medienbeduerfnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Behoerde Ruecksicht auf besondere Beduerfnisse der Medien nimmt"
    reference = "SR 152.31 Art. 9"

    def formula(person, period, parameters):
        return person('ist_medienschaffende_person', period)
