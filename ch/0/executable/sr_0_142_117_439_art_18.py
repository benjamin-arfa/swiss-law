"""SR 0.142.117.439 Art. 18

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

This article does not pertain to the calculation of AHV/IV/EO amounts or rates. Hence, the necessary formulas for these calculations can be left unchanged.
