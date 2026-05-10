"""SR 0.103.1 Art. 2

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rights_entitlement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Right of non-nationals to social benefits (Art. 2 Charter)"

    def formula(person, period, parameters):
        nationality = person("nationality", period)
        contract_state = parameters(period).covenants.contract_states.all
        return (nationality in contract_state)
