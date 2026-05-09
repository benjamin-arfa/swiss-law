"""SR 510.35 Art. 1 - Seuchenpolizeiliche Massnahmen

Generated from: ch/510/de/510.35.md

Das EMD (im Aktivdienst das Armeekommando) kann seuchenpolizeiliche
Massnahmen anordnen, um zu verhindern, dass ansteckende Krankheiten
in die Armee eingeschleppt oder durch die Armee ausgebreitet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ansteckende_krankheit_droht_armee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gefahr besteht, dass ansteckende Krankheiten in die Armee eingeschleppt oder durch die Armee ausgebreitet werden"
    reference = "SR 510.35 Art. 1 Abs. 1"


class verseuchung_chemisch_radioaktiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verseuchung durch chemische oder radioaktive Stoffe vorliegt"
    reference = "SR 510.35 Art. 1 Abs. 1"


class seuchenpolizeiliche_massnahme_angeordnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob seuchenpolizeiliche Massnahmen angeordnet wurden"
    reference = "SR 510.35 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('ansteckende_krankheit_droht_armee', period)
            + person('verseuchung_chemisch_radioaktiv', period)
        ) > 0
