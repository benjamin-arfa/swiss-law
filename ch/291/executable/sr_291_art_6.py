"""SR 291 Art. 6

Generated from: ch/291/de/291.md

Einlassung: In vermoegensrechtlichen Streitigkeiten begruendet die
vorbehaltlose Einlassung die Zustaendigkeit des angerufenen schweizerischen
Gerichtes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_vermoegensrechtliche_streitigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine vermoegensrechtliche Streitigkeit vorliegt"
    reference = "SR 291 Art. 6"


class vorbehaltlose_einlassung_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich der Beklagte vorbehaltlos auf das Verfahren eingelassen hat"
    reference = "SR 291 Art. 6"


class zustaendigkeit_durch_einlassung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustaendigkeit durch vorbehaltlose Einlassung begruendet ist"
    reference = "SR 291 Art. 6"

    def formula(person, period, parameters):
        vermoegen = person('ist_vermoegensrechtliche_streitigkeit', period)
        einlassung = person('vorbehaltlose_einlassung_erfolgt', period)
        return vermoegen * einlassung
