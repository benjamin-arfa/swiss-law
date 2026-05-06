"""SR 196.1 Art. 10

Generated from: ch/196/de/196.1.md

Guetliche Einigung: Der Bundesrat kann das EDA beauftragen, eine guetliche
Einigung zu suchen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 10 regulates amicable settlement procedures.
# Procedural provision, no computable rule.
