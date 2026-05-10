"""SR 513.52 Art. 6

Generated from: ch/513/de/513.52.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rkd_grundausbildung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Grundausbildung RKD erfolgreich abgeschlossen"


class rkd_mindestens_ein_ausbildungsdienst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mindestens ein Ausbildungsdienst geleistet"


class rkd_befoerderung_durch_srk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befoerderung durch das SRK erfolgt"


class rkd_kaderfunktion_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen fuer Kaderfunktion im RKD erfuellt (Art. 6 Abs. 2 SR 513.52)"
    reference = "SR 513.52 Art. 6"

    def formula(person, period, parameters):
        # Die Zuweisung der Kaderfunktion setzt voraus:
        # 1. erfolgreicher Abschluss der Grundausbildung
        # 2. mindestens ein Ausbildungsdienst
        # 3. Befoerderung durch das SRK
        grundausbildung = person('rkd_grundausbildung_bestanden', period)
        ein_dienst = person('rkd_mindestens_ein_ausbildungsdienst', period)
        befoerderung = person('rkd_befoerderung_durch_srk', period)
        return grundausbildung * ein_dienst * befoerderung
