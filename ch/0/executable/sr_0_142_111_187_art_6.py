"""SR 0.142.111.187 Art. 6

Generated from: ch/0/de/0.142.111.187.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

## Since Art. 6 of the Federal Act on International Compensatory Allowances does not introduce a specific regulation, no OpenFisca variable is required.
