"""SR 142.318 Art. 2

Generated from: ch/142/de/142.318.md

Voruebergehende Nutzung von militaerischen Bauten und Anlagen des Bundes:
Erneute Nutzung kann unterbruchslos erfolgen, VBS hat Prioritaet.
Anzeigefrist wird auf 5 Tage verkuerzt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class militaerische_bauten_unterbruchslose_nutzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob militaerische Bauten und Anlagen unterbruchslos erneut genutzt werden koennen"
    reference = "SR 142.318 Art. 2 Abs. 1"

    def formula_2020_04(person, period, parameters):
        return True


class vbs_hat_prioritaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Beduerfnisse des VBS Prioritaet haben"
    reference = "SR 142.318 Art. 2 Abs. 1"

    def formula_2020_04(person, period, parameters):
        return True


class anzeigefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzeigefrist in Tagen gemaess Art. 24c Abs. 4 AsylG (verkuerzt)"
    reference = "SR 142.318 Art. 2 Abs. 2"

    def formula_2020_04(person, period, parameters):
        return parameters(period).anzeigefrist_militaerische_bauten_tage
