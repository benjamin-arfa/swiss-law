"""SR 116 Art. 3 - Vorbehalt kantonalen Rechts (Reservation of Cantonal Law)

Generated from: ch/de/116.md
Cantonal provisions on Sunday rest and opening hours for retail,
hospitality, and entertainment businesses are reserved.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)

# Skipped: Art. 3 is a reservation clause deferring to cantonal law.
# Cantonal Sunday rest and opening hour rules take precedence.
