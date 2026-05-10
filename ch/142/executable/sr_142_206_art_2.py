"""SR 142.206 Art. 2

Generated from: ch/142/de/142.206.md

Begriffe: Definitionen von Schengen-Staat, Schengen-Aussengrenzen,
Drittstaatsangehoerige, terroristische Straftat, sonstige schwere Straftat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_drittstaatsangehoeriger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Angehoerige/r eines Staates ist, der weder EU- noch EFTA-Mitglied ist"
    reference = "SR 142.206 Art. 2 Abs. 1 Bst. c"


class ist_schengen_aussengrenze(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kontrolle an einer Schengen-Aussengrenze stattfindet"
    reference = "SR 142.206 Art. 2 Abs. 1 Bst. b"


class ist_terroristische_straftat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine terroristische Straftat nach Anhang 1a der N-SIS-Verordnung vorliegt"
    reference = "SR 142.206 Art. 2 Abs. 1 Bst. d"


class ist_sonstige_schwere_straftat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine sonstige schwere Straftat nach Anhang 1b der N-SIS-Verordnung vorliegt"
    reference = "SR 142.206 Art. 2 Abs. 1 Bst. e"
