"""SR 0.103.2 Art. 5

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Unfortunately, Art. 5 of the ECHR (in its SR 0.103.2 version) is focused on the interpretation of a human rights treaty, and does not provide concrete mathematical or factual data to be input into an OpenFisca variable.

Thus, no OpenFisca variable is generated from this Article.
