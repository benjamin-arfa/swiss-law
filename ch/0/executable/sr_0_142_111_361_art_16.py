"""SR 0.142.111.361 Art. 16

Generated from: ch/0/de/0.142.111.361.md
"""

from openfisca_core.model_api import *
import numpy as np


class personnel_transportation_costs(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Personnel transportation costs (Art. 16)">

    def formula(person, period, parameters):
        return np.nan
