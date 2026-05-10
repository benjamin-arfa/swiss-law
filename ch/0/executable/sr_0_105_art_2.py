"""SR 0.105 Art. 2

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prevent_torture_obligation(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Obligation to prevent torture under the UN Convention (Art. 2 SR 0.105)"

    def formula(countries, period, parameters):
        return True  # Binding obligations under an international treaty cannot be waived

class war_declaration_allowed(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Whether war can be declared under article 2 SR 0.105"

    def formula(countries, period, parameters):
        # According to Art. 2, para. 2, no extraordinary circumstances can be invoked to justify torture,
        # implying war (as a state of extraordinary circumstances) cannot be declared under these obligations.
        return False

class superior_order_permitted(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Whether orders by superiors or public authority agents can be used to authorize torture"

    def formula(countries, period, parameters):
        return False  # According to Art. 2, para. 3, NO such orders can be invoked
