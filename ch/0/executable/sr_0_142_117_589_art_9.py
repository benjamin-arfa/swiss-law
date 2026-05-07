"""SR 0.142.117.589 Art. 9

Generated from: ch/0/de/0.142.117.589.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

To implement such a variable, a custom project would be needed.
