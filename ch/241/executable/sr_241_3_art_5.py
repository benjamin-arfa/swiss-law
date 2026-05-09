"""SR 241.3 Art. 5

Generated from: ch/241/de/241.3.md

Inkrafttreten: This ordinance enters into force on 1 April 2012.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# No computable logic - this article only sets the entry-into-force date.
