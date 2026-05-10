"""SR 981 Art. 9

Generated from: ch/de/981.md

Special provisions for trivial cases: exclusion from compensation,
uniform compensation amounts, and simplified procedure.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bagatellfall_von_abgeltung_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission Bagatellfaelle von der Abgeltung ausschliesst"
    reference = "SR 981 Art. 9 Bst. a"


class bagatellfall_einheitliche_entschaedigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fuer bestimmte Kategorien von Bagatellfaellen einheitliche Entschaedigungen festgesetzt werden"
    reference = "SR 981 Art. 9 Bst. b"


class bagatellfall_summarisches_verfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fuer bestimmte Kategorien von Bagatellfaellen ein summarisches Verfahren angewendet wird"
    reference = "SR 981 Art. 9 Bst. c"
