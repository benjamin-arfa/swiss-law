"""SR 210 Art. 32

Generated from: ch/de/210.md

Beweis fuer Geburt und Tod - Beweislast: Wer zur Ausuebung eines Rechtes
sich darauf beruft, dass eine Person lebe oder gestorben sei oder zu einer
bestimmten Zeit gelebt oder eine andere Person ueberlebt habe, hat hiefuer
den Beweis zu erbringen. Kann nicht bewiesen werden, dass von mehreren
gestorbenen Personen die eine die andere ueberlebt habe, so gelten sie als
gleichzeitig gestorben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class beruft_sich_auf_leben_oder_tod(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob sich die Person auf Leben oder Tod einer anderen Person beruft"
    reference = "SR 210 Art. 32 Abs. 1"


class hat_beweis_leben_oder_tod(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Beweis fuer Leben oder Tod erbracht wurde"
    reference = "SR 210 Art. 32 Abs. 1"


class traegt_beweislast_art32(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person die Beweislast fuer Leben/Tod traegt (Art. 32 ZGB)"
    reference = "SR 210 Art. 32"

    def formula(person, period, parameters):
        # Abs. 1: Wer sich auf Leben/Tod beruft, traegt die Beweislast
        return person('beruft_sich_auf_leben_oder_tod', period)
