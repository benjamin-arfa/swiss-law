"""SR 654.1 Art. 23 - Competence (suspension et denonciation)

Generated from: ch/654/de/654.1.md

The EFD may only act with Federal Council authorisation to suspend
or terminate CbC exchange with a partner state or to terminate the
agreement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 23 defines the competence of the EFD (with Federal Council
# authorisation) to suspend or terminate agreements. This is a purely
# institutional/procedural provision with no computable rule.
