"""SR 510.35 Art. 5 - Quarantaene

Generated from: ch/510/de/510.35.md

Mit Quarantaene koennen Schulen und Kurse oder Teile davon belegt werden,
wenn die Gefahr der Ausbreitung einer Infektionskrankheit besteht.
Die Truppe wird abgesondert und darf weder beurlaubt noch entlassen werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gefahr_ausbreitung_infektionskrankheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gefahr der Ausbreitung einer Infektionskrankheit besteht"
    reference = "SR 510.35 Art. 5 Abs. 1"


class truppe_mit_quarantaene_belegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Truppe (Schulen/Kurse) mit Quarantaene belegt ist"
    reference = "SR 510.35 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('gefahr_ausbreitung_infektionskrankheit', period) * person('quarantaene_angeordnet', period)


class truppe_darf_nicht_beurlaubt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die mit Quarantaene belegte Truppe nicht beurlaubt oder entlassen werden darf"
    reference = "SR 510.35 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        return person('truppe_mit_quarantaene_belegt', period)
