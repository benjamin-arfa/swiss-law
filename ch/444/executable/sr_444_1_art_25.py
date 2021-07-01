"""SR 444.1 Art. 25

Generated from: ch/444/de/444.1.md

Uebertretungen im Kunsthandel/Auktionswesen: Busse bis 20'000 CHF.
Versuch und Gehilfenschaft strafbar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sorgfaltspflicht_missachtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Sorgfaltspflichten im Kunsthandel missachtet wurden"
    reference = "SR 444.1 Art. 25 Abs. 1 Bst. a"


class kontrolle_vereitelt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kontrolle vereitelt wurde"
    reference = "SR 444.1 Art. 25 Abs. 1 Bst. b"


class max_busse_uebertretung_kunsthandel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Uebertretung im Kunsthandel (CHF)"
    reference = "SR 444.1 Art. 25 Abs. 1"
    default_value = 20000
