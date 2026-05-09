"""SR 836.21 Art. 5 - Foster children (Pflegekinder)

Art. 5: Entitlement to family allowances exists for foster children if they
have been taken in for gratuitous permanent care and upbringing within the
meaning of Art. 49 par. 1 AHVV (SR 831.101).

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class ist_pflegekind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is a foster child (Art. 5 FamZV)"
    default_value = False


class pflegekind_unentgeltlich_dauerpflege(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Foster child taken in for gratuitous permanent care (Art. 49 par. 1 AHVV)"
    default_value = False


class anspruch_familienzulagen_pflegekind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to family allowances for foster child (Art. 5 FamZV)"

    def formula(person, period, parameters):
        ist_pflege = person("ist_pflegekind", period)
        unentgeltlich = person("pflegekind_unentgeltlich_dauerpflege", period)
        return ist_pflege * unentgeltlich
