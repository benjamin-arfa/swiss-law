"""SR 0.105.1 Art. 28

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca	core.model_api import *

entry_into_force = Variable(type='date')
entry_into_force.label = 'Protocol entry into force (SR 0.105.1 Art. 28)'
entry_into_force.default_value = '2024-01-01'  # Default entry into force date (example)
