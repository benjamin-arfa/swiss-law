"""SR 0.142.117.121 Art. 15

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

empty, since this article does not create any OpenFisca variables or impact on fiscal calculations
