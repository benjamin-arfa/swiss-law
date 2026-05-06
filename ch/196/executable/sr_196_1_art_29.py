"""SR 196.1 Art. 29

Generated from: ch/196/de/196.1.md

Vereinigung der Strafverfolgung.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 29 regulates consolidation of criminal proceedings.
# Procedural provision, no computable rule.
