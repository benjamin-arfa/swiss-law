"""SR 0.104 Art. 22

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# In OpenFisca, we don't create a variable, but an input parameter for the Swiss agreement entities could possibly be implemented here.
