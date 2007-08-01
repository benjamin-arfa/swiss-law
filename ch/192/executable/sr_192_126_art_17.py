"""SR 192.126 Art. 17

Generated from: ch/192/de/192.126.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 17 lists documents to submit for abroad-hired employees. Procedural.
