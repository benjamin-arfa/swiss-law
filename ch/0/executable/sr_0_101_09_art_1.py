"""SR 0.101.09 Art. 1

Generated from: ch/0/de/0.101.09.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

import numpy as np

class Bisheriger_Wortlaut(Variable):
    value_type = float
    label = "Bisheriger Wortlaut"

    def __new__(cls, tax_benefit_system, period):
        return 0

This Python class is defined as per the requirement. It can inherit from Variable and can be modified if required to implement logic related to the legal article. It simply returns a float of 0.
