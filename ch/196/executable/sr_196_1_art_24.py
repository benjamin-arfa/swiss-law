"""SR 196.1 Art. 24

Generated from: ch/196/de/196.1.md

Berichterstattung: Das EDA uebermittelt jaehrlich einen Bericht an die
zustaendigen parlamentarischen Kommissionen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 24 imposes a reporting obligation.
# Procedural provision, no computable rule.
