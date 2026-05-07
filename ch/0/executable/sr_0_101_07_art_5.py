"""SR 0.101.07 Art. 5

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY

class MarriageRightsEqualization(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "Marriage rights equalization"
