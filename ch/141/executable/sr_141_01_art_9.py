"""SR 141.01 Art. 9

Generated from: ch/141/de/141.01.md

Beruecksichtigung der persoenlichen Verhaeltnisse: Die zustaendige
Behoerde kann von den Kriterien nach Art. 6, 7 und 11 abweichen bei
Behinderung, Krankheit oder anderen gewichtigen persoenlichen Umstaenden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class behinderung_vorliegend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine koerperliche, geistige oder psychische Behinderung vorliegt"
    reference = "SR 141.01 Art. 9 Bst. a"


class schwere_krankheit_vorliegend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine schwere oder lang andauernde Krankheit vorliegt"
    reference = "SR 141.01 Art. 9 Bst. b"


class gewichtige_persoenliche_umstaende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob andere gewichtige persoenliche Umstaende vorliegen (Lernschwaeche, Erwerbsarmut, Betreuungsaufgaben, etc.)"
    reference = "SR 141.01 Art. 9 Bst. c"


class abweichung_integrationskriterien_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Abweichung von den Integrationskriterien (Art. 6, 7, 11) aufgrund persoenlicher Verhaeltnisse moeglich ist"
    reference = "SR 141.01 Art. 9"

    def formula(person, period, parameters):
        behinderung = person('behinderung_vorliegend', period)
        krankheit = person('schwere_krankheit_vorliegend', period)
        umstaende = person('gewichtige_persoenliche_umstaende', period)
        return (behinderung + krankheit + umstaende) > 0
