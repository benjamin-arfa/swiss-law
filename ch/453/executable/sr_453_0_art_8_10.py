"""SR 453.0 Art. 8-10

Generated from: ch/453/de/453.0.md

Skipped: Art. 8 - Allgemeine Bewilligungsvoraussetzungen (Verweis auf CITES).
Art. 9 - Zusaetzliche Voraussetzungen Einfuhr (qualitativ).
Art. 10 - Zusaetzliche Voraussetzungen Ausfuhr/Wiederausfuhr (qualitativ).
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Qualitative Bewilligungsvoraussetzungen - nicht in Formeln ausdrueckbar
