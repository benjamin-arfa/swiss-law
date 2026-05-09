"""SR 654.1 Art. 28 - Competence d'approbation

Generated from: ch/654/de/654.1.md

The Federal Council is competent for adding a state or territory
to the list under Section 8(1)(e) of the ALBA Agreement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 28 is a competence attribution provision.
# No computable rule can be derived.
