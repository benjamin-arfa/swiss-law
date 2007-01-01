"""SR 429.1 Art. 9

Generated from: ch/429/de/429.1.md

Skipped: Referendum and entry-into-force provision.
Art. 9 states the law is subject to optional referendum and sets
entry into force date (1 April 2000). No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 9 - Referendum und Inkrafttreten
# Fakultatives Referendum, Inkrafttreten 1. April 2000. Keine berechenbare Regel.
