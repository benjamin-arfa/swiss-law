"""SR 429.1 Art. 6

Generated from: ch/429/de/429.1.md

Skipped: Purely procedural article.
Art. 6 authorizes the Federal Council to delegate tasks to third parties by contract.
No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 6 - Aufgabenerfuellung durch Dritte
# Ermaechtigung zur Delegation von Aufgaben. Keine berechenbare Regel.
