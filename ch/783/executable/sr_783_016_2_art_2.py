"""SR 783.016.2 Art. 2

Generated from: ch/783/de/783.016.2.md

Mindeststandards: Bruttolohn mindestens 19 CHF/Stunde,
Arbeitszeit hoechstens 44 Stunden/Woche, ab Beginn des
Arbeitsverhaeltnisses und unabhaengig vom Beschaeftigungsgrad.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bruttolohn_pro_stunde(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Bruttolohn pro Stunde in CHF"
    reference = "SR 783.016.2 Art. 2 Abs. 1"


class vereinbarte_wochenarbeitszeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertraglich vereinbarte Arbeitszeit in Stunden pro Woche"
    reference = "SR 783.016.2 Art. 2 Abs. 2"


MINDESTLOHN_PRO_STUNDE = 19.0
MAX_WOCHENARBEITSZEIT = 44.0


class erfuellt_mindestlohn_postdienste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Mindestlohn von 19 CHF/Stunde eingehalten wird"
    reference = "SR 783.016.2 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        lohn = person('bruttolohn_pro_stunde', period)
        return lohn >= MINDESTLOHN_PRO_STUNDE


class erfuellt_max_arbeitszeit_postdienste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die maximale Wochenarbeitszeit von 44 Stunden eingehalten wird"
    reference = "SR 783.016.2 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        arbeitszeit = person('vereinbarte_wochenarbeitszeit', period)
        return arbeitszeit <= MAX_WOCHENARBEITSZEIT


class erfuellt_mindeststandards_postdienste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob alle Mindeststandards fuer Arbeitsbedingungen im Postdienst erfuellt sind"
    reference = "SR 783.016.2 Art. 2"

    def formula(person, period, parameters):
        lohn_ok = person('erfuellt_mindestlohn_postdienste', period)
        zeit_ok = person('erfuellt_max_arbeitszeit_postdienste', period)
        return lohn_ok * zeit_ok
