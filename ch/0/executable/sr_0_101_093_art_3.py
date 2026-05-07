"""SR 0.101.093 Art. 3

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.variables import Variable
from openfisca_core.period import YEAR

class VerbottenVorbehalte(Variable):
    value_type = bool
    entity = 'Person'
    label = 'Verbot von Vorbehalten'  # Translated as "Prohibition on reservations"
    definition_period = YEAR
    default_value = False
