"""SR 743.01 Art. 24b

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Feststellung der Dienstunfaehigkeit.
Atemalkoholprobe moeglich. Weitere Voruntersuchungen bei nicht-alkoholbedingten
Anzeichen. Blutprobe bei Anzeichen oder Verweigerung der Atemalkoholprobe.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_person_anzeichen_dienstunfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Anzeichen von Dienstunfaehigkeit vorliegen"
    reference = "SR 743.01 Art. 24b Abs. 3 Bst. a"


class seilbahn_person_atemalkoholprobe_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person die Atemalkoholprobe verweigert oder vereitelt hat"
    reference = "SR 743.01 Art. 24b Abs. 3 Bst. b"


class seilbahn_person_blutprobe_anzuordnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Blutprobe anzuordnen ist"
    reference = "SR 743.01 Art. 24b Abs. 3"

    def formula(person, period, parameters):
        anzeichen = person('seilbahn_person_anzeichen_dienstunfaehigkeit', period)
        verweigert = person('seilbahn_person_atemalkoholprobe_verweigert', period)
        return (anzeichen + verweigert) > 0
