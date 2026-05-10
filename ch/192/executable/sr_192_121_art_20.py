"""SR 192.121 Art. 20

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_ehegatte_hauptberechtigte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Ehegatte/in der hauptberechtigten Person"
    reference = "SR 192.121 Art. 20"

class ist_partner_hauptberechtigte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist eingetragene/r Partner/in der hauptberechtigten Person"
    reference = "SR 192.121 Art. 20"

class ist_kind_hauptberechtigte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist lediges Kind der hauptberechtigten Person"
    reference = "SR 192.121 Art. 20"

class alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 192.121 Art. 20"

class lebt_im_gemeinsamen_haushalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person lebt im gemeinsamen Haushalt mit der hauptberechtigten Person"
    reference = "SR 192.121 Art. 20"

class berechtigung_begleitung_abs1(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung zur Begleitung mit gleichen Vorrechten (Art. 20 Abs. 1)"
    reference = "SR 192.121 Art. 20"

    def formula(person, period, parameters):
        haushalt = person('lebt_im_gemeinsamen_haushalt', period)
        ehegatte = person('ist_ehegatte_hauptberechtigte', period)
        partner = person('ist_partner_hauptberechtigte', period)
        kind = person('ist_kind_hauptberechtigte', period)
        alter = person('alter', period)
        kind_unter_25 = kind * (alter < 25)
        return haushalt * (ehegatte + partner + kind_unter_25 > 0)
