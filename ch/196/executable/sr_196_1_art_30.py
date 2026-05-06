"""SR 196.1 Art. 30

Generated from: ch/196/de/196.1.md

Vollzug: Der Bundesrat erlaesst die Ausfuehrungsbestimmungen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 30 is an implementation delegation clause.
# Procedural provision, no computable rule.
