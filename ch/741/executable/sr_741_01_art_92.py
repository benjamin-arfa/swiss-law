"""SR 741.01 Art. 92 - Pflichtwidriges Verhalten bei Unfall

Generated from: ch/de/741/741.01.md

Hit-and-run / accident duty violations:
- Abs. 1: Busse (violation of accident duties)
- Abs. 2: Freiheitsstrafe bis 3 Jahre / Geldstrafe (fleeing after
  causing injury/death)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class unfallpflicht_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Unfallpflichten nach SVG verletzt wurden"
    reference = "SR 741.01 Art. 92 Abs. 1"


class unfall_person_verletzt_oder_getoetet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob beim Unfall ein Mensch verletzt oder getoetet wurde"
    reference = "SR 741.01 Art. 92 Abs. 2"


class fahrerflucht_nach_personenschaden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Fahrzeugfuehrer nach Personenschaden die Flucht ergriffen hat"
    reference = "SR 741.01 Art. 92 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('unfallpflicht_verletzt', period)
            * person('unfall_person_verletzt_oder_getoetet', period)
            * person('ist_motorfahrzeugfuehrer', period)
        )


class art92_strafe_freiheitsstrafe_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Freiheitsstrafe nach Art. 92 SVG in Jahren"
    reference = "SR 741.01 Art. 92"

    def formula(person, period, parameters):
        flucht = person('fahrerflucht_nach_personenschaden', period)
        return where(flucht, 3, 0)
