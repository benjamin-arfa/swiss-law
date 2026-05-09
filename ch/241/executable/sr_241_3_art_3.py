"""SR 241.3 Art. 3

Generated from: ch/241/de/241.3.md

Aufhebung bisherigen Rechts: The ordinance of 17 February 1993 on the
right of action of the Confederation under the Federal Act against Unfair
Competition is repealed.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# No computable logic - this article repeals a prior ordinance.
