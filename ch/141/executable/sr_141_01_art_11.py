"""SR 141.01 Art. 11

Generated from: ch/141/de/141.01.md

Enge Verbundenheit mit der Schweiz: Mindestens 3 Aufenthalte von je
5 Tagen in den letzten 6 Jahren, muendliche Verstaendigung in einer
Landessprache, Grundkenntnisse, Kontakte zu Schweizern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class aufenthalte_schweiz_6_jahre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob mindestens 3 Aufenthalte von je mindestens 5 Tagen in der Schweiz in den letzten 6 Jahren erfolgt sind"
    reference = "SR 141.01 Art. 11 Abs. 1 Bst. a"


class muendliche_verstaendigung_landessprache(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person im Alltag muendlich in einer Landessprache verstaendigen kann"
    reference = "SR 141.01 Art. 11 Abs. 1 Bst. b"


class enge_verbundenheit_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine enge Verbundenheit mit der Schweiz vorliegt"
    reference = "SR 141.01 Art. 11"

    def formula(person, period, parameters):
        aufenthalte = person('aufenthalte_schweiz_6_jahre', period)
        sprache = person('muendliche_verstaendigung_landessprache', period)
        kenntnisse = person('grundkenntnisse_schweiz', period)
        kontakte = person('kontakte_zu_schweizern', period)
        return aufenthalte * sprache * kenntnisse * kontakte
