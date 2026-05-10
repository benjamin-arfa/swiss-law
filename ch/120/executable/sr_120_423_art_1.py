"""SR 120.423 Art. 1

Generated from: ch/120/de/120.423.md

Gegenstand: Festlegung der jeweiligen Pruefstufe fuer
Funktionen des VBS und der Armee nach PSPV.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_funktion_vbs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine Funktion des VBS nach Anhang 1 PSPV ausubt"
    reference = "SR 120.423 Art. 1 Abs. 1 Bst. a"


class hat_funktion_armee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine Funktion der Armee nach Anhang 2 PSPV ausubt"
    reference = "SR 120.423 Art. 1 Abs. 1 Bst. b"


class pruefstufe_vbs(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Pruefstufe nach Art. 9 Abs. 1 PSPV fuer VBS-Funktionen (gemaess Anhang 1)"
    reference = "SR 120.423 Art. 1 Abs. 2"


class pruefstufe_armee(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Pruefstufe nach Art. 9 Abs. 1 PSPV fuer Armee-Funktionen (gemaess Anhang 2)"
    reference = "SR 120.423 Art. 1 Abs. 3"


class pruefstufe_personensicherheitspruefung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwendbare Pruefstufe der Personensicherheitspruefung"
    reference = "SR 120.423 Art. 1"

    def formula(person, period, parameters):
        vbs = person('hat_funktion_vbs', period)
        armee = person('hat_funktion_armee', period)
        stufe_vbs = person('pruefstufe_vbs', period)
        stufe_armee = person('pruefstufe_armee', period)
        return where(vbs, stufe_vbs, where(armee, stufe_armee, 0))
