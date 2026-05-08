"""SR 935.01 Art. 3

Generated from: ch/935/de/935.01.md

Verfahren und Nachprüfung der Berufsqualifikationen bei reglementierten
Berufen mit Auswirkung auf die öffentliche Gesundheit oder Sicherheit:
- SBFI leitet Meldung an zuständige Stelle weiter
- Bundesbehörde prüft Qualifikationen
- Bei wesentlicher Abweichung: Eignungsprüfung möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class beruf_betrifft_gesundheit_sicherheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der reglementierte Beruf die öffentliche Gesundheit oder Sicherheit betrifft"
    reference = "SR 935.01 Art. 3 Abs. 1"


class qualifikation_weicht_wesentlich_ab(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Berufsqualifikation wesentlich von Schweizer Anforderungen abweicht"
    reference = "SR 935.01 Art. 3 Abs. 2"


class eignungspruefung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Eignungsprüfung zum Nachweis fehlender Kenntnisse erforderlich ist"
    reference = "SR 935.01 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        gesundheit = person('beruf_betrifft_gesundheit_sicherheit', period)
        abweichung = person('qualifikation_weicht_wesentlich_ab', period)
        return gesundheit * abweichung
