"""SR 210 Art. 29

Generated from: ch/de/210.md

Recht auf den Namen - Namensschutz: Wird jemandem die Fuehrung seines
Namens bestritten, so kann er auf Feststellung seines Rechtes klagen.
Wird jemand durch Namensanmassung beeintraechtigt, kann er auf Unterlassung
sowie bei Verschulden auf Schadenersatz und Genugtuung klagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wird_namensfuehrung_bestritten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Person die Fuehrung ihres Namens bestritten wird"
    reference = "SR 210 Art. 29 Abs. 1"


class liegt_namensanmassung_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Namensanmassung durch eine andere Person vorliegt"
    reference = "SR 210 Art. 29 Abs. 2"


class hat_verschulden_namensanmassung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Verschulden bei der Namensanmassung vorliegt"
    reference = "SR 210 Art. 29 Abs. 2"


class kann_feststellungsklage_name(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person auf Feststellung des Namensrechts klagen kann"
    reference = "SR 210 Art. 29 Abs. 1"

    def formula(person, period, parameters):
        # Abs. 1: Wer in der Namensfuehrung bestritten wird, kann klagen
        return person('wird_namensfuehrung_bestritten', period)


class kann_unterlassungsklage_name(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person auf Unterlassung der Namensanmassung klagen kann"
    reference = "SR 210 Art. 29 Abs. 2"

    def formula(person, period, parameters):
        # Abs. 2: Wer durch Namensanmassung beeintraechtigt wird
        return person('liegt_namensanmassung_vor', period)


class kann_schadenersatzklage_name(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person bei Namensanmassung auf Schadenersatz klagen kann"
    reference = "SR 210 Art. 29 Abs. 2"

    def formula(person, period, parameters):
        # Abs. 2: Bei Verschulden auch Schadenersatz und Genugtuung
        anmassung = person('liegt_namensanmassung_vor', period)
        verschulden = person('hat_verschulden_namensanmassung', period)
        return anmassung * verschulden
