"""SR 161.1 Art. 3

Generated from: ch/161/de/161.1.md

Politischer Wohnsitz: Die Stimmabgabe erfolgt am politischen Wohnsitz
(Gemeinde, wo die Person wohnt und angemeldet ist).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_fahrende_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Fahrende/r gilt"
    reference = "SR 161.1 Art. 3 Abs. 1"


class wohngemeinde(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Gemeinde, wo die Person wohnt und angemeldet ist"
    reference = "SR 161.1 Art. 3 Abs. 1"


class heimatgemeinde(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Heimatgemeinde der Person"
    reference = "SR 161.1 Art. 3 Abs. 1"

# Skipped formula: politischer_wohnsitz is string-based, would need to return
# wohngemeinde or heimatgemeinde based on ist_fahrende_person.
