"""SR 0.142.116.909 Art. 23

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Parameterized exceptions in the AHV treaty

class ahv_treaty_exceptions(Variable):
    value_type = bool
    start = '2023-01-01'
    label = "Exemptions to the Switzerland - International Agreement (AHV treaty)"

    def formula(person, period, parameters):
        return False  # This is a constant placeholder, as AHV treaty exceptions are fixed per-person and don't have parameters.
