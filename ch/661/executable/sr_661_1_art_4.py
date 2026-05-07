"""SR 661.1 Art. 4

Generated from: ch/661/de/661.1.md

Art. 4 Auslandjahr (Year abroad):
A year abroad under Art. 4a Abs. 2 WPEG means 12 consecutive calendar months
during which the Swiss citizen, regardless of age:
a. lives abroad; or
b. stays abroad with military/civil service leave.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wpev_monate_im_ausland(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of consecutive months living/staying abroad"
    reference = "SR 661.1 Art. 4"


class wpev_auslandjahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person qualifies as having an 'Auslandjahr' (12 consecutive months abroad)"
    reference = "SR 661.1 Art. 4"

    def formula(person, period, parameters):
        monate = person('wpev_monate_im_ausland', period)
        return monate >= 12
