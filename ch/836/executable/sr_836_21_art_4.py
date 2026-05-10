"""SR 836.21 Art. 4 - Stepchildren (Stiefkinder)

Art. 4: Entitlement to family allowances exists for stepchildren if the
stepchild predominantly lives in the stepparent's household (or lived there
until reaching majority). Children of a registered partner under the
Partnership Act (SR 211.231) are also considered stepchildren.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_stiefkind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is a stepchild (Art. 4 FamZV)"
    default_value = False


class stiefkind_lebt_im_haushalt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Stepchild predominantly lives in stepparent's household (Art. 4 par. 1 FamZV)"
    default_value = False


class anspruch_familienzulagen_stiefkind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to family allowances for stepchild (Art. 4 FamZV)"

    def formula(person, period, parameters):
        ist_stief = person("ist_stiefkind", period)
        im_haushalt = person("stiefkind_lebt_im_haushalt", period)
        return ist_stief * im_haushalt
