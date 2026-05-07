"""SR 0.101.093 Art. 6

Generated from: ch/0/de/0.101.093.md
"""

import numpy as np
from datetime import date
from openfisca_core import periods
from openfisca_core.variables import Variable
from openfisca_core.pensions import build_person

class HasRatifiedConventionDate(Variable):
    value_type = bool
    entity = person
    label = u"Person has ratified the Convention"
    definition_period = ETERNITY

    def formula_2019_01(people, period, parameters):
        return people("has_convention_ratified_by", period).exists()

class HasRatifiedProtocolDate(Variable):
    value_type = bool
    entity = person
    label = u"Person has ratified the Protocol"
    definition_period = ETERNITY
    
    def formula_sia(people, period, parameters):
        return people("has_ratifed_convention_date"): np.maximum(people("has_convention_ratified_by", period), date.today())
