"""SR 831.411 Art. 7

Generated from: ch/831/de/831.411.md

Art. 7: Rueckzahlung - Repayment of early withdrawal.

Abs. 1: Minimum repayment amount is CHF 10,000.

Abs. 2: If the outstanding early withdrawal is less than the minimum
amount, repayment must be made in a single payment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wefv_ausstehender_vorbezug(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Ausstehender Vorbezugsbetrag"
    reference = "SR 831.411 Art. 7"


class wefv_rueckzahlung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Geplanter Rueckzahlungsbetrag"
    reference = "SR 831.411 Art. 7 Abs. 1"


class wefv_rueckzahlung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rueckzahlung ist zulaessig (Art. 7 WEFV)"
    reference = "SR 831.411 Art. 7"

    def formula(person, period, parameters):
        ausstehend = person('wefv_ausstehender_vorbezug', period)
        betrag = person('wefv_rueckzahlung_betrag', period)
        mindestbetrag = 10000

        # If outstanding < minimum: must repay full amount
        muss_voll_zurueckzahlen = ausstehend < mindestbetrag
        voller_betrag = muss_voll_zurueckzahlen * (betrag >= ausstehend)
        teilbetrag = not_(muss_voll_zurueckzahlen) * (betrag >= mindestbetrag)

        return voller_betrag + teilbetrag > 0
