"""SR 211.111.1 Art. 8

Generated from: ch/211/de/211.111.1.md

Zustimmung der Erwachsenenschutzbehoerde: Die Behoerde prueft auf Antrag,
ob die Voraussetzungen der Sterilisation erfuellt sind.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 8 regulates the procedure for the adult protection authority's consent.
# Procedural provision (hearing requirements, expert opinions), no computable rule.
