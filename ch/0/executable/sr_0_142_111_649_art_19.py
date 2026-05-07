"""SR 0.142.111.649 Art. 19

Generated from: ch/0/de/0.142.111.649.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# No need for any variable in the OpenFisca implementation, as this article specifies a treaty change procedure rather than any specific calculation or parameter.
