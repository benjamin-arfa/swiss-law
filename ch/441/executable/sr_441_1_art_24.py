"""SR 441.1 Art. 24

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ausschluss_mehrfachunterstuetzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Für dieselbe Massnahme können nicht mehrere Finanzhilfen nach SpG gewährt werden"
    reference = "SR 441.1, Art. 24"

    def formula(self, period, parameters):
        # If already receiving financial aid for this measure under SpG, no additional SpG aid
        erhaelt_bereits_finanzhilfe_spg = self.person('erhaelt_bereits_finanzhilfe_spg', period)
        return erhaelt_bereits_finanzhilfe_spg


class erhaelt_bereits_finanzhilfe_spg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erhält bereits eine Finanzhilfe nach dem Sprachengesetz für dieselbe Massnahme"
    reference = "SR 441.1, Art. 24"
