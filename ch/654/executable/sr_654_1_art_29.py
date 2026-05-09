"""SR 654.1 Art. 29 - Modification de l'accord applicable

Generated from: ch/654/de/654.1.md

The Federal Assembly approves amendments to the applicable agreement
by simple federal decree, subject to optional referendum if conditions
under Art. 141(1)(d)(3) BV are met.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 29 is a procedural provision on treaty amendment approval.
# No computable rule can be derived.
