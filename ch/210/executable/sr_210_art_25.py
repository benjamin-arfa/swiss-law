"""SR 210 Art. 25

Generated from: ch/de/210.md

Wohnsitz Minderjaehriger: Als Wohnsitz des Kindes unter elterlicher Sorge
gilt der Wohnsitz der Eltern. Bei getrenntem Wohnsitz der Eltern gilt der
Wohnsitz des Elternteils mit Obhut. Bevormundete Kinder haben Wohnsitz
am Sitz der Kindesschutzbehoerde.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_unter_elterlicher_sorge(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Kind unter elterlicher Sorge steht"
    reference = "SR 210 Art. 25 Abs. 1"


class eltern_haben_gemeinsamen_wohnsitz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Eltern einen gemeinsamen Wohnsitz haben"
    reference = "SR 210 Art. 25 Abs. 1"


class ist_bevormundetes_kind(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Kind bevormundet ist"
    reference = "SR 210 Art. 25 Abs. 2"


class wohnsitz_folgt_eltern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Wohnsitz dem der Eltern folgt (abgeleiteter Wohnsitz)"
    reference = "SR 210 Art. 25"

    def formula(person, period, parameters):
        ist_minderjaehrig = not_(person('ist_volljaehrig', period))
        unter_elterlicher_sorge = person('ist_unter_elterlicher_sorge', period)
        ist_bevormundet = person('ist_bevormundetes_kind', period)

        # Abs. 1: Kind unter elterlicher Sorge -> Wohnsitz der Eltern
        # Abs. 2: Bevormundete Kinder -> Sitz der Kindesschutzbehoerde
        return ist_minderjaehrig * (unter_elterlicher_sorge + ist_bevormundet > 0)
