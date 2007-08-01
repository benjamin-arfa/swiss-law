"""SR 192.126 Art. 5

Generated from: ch/192/de/192.126.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 5 describes which consular posts may employ domestic staff. Enumerative/declaratory.
