"""SR 151.1 Art. 6

Generated from: ch/151/de/151.1.md

Beweislasterleichterung: Diskriminierung wird vermutet, wenn sie
von der betroffenen Person glaubhaft gemacht wird.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class diskriminierung_glaubhaft_gemacht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffene Person eine Diskriminierung glaubhaft gemacht hat"
    reference = "SR 151.1 Art. 6"


class diskriminierung_vermutet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Diskriminierung vermutet wird (Beweislastumkehr)"
    reference = "SR 151.1 Art. 6"

    def formula(person, period, parameters):
        return person('diskriminierung_glaubhaft_gemacht', period)
