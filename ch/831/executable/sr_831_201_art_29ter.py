"""SR 831.201 Art. 29ter

Generated from: ch/831/de/831.201.md

Unterbruch der Arbeitsunfaehigkeit:
Ein wesentlicher Unterbruch der Arbeitsunfaehigkeit im Sinne von
Art. 28 Abs. 1 Bst. b IVG liegt vor, wenn die versicherte Person
an mindestens 30 aufeinanderfolgenden Tagen voll arbeitsfaehig war.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_aufeinanderfolgende_tage_voll_arbeitsfaehig(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl aufeinanderfolgender Tage mit voller Arbeitsfaehigkeit"
    reference = "SR 831.201 Art. 29ter"


class iv_wesentlicher_unterbruch_arbeitsunfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein wesentlicher Unterbruch der Arbeitsunfaehigkeit vorliegt (>= 30 Tage voll arbeitsfaehig)"
    reference = "SR 831.201 Art. 29ter"

    def formula(person, period, parameters):
        tage = person('iv_aufeinanderfolgende_tage_voll_arbeitsfaehig', period)
        return tage >= 30
