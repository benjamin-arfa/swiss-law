"""SR 210 Art. 35-36

Generated from: ch/de/210.md

Verschollenerklärung: Eine Person kann fuer verschollen erklaert werden,
wenn sie in hoher Todesgefahr verschwunden oder seit langem nachrichtlos
abwesend ist. Antrag nach 1 Jahr seit Todesgefahr oder 5 Jahren seit
letzter Nachricht. Aufgebotsfrist mindestens 1 Jahr.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_in_todesgefahr_verschwunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person in hoher Todesgefahr verschwunden ist"
    reference = "SR 210 Art. 35 Abs. 1"


class ist_nachrichtlos_abwesend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person seit langem nachrichtlos abwesend ist"
    reference = "SR 210 Art. 35 Abs. 1"


class dauer_seit_todesgefahr_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer in Monaten seit dem Zeitpunkt der Todesgefahr"
    reference = "SR 210 Art. 36 Abs. 1"


class dauer_seit_letzter_nachricht_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer in Monaten seit der letzten Nachricht"
    reference = "SR 210 Art. 36 Abs. 1"


class kann_verschollenerklarung_beantragt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Antrag auf Verschollenerklärung gestellt werden kann"
    reference = "SR 210 Art. 35, Art. 36"

    def formula(person, period, parameters):
        in_todesgefahr = person('ist_in_todesgefahr_verschwunden', period)
        nachrichtlos = person('ist_nachrichtlos_abwesend', period)
        dauer_todesgefahr = person('dauer_seit_todesgefahr_monate', period)
        dauer_nachricht = person('dauer_seit_letzter_nachricht_monate', period)

        # Art. 36 Abs. 1: Antrag nach Ablauf von mindestens 1 Jahr
        # seit Todesgefahr oder 5 Jahren seit letzter Nachricht
        frist_todesgefahr = parameters(period).zgb.verschollenheit.frist_todesgefahr_monate
        frist_nachrichtlos = parameters(period).zgb.verschollenheit.frist_nachrichtlos_monate

        antrag_todesgefahr = in_todesgefahr * (dauer_todesgefahr >= frist_todesgefahr)
        antrag_nachrichtlos = nachrichtlos * (dauer_nachricht >= frist_nachrichtlos)

        return (antrag_todesgefahr + antrag_nachrichtlos) > 0
