"""SR 836.21 Art. 1 - Education allowance (Ausbildungszulage)

Art. 1: Entitlement to an education allowance exists for children who are
undergoing post-compulsory education (Art. 49bis/49ter AHVV). Post-compulsory
education is education following compulsory schooling; the duration and end of
compulsory schooling are governed by cantonal law.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class kind_in_nachobligatorischer_ausbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is in post-compulsory education (Art. 1 par. 1 FamZV)"
    default_value = False


class obligatorische_schulzeit_beendet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child has completed compulsory schooling (Art. 1 par. 2 FamZV)"
    default_value = False


class anspruch_ausbildungszulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to education allowance (Art. 1 FamZV)"

    def formula(person, period, parameters):
        in_ausbildung = person("kind_in_nachobligatorischer_ausbildung", period)
        schule_beendet = person("obligatorische_schulzeit_beendet", period)
        return in_ausbildung * schule_beendet
