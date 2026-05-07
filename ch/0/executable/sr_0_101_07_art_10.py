"""SR 0.101.07 Art. 10

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

class Inkrafttretensdatum(Variable):
    value_type = int
    label = "Inkrafttretensdatum von Protokollen"
    entity = Person
    definition_period = D
    reference = "Artikel 10 SR 0.101.07"
