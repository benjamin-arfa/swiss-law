"""SR 0.105 Art. 28

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

''' 
OpenFisca-specific information:
Description: Art 28 AHV option
'''


class ahv_state_sovereignty_opt_out(Variable):
    value_type = bool
    entity = State
    definition_period = DAY
    label = "Does the state opt-out of AHV sovereignty (Art 28 AHVG)?"

    def formula(state, period, parameters):
        opted_out_initially = state("ahv_state_sovereignty_opt_out_initial", period)
        opt_out_canceled = state('opt_out_canceled', period)
        return (opted_out_initially | ~opt_out_canceled)
