"""SR 831.201 Art. 30

Generated from: ch/831/de/831.201.md

Ausrichtung der Uebergangsleistung (Transitional benefit):
- Abs. 1: A transitional benefit is paid when:
  a. conditions of Art. 32 IVG are met, AND
  b. medical certificate confirms:
     1. work incapacity of at least 50%, and
     2. prognosis that incapacity continues
- Abs. 2: Entitlement expires at end of month when IV office revokes it
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_voraussetzungen_art32_ivg_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Voraussetzungen nach Art. 32 IVG fuer Uebergangsleistung erfuellt"
    reference = "SR 831.201 Art. 30 Abs. 1 Bst. a"


class iv_aerztlich_bestaetigte_arbeitsunfaehigkeit_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Aerztlich bestaetigte Arbeitsunfaehigkeit in Prozent"
    reference = "SR 831.201 Art. 30 Abs. 1 Bst. b Ziff. 1"


class iv_prognose_arbeitsunfaehigkeit_andauernd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Medizinische Prognose besagt, dass Arbeitsunfaehigkeit weiter andauert"
    reference = "SR 831.201 Art. 30 Abs. 1 Bst. b Ziff. 2"


class iv_anspruch_uebergangsleistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Uebergangsleistung nach Art. 30 IVV"
    reference = "SR 831.201 Art. 30"

    def formula(person, period, parameters):
        voraussetzungen = person('iv_voraussetzungen_art32_ivg_erfuellt', period)
        au_prozent = person('iv_aerztlich_bestaetigte_arbeitsunfaehigkeit_prozent', period)
        prognose = person('iv_prognose_arbeitsunfaehigkeit_andauernd', period)

        # At least 50% work incapacity confirmed by medical certificate
        au_mindestens_50 = au_prozent >= 50

        return voraussetzungen * au_mindestens_50 * prognose
