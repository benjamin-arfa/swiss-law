"""SR 172.041.0 Art. 1

Generated from: ch/172/de/172.041.0.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 1: Verfahrenskosten der unterliegenden Partei
# Skipped: Art. 1 lists cost components (Spruchgebuehr, Barauslagen, Kanzleigebuehren). Enumerative.
