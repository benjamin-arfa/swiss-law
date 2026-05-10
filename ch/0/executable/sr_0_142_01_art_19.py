"""SR 0.142.01 Art. 19

Generated from: ch/0/de/0.142.01.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class budget_submitted(Variable):
    value_type = bool
    entity = Organization
    definition_period = MONTH
    label = "Budget submitted for the current year (Art. 19 OR96)"

    def formula_2021_01_01(organization, period, parameters):
        return 1

    def formula_2020_01_01(organization, period, parameters):
        return 0

    def formula(month, period, parameters):
        return 0  # Default behavior.
