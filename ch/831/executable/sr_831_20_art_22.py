"""SR 831.20 Art. 22

Generated from: ch/831/de/831.20.md

Art. 22: Anspruch - Entitlement to daily allowance during integration measures:
- Abs. 1: During integration measures per Art. 8 Abs. 3, insured persons
  are entitled to a daily allowance if (a) prevented from working for at
  least 3 consecutive days, or (b) at least 50% incapacitated.
- Abs. 3: Those in higher education only qualify if health prevents
  concurrent work or significantly prolongs studies.
- Abs. 4: Those in school-only vocational training have no entitlement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_durchfuehrung_eingliederungsmassnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nimmt an Eingliederungsmassnahmen nach Art. 8 Abs. 3 IVG teil"
    reference = "SR 831.20 Art. 22 Abs. 1"


class iv_verhindert_mindestens_3_tage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Wegen Eingliederungsmassnahmen an mindestens 3 aufeinanderfolgenden "
        "Tagen an Arbeit verhindert"
    )
    reference = "SR 831.20 Art. 22 Abs. 1 Bst. a"


class iv_arbeitsunfaehigkeit_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Arbeitsunfaehigkeit in Prozent (0-100)"
    reference = "SR 831.20 Art. 22 Abs. 1 Bst. b"


class iv_in_erstmaliger_beruflicher_ausbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Befindet sich in erstmaliger beruflicher Ausbildung"
    reference = "SR 831.20 Art. 22 Abs. 2"


class iv_in_schulischer_grundbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Besucht allgemeinbildende Schule oder rein schulische berufliche Grundbildung"
    reference = "SR 831.20 Art. 22 Abs. 4"


class iv_anspruch_taggeld(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf IV-Taggeld (Art. 22 IVG)"
    reference = "SR 831.20 Art. 22"

    def formula(person, period, parameters):
        massnahme = person('iv_durchfuehrung_eingliederungsmassnahme', period)
        verhindert_3_tage = person('iv_verhindert_mindestens_3_tage', period)
        arbeitsunfaehigkeit = person('iv_arbeitsunfaehigkeit_prozent', period)
        schulisch = person('iv_in_schulischer_grundbildung', period)

        # Abs. 1: entitled if (a) prevented 3+ consecutive days OR (b) >= 50% incapacitated
        grundanspruch = massnahme * (verhindert_3_tage + (arbeitsunfaehigkeit >= 50))

        # Abs. 4: no entitlement for school-only vocational training
        return grundanspruch * (schulisch == 0)
