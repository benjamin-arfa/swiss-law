"""SR 173.320.3 Art. 3

Generated from: ch/173/de/173.320.3.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 3 defines fee exemptions and reductions. Discretionary, no fixed formula.
