"""SR 0.101.094 Art. 20

Generated from: ch/0/de/0.101.094.md
"""

import numpy as np

import numpy as np
from openfisca_core import formulas
from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY
from openfisca_country_templates import settings
from openfisca_core import periods

class Article_20_Var(Variable):
    value_type = int
    entity = person
    label = u"Art. 20 Var."
    definition_period = ETERNITY

    def formula(person, period, parameters):
        protocol_entry_year = parameters(period).protocol_entry_year
        case_year = person('reference_year', period)
        return np.where(case_year > protocol_entry_year, 1, 0)
