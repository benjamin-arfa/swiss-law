"""SR 831.30 Art. 6

Generated from: ch/831/de/831.30.md

Art. 6: Mindestalter - Persons entitled to a helplessness allowance only
have a right to supplementary benefits once they have reached the age of 18.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Alter der Person in Jahren"
    reference = "SR 831.30 Art. 6"


class el_mindestalter_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestalter 18 fuer EL bei Hilflosenentschaedigung erfuellt (Art. 6 ELG)"
    reference = "SR 831.30 Art. 6"

    def formula(person, period, parameters):
        alter = person('el_alter', period)
        return alter >= 18
