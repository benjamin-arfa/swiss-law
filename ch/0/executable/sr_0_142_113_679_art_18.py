"""SR 0.142.113.679 Art. 18

Generated from: ch/0/de/0.142.113.679.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Currently, this is a more complex social security question, requiring custom implementation
# A variable for 'Mixed Committee' would likely involve some custom logic for the committee's
# tasks, such as reporting proposals and monitoring activity.
