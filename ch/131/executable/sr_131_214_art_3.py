"""SR 131.214 Art. 3

Generated from: ch/131/de/131.214.md

Bürgerrecht: Kantons- und Gemeindebürgerrecht sind untrennbar miteinander
verbunden. Die Gesetzgebung regelt die Erteilung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_gemeindebuergerrecht_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person das Gemeindebürgerrecht in einer Urner Gemeinde besitzt"
    reference = "SR 131.214 Art. 3 Abs. 1"


class hat_kantonsbuergerrecht_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person das Kantonsbürgerrecht Uri besitzt"
    reference = "SR 131.214 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # Kantons- und Gemeindebürgerrecht sind untrennbar verbunden
        return person('hat_gemeindebuergerrecht_uri', period)
