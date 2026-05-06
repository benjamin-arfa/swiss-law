"""SR 196.1 Art. 20

Generated from: ch/196/de/196.1.md

Gesuch um Streichung: Betroffene Personen koennen ein Gesuch um Streichung
ihres Namens an das EDA richten.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 20 regulates an administrative petition procedure.
# Procedural provision, no computable rule.
