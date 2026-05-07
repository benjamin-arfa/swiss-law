"""SR 0.142.116.902 Art. 10

Generated from: ch/0/de/0.142.116.902.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# No new variable is created as per the reasoning; OpenFisca does not model geographical regions or entities inherently.
