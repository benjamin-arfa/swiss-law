"""SR 251.4 Art. 20

Generated from: ch/251/de/251.4.md

Fristen: Die Monatsfrist beginnt am Tag nach Eingang der vollstaendigen
Meldung und endet am gleichen Kalendertag des Folgemonats.
Art. 22a VwVG findet keine Anwendung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vollstaendige_meldung_eingangsdatum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Eingangs der vollstaendigen Meldung"
    reference = "SR 251.4 Art. 20 Abs. 1"


class pruefungsverfahren_fristbeginn(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Tag nach Eingang der vollstaendigen Meldung (Fristbeginn)"
    reference = "SR 251.4 Art. 20 Abs. 1"


class pruefung_beschluss_zugestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beschluss ueber die Einleitung der Pruefung innerhalb der Monatsfrist zugestellt wurde"
    reference = "SR 251.4 Art. 20 Abs. 2"


class wesentliche_aenderung_mitgeteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob wesentliche Aenderungen der Verhaeltnisse mitgeteilt wurden (Fristneustart moeglich)"
    reference = "SR 251.4 Art. 21"
