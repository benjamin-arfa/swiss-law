"""SR 196.1 Art. 18

Generated from: ch/196/de/196.1.md

Verfahren: Die eingezogenen Vermoegenswerte werden ueber Programme von
oeffentlichem Interesse ruckerstattet.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 18 regulates the restitution procedure.
# Procedural provision, no computable rule.
