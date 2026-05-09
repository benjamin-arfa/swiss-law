"""SR 292.741.1 Art. 3

Generated from: ch/292/de/292.741.1.md

Inkrafttreten: This ordinance enters into force on 1 October 1954.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# No computable logic - this article only sets the entry-into-force date.
