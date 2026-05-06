"""SR 196.1 Art. 9

Generated from: ch/196/de/196.1.md

Freigabe gesperrter Vermoegenswerte: Das EDA kann ausnahmsweise die Freigabe
einzelner gesperrter Vermoegenswerte bewilligen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 9 grants discretionary power to the EDA for exceptional release.
# No computable rule (discretionary decision).
