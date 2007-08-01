"""SR 172.061.1 Art. 21

Generated from: ch/172/de/172.061.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Legislation / publication regulation. Procedural, no computable rule.
