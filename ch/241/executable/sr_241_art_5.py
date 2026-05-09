"""SR 241 Art. 5

Generated from: ch/de/241.md

Exploitation of others' work: unauthorized use of entrusted
work results, use of improperly obtained work results,
or technical reproduction of market-ready work of others.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class unbefugte_verwertung_anvertrautes_ergebnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein anvertrautes Arbeitsergebnis unbefugt verwertet wird"
    reference = "SR 241 Art. 5 Bst. a"


class verwertung_unbefugt_erlangtes_ergebnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein unbefugt erlangtes Arbeitsergebnis Dritter verwertet wird"
    reference = "SR 241 Art. 5 Bst. b"


class technische_reproduktion_fremder_leistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein marktreifes Arbeitsergebnis durch technische Reproduktion uebernommen wird"
    reference = "SR 241 Art. 5 Bst. c"
