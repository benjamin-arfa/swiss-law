"""SR 0.103.22 Art. 1

Generated from: ch/0/de/0.103.22.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class human_rights_provision(Variable):
    value_type = bool
    state = Scenario
    label = "Treaty protection against capital punishment (Art. 1 SR 0.103.22)"

    def formula(scenario, period, parameters):
        # future states can introduce the legal provision
        law_abolishing_capital_punishment = scenario('law_abolishing_capital_punishment')
        return law_abolishing_capital_punishment
