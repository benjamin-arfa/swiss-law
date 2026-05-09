"""SR 831.30 Art. 16a

Generated from: ch/831/de/831.30.md

Art. 16a: Hoehe der Rueckerstattung - Repayment of lawfully received
benefits from the estate after death of the recipient.

Abs. 1: Benefits under Art. 3(1) must be repaid from the estate after
the recipient's death. Repayment is only due on the portion of the
estate exceeding CHF 40,000.
Abs. 2: For couples, repayment obligation arises only from the estate
of the second spouse to die.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_nachlasswert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wert des Nachlasses"
    reference = "SR 831.30 Art. 16a Abs. 1"


class el_bezogene_leistungen_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total rechtmaessig bezogene EL-Leistungen"
    reference = "SR 831.30 Art. 16a Abs. 1"


class el_rueckerstattung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckerstattungspflicht aus dem Nachlass (Art. 16a ELG)"
    reference = "SR 831.30 Art. 16a Abs. 1"

    def formula(person, period, parameters):
        nachlass = person('el_nachlasswert', period)
        bezogen = person('el_bezogene_leistungen_total', period)

        # Only repay from estate portion exceeding CHF 40,000
        rueckerstattungsfaehig = max_(nachlass - 40000, 0)
        return min_(rueckerstattungsfaehig, bezogen)
