"""SR 0.106 Art. 3

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

No OpenFisca variable needs to be defined here, as there is no monetary threshold or rate.
