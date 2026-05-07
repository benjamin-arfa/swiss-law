"""SR 0.101.3 Art. 3

Generated from: ch/0/de/0.101.3.md
"""

import pandas as pd
import numpy as np

from openfisca_core.model_api import *
from openfisca_core.periods import ETERNITY

class FreeMovement(Entity):
    formula = "1"
    values = {
        'in_prison': False
    }
    variables = {
        _duration_: Formula(
            "person('in_prison', period) and ((period == ETERNITY) or ((period.earliest == index_period)))"
        ),
        _rights_granted_: Formula(
            "PERSON() != 'in_prison' or person('in_prison', period) == person('unrestricted_correspondence', period)"
        )
    }

class UnrestrictedCorrespondence(Entity):
    formula = "1"
    values = {
        'receiving_correspondence_without_delays': False,
        'disciplinary_measures_after_proper_communication': False,
        'right_to_communicate_with_lawyer': False
    }
    variables = {
    }
