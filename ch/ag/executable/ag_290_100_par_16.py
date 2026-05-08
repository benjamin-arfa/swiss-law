"""AG 290.100 § 16

Generated from: ch/ag/de/290.100.md

§ 16 Pruefung: The exam covers main areas of applicable federal and cantonal
law, is practice-oriented. Passing grants the certificate. After 3 failures,
no further exam is permitted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_anwaltspruefung_versuche(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Anwaltspruefungsversuche (AG 290.100 § 16)"
    reference = "AG 290.100 § 16 Abs. 3"


class ag_anwaltspruefung_bestanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwaltspruefung bestanden (AG 290.100 § 16 Abs. 2)"
    reference = "AG 290.100 § 16 Abs. 2"


class ag_faehigkeitsausweis_erhalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Faehigkeitsausweis als Rechtsanwalt erhalten (AG 290.100 § 16 Abs. 2)"
    reference = "AG 290.100 § 16 Abs. 2"

    def formula(person, period, parameters):
        return person('ag_anwaltspruefung_bestanden', period)


class ag_weitere_pruefung_zugelassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zu weiterer Anwaltspruefung zugelassen (AG 290.100 § 16 Abs. 3)"
    reference = "AG 290.100 § 16 Abs. 3"

    def formula(person, period, parameters):
        versuche = person('ag_anwaltspruefung_versuche', period)
        bestanden = person('ag_anwaltspruefung_bestanden', period)
        # After 3 failures, no further exam; also not needed if passed
        return (versuche < 3) * (bestanden == 0)
