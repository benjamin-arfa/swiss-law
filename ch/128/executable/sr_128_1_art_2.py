"""SR 128.1 Art. 2

Generated from: ch/128/de/128.1.md

Geltungsbereich: The ordinance applies to the Federal Council, departments,
Federal Chancellery, and the army. Special rules for decentralised units
and cantons.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_bundesrat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation der Bundesrat ist"
    reference = "SR 128.1 Art. 2 Abs. 1 Bst. a"


class ist_departement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ein Departement ist"
    reference = "SR 128.1 Art. 2 Abs. 1 Bst. b"


class ist_bundeskanzlei_oder_bundesamt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation die BK, ein Generalsekretariat, eine Gruppe oder ein Bundesamt ist"
    reference = "SR 128.1 Art. 2 Abs. 1 Bst. c"


class ist_armee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation die Armee ist"
    reference = "SR 128.1 Art. 2 Abs. 1 Bst. d"


class isv_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ISV auf die Organisation anwendbar ist"
    reference = "SR 128.1 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        br = person('ist_bundesrat', period)
        dep = person('ist_departement', period)
        bk = person('ist_bundeskanzlei_oder_bundesamt', period)
        armee = person('ist_armee', period)
        return br + dep + bk + armee > 0
