"""SR 831.135.1 Art. 3

Generated from: ch/831/de/831.135.1.md

Art. 3: Beginn und Ende des Anspruchs - Start and end of entitlement.

The entitlement arises at the earliest on the first day of the month
for which a full old-age pension is drawn, at the latest upon reaching
the reference age under Art. 21 Abs. 1 AHVG. It ceases when the
eligibility conditions are no longer met.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hva_bezieht_ganze_altersrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person bezieht eine ganze Altersrente"
    reference = "SR 831.135.1 Art. 3"


class hva_referenzalter_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Referenzalter nach Art. 21 Abs. 1 AHVG erreicht"
    reference = "SR 831.135.1 Art. 3"


class hva_anspruch_begonnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Hilfsmittel hat begonnen (Art. 3 HVA)"
    reference = "SR 831.135.1 Art. 3"

    def formula(person, period, parameters):
        ganze_rente = person('hva_bezieht_ganze_altersrente', period)
        referenzalter = person('hva_referenzalter_erreicht', period)
        # Entitlement starts at the earlier of: first full pension month or reference age
        return ganze_rente + referenzalter > 0
