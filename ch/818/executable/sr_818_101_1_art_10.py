"""SR 818.101.1 Art. 10

Generated from: ch/818/de/818.101.1.md

Entgegennahme und Kontrolle der Meldungen: Kantonsaerztinnen nehmen
Meldungen entgegen und pruefen auf Vollstaendigkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_kantonsaerztin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Kantonsaerztin oder Kantonsarzt ist"
    reference = "SR 818.101.1 Art. 10 Abs. 1"


class ist_oberfeldarzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Oberfeldaerztin oder Oberfeldarzt ist (Armee)"
    reference = "SR 818.101.1 Art. 10 Abs. 1"


class meldung_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die eingegangene Meldung vollstaendig ist"
    reference = "SR 818.101.1 Art. 10 Abs. 1"


class hat_klinischen_befund_nach_laborbefund_erhalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein klinischer Befund nach Eingang eines Laborbefunds eingegangen ist"
    reference = "SR 818.101.1 Art. 10 Abs. 2"


class muss_klinischen_befund_einfordern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Kantonsaerztin den klinischen Befund einfordern muss"
    reference = "SR 818.101.1 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        ist_ka = person('ist_kantonsaerztin', period)
        ist_oa = person('ist_oberfeldarzt', period)
        kein_klinischer = 1 - person('hat_klinischen_befund_nach_laborbefund_erhalten', period)
        return (ist_ka + ist_oa > 0) * kein_klinischer
