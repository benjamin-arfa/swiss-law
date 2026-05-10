"""SR 131.217 Art. 20

Generated from: ch/131/de/131.217.md

Bürgerrecht: Das Kantonsbürgerrecht begründet alle Rechte und Pflichten
eines Bürgers des Bundes, des Kantons und der Gemeinde.
Das Kantonsbürgerrecht ist mit dem Gemeindebürgerrecht untrennbar verbunden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_gemeindebuergerrecht_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person das Gemeindebürgerrecht in einer Glarner Gemeinde besitzt"
    reference = "SR 131.217 Art. 20 Abs. 2"


class hat_kantonsbuergerrecht_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person das Kantonsbürgerrecht Glarus besitzt"
    reference = "SR 131.217 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        # Kantonsbürgerrecht ist mit Gemeindebürgerrecht untrennbar verbunden
        return person('hat_gemeindebuergerrecht_gl', period)


class hat_bundesbuergerrechte_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Glarner Kantonsbürger alle Rechte eines Bundesbürgers hat"
    reference = "SR 131.217 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        return person('hat_kantonsbuergerrecht_gl', period)
