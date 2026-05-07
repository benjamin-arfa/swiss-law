"""SR 725.11 Art. 1

Generated from: ch/725/de/725.11.md

Nationalstrassen: Die wichtigsten Strassenverbindungen von
gesamtschweizerischer Bedeutung werden von der Bundesversammlung
zu Nationalstrassen erklaert. Klassen 1, 2 und 3.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_nationalstrasse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse als Nationalstrasse erklaert wurde"
    reference = "SR 725.11 Art. 1 Abs. 1"


class nationalstrassen_klasse(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Klasse der Nationalstrasse (1, 2 oder 3)"
    reference = "SR 725.11 Art. 1 Abs. 2"
