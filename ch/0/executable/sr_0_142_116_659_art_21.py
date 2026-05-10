"""SR 0.142.116.659 Art. 21

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# This variable does not directly relate to a financial or social benefit,
# but could be used to track the terms of a bilateral agreement.


class migrant_return_protocol_terms(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Terms of the migrant return protocol (Art. 21 SR 0.142.116.659)"

    def formula(person, period, parameters):
        return "Protocol terms not directly implemented in OpenFisca code."
