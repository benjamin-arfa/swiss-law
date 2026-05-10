"""SR 0.142.116.909 Art. 25

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# This legal article text does not define a variable.
class treatytermination_variable(Variable):
    value_type = bool
    entity = Institution
    definition_period = YEAR
    label = "Termination of Treaty (Art. 25 SR 0.142.116.909)"

    def formula(institution, period, parameters):
        termination_date = parameter('treatytermination', period)
        return institution.date > termination_date
