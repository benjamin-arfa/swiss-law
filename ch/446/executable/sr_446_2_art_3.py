"""SR 446.2 Art. 3

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_werbefilm(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein Werbefilm"
    reference = "SR 446.2 Art. 3 Abs. 1"


class ist_redaktioneller_beitrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein von einer Redaktion gestalteter Beitrag"
    reference = "SR 446.2 Art. 3 Abs. 1"


class ist_fernsehprogramm_schweizer_veranstalter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Fernsehprogramm eines schweizerischen Programmveranstalters nach Art. 2 Bst. d RTVG"
    reference = "SR 446.2 Art. 3 Abs. 2"


class jsfvg_sachlich_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "JSFVG ist sachlich anwendbar (kein Ausschluss nach Art. 3)"
    reference = "SR 446.2 Art. 3"

    def formula(person, period, parameters):
        werbefilm = person('ist_werbefilm', period)
        redaktionell = person('ist_redaktioneller_beitrag', period)
        tv_schweiz = person('ist_fernsehprogramm_schweizer_veranstalter', period)
        return not_(werbefilm) * not_(redaktionell) * not_(tv_schweiz)
