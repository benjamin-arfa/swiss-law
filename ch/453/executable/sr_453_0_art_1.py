"""SR 453.0 Art. 1

Generated from: ch/453/de/453.0.md

Skipped: Rein deklarativ - Geltungsbereich der VCITES (Tiere/Pflanzen geschuetzter Arten).
Aufzaehlung ohne berechenbare Logik.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Rein deklarativ - Geltungsbereich
