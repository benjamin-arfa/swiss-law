"""SR 446.11 Art. 29

Generated from: ch/446/de/446.11.md

Skipped: Prozedural - Vollzug durch das BSV.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Vollzugsbestimmung - keine berechenbare Regel
