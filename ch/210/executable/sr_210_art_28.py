"""SR 210 Art. 28

Generated from: ch/de/210.md

Schutz der Persoenlichkeit - Gegen Verletzungen: Wer in seiner
Persoenlichkeit widerrechtlich verletzt wird, kann zu seinem Schutz gegen
jeden, der an der Verletzung mitwirkt, das Gericht anrufen. Eine Verletzung
ist widerrechtlich, wenn sie nicht durch Einwilligung des Verletzten, durch
ein ueberwiegendes privates oder oeffentliches Interesse oder durch Gesetz
gerechtfertigt ist.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_persoenlichkeit_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Persoenlichkeitsverletzung vorliegt"
    reference = "SR 210 Art. 28 Abs. 1"


class hat_einwilligung_verletzter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Einwilligung des Verletzten vorliegt"
    reference = "SR 210 Art. 28 Abs. 2"


class liegt_ueberwiegendes_interesse_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein ueberwiegendes privates oder oeffentliches Interesse vorliegt"
    reference = "SR 210 Art. 28 Abs. 2"


class ist_durch_gesetz_gerechtfertigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Verletzung durch Gesetz gerechtfertigt ist"
    reference = "SR 210 Art. 28 Abs. 2"


class ist_persoenlichkeitsverletzung_widerrechtlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Persoenlichkeitsverletzung widerrechtlich ist (Art. 28 ZGB)"
    reference = "SR 210 Art. 28"

    def formula(person, period, parameters):
        ist_verletzt = person('ist_persoenlichkeit_verletzt', period)
        # Abs. 2: Widerrechtlich, wenn nicht gerechtfertigt durch:
        einwilligung = person('hat_einwilligung_verletzter', period)
        ueberwiegendes_interesse = person('liegt_ueberwiegendes_interesse_vor', period)
        gesetz = person('ist_durch_gesetz_gerechtfertigt', period)

        ist_gerechtfertigt = (einwilligung + ueberwiegendes_interesse + gesetz) > 0
        return ist_verletzt * not_(ist_gerechtfertigt)


class kann_gericht_anrufen_art28(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person das Gericht zum Schutz der Persoenlichkeit anrufen kann"
    reference = "SR 210 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        # Abs. 1: Wer widerrechtlich verletzt wird, kann Gericht anrufen
        return person('ist_persoenlichkeitsverletzung_widerrechtlich', period)
