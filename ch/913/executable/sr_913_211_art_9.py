"""SR 913.211 Art. 9

Generated from: ch/913/de/913.211.md

Voraussetzungen für besonders innovative Projekte:
- Problemlösung ist im betreffenden Gebiet erstmalig (Pilotprojekt)
- Projekt hat Modellcharakter
- Anforderungen der Nachhaltigkeit überdurchschnittlich berücksichtigt
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_pilotprojekt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Problemlösung im betreffenden Gebiet erstmalig ist (Pilotprojekt)"
    reference = "SR 913.211 Art. 9 Bst. a"


class hat_modellcharakter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt Modellcharakter hat"
    reference = "SR 913.211 Art. 9 Bst. b"


class nachhaltigkeit_ueberdurchschnittlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Nachhaltigkeitsanforderungen überdurchschnittlich berücksichtigt werden"
    reference = "SR 913.211 Art. 9 Bst. c"


class ist_besonders_innovatives_projekt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt als besonders innovativ gilt (erhöhte Investitionskredite)"
    reference = "SR 913.211 Art. 9"

    def formula(person, period, parameters):
        return (
            person('ist_pilotprojekt', period) *
            person('hat_modellcharakter', period) *
            person('nachhaltigkeit_ueberdurchschnittlich', period)
        )
