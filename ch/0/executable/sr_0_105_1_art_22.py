"""SR 0.105.1 Art. 22

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

There is no corresponding Variable in this case, as it's a requirement for authorities rather than an economic parameter.
