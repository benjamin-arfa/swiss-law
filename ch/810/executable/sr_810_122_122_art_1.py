"""SR 810.122.122 Art. 1

Generated from: ch/810/de/810.122.122.md

Bezeichnung der genetischen Untersuchungen: Personen mit Titel nach
Art. 6 Abs. 1 Bst. b-f GUMV sind zur Durchfuehrung molekulargenetischer
Untersuchungen gemaess Anhang zugelassen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_titel_gumv_art6(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einen Titel nach Art. 6 Abs. 1 Bst. b-f GUMV besitzt"
    reference = "SR 810.122.122 Art. 1"


class zugelassen_molekulargenetische_untersuchungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person zur Durchfuehrung molekulargenetischer Untersuchungen gemaess Anhang zugelassen ist"
    reference = "SR 810.122.122 Art. 1"

    def formula(person, period, parameters):
        return person('hat_titel_gumv_art6', period)
