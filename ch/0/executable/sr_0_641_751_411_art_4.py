"""SR 0.641.751.411 Art. 4 - Revenue sharing: financing environmental taxes

Art. 4: Revenues from financing environmental taxes are paid into a
common fund managed by Switzerland.
Each contracting state receives compensations for eligible benefits.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class recettes_taxes_financement_ch_li(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total financing environmental tax revenues CH + LI (Art. 4 par. 1)"
    default_value = 0


class compensation_ch_taxes_financement(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Switzerland's compensation from common fund (Art. 4 par. 2)"
    default_value = 0


class compensation_li_taxes_financement(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Liechtenstein's compensation from common fund (Art. 4 par. 2)"
    default_value = 0
