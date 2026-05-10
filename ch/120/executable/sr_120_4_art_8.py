"""SR 120.4 Art. 8

Generated from: ch/120/de/120.4.md

Vorabklaerung: If a person was checked within the last 5 years, a new check
may be waived.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class letzte_psp_innerhalb_5_jahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person innerhalb von 5 Jahren vor Vorabklaerung bereits einer PSP unterzogen wurde"
    reference = "SR 120.4 Art. 8 Abs. 1"


class verzicht_auf_psp_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob auf die PSP verzichtet werden kann (Vorabklaerung)"
    reference = "SR 120.4 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('letzte_psp_innerhalb_5_jahren', period)


class psp_einleitung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine neue PSP eingeleitet werden muss"
    reference = "SR 120.4 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        return not_(person('letzte_psp_innerhalb_5_jahren', period))
