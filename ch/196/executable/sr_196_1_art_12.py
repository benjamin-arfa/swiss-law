"""SR 196.1 Art. 12

Generated from: ch/196/de/196.1.md

Technische Unterstuetzung: Das EDA und das BJ koennen dem Herkunftsstaat
technische Unterstuetzung leisten.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 12 regulates technical assistance measures.
# Procedural/organizational provision, no computable rule.
