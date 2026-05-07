"""SR 513.12 Art. 1

Generated from: ch/513/de/513.12.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


# Skipped: Art. 1 is purely declarative (Gegenstand und Geltungsbereich).
# It defines the scope of the ordinance but contains no computable rule.
