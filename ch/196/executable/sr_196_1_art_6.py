"""SR 196.1 Art. 6

Generated from: ch/196/de/196.1.md

Dauer der Sperrung: Maximale Sperrungsdauer und Verlaengerungsregeln.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sperrungsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aktuelle Dauer der Sperrung in Jahren"
    reference = "SR 196.1 Art. 6"


class herkunftsstaat_hat_willen_zur_rechtshilfe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Herkunftsstaat seinen Willen zur Rechtshilfezusammenarbeit ausdrueckt"
    reference = "SR 196.1 Art. 6 Abs. 1"


class sperrung_nach_art_3_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Sperrung nach Art. 3 noch gueltig ist (max 4 Jahre, Verlaengerung je 1 Jahr bis max 10 Jahre)"
    reference = "SR 196.1 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        dauer = person('sperrungsdauer_jahre', period)
        wille = person('herkunftsstaat_hat_willen_zur_rechtshilfe', period)
        # Grundbefristung: max 4 Jahre
        innerhalb_grundfrist = dauer <= 4
        # Verlaengerung moeglich wenn Wille vorhanden, max 10 Jahre
        verlaengert_gueltig = wille * (dauer <= 10)
        return innerhalb_grundfrist + verlaengert_gueltig > 0


class einziehungsverfahren_eingeleitet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Einziehungsverfahren eingeleitet wurde"
    reference = "SR 196.1 Art. 6 Abs. 2"


class jahre_seit_sperrungsverfuegung_art_4(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit Rechtskraft der Sperrungsverfuegung nach Art. 4"
    reference = "SR 196.1 Art. 6 Abs. 2"


class sperrung_nach_art_4_hinfaellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sperrung nach Art. 4 hinfaellig wird (kein Einziehungsverfahren innert 10 Jahren)"
    reference = "SR 196.1 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        nicht_eingeleitet = 1 - person('einziehungsverfahren_eingeleitet', period)
        ueber_10_jahre = person('jahre_seit_sperrungsverfuegung_art_4', period) >= 10
        return nicht_eingeleitet * ueber_10_jahre
