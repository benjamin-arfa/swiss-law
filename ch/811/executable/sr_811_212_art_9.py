"""SR 811.212 Art. 9

Generated from: ch/811/de/811.212.md

Periodische Überprüfung der berufsspezifischen Kompetenzen:
- BAG überprüft periodisch Anpassungsbedarf
- Einbezug von SBFI, Hochschulen und Organisationen der Arbeitswelt
- Überprüfung mindestens alle 10 Jahre ab Inkrafttreten
- Frühere Überprüfung bei Bedarf möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class jahre_seit_letzter_ueberpruefung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit der letzten Überprüfung der berufsspezifischen Kompetenzen"
    reference = "SR 811.212 Art. 9 Abs. 3"


class entwicklung_erfordert_fruehere_ueberpruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Entwicklungen der Gesundheitsversorgung eine frühere Überprüfung erfordern"
    reference = "SR 811.212 Art. 9 Abs. 3"


class ueberpruefung_kompetenzen_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Überprüfung der berufsspezifischen Kompetenzen erforderlich ist"
    reference = "SR 811.212 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_letzter_ueberpruefung', period)
        frueher = person('entwicklung_erfordert_fruehere_ueberpruefung', period)
        max_intervall = parameters(period).sr_811_212.max_ueberpruefungsintervall_jahre

        return (jahre >= max_intervall) + frueher
