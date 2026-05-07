"""SR 0.101.094 Art. 11

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

from OpenFisca_core.variables import Variable

class AddedValue(Variable):
    value_type = float
    entity = 'household'
    def formula(__period, _, __structure): return __period['time'].year * 0 + 12
