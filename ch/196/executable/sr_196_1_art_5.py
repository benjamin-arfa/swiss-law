"""SR 196.1 Art. 5

Generated from: ch/196/de/196.1.md

Anpassung und Veroeffentlichung der Listen: Das EDA kann die Namensliste
anpassen (streichen oder hinzufuegen).
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 5 regulates administrative procedures for list management.
# No computable rule can be derived.
