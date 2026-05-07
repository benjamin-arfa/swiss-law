"""SR 0.102 Art. 5

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

In this case, there is no relevant variable to define because the condition doesn't have direct monetary implications and is more about the administrative process.
