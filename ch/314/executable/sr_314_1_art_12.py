"""SR 314.1 Art. 12

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class verfahrenskosten_ordnungsbussenverfahren(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verfahrenskosten im Ordnungsbussenverfahren (immer 0)"
    reference = "SR 314.1 Art. 12"
    default_value = 0.0
