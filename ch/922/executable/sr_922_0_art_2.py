"""SR 922.0 Art. 2

Generated from: ch/922/de/922.0.md

Art. 2: Geltungsbereich - Scope of the Hunting Act:
Applies to the following wild animals in Switzerland:
a. Birds
b. Carnivores (Raubtiere)
c. Even-toed ungulates (Paarhufer)
d. Lagomorphs (Hasenartige)
e. Beaver, marmot, and squirrel
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
import numpy as np


class jsg_tier_kategorie(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Tierkategorie nach JSG Art. 2 (1=Vögel, 2=Raubtiere, 3=Paarhufer, 4=Hasenartige, 5=Biber/Murmeltier/Eichhörnchen, 0=nicht erfasst)"
    reference = "SR 922.0 Art. 2"


class jsg_tier_im_geltungsbereich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Tier fällt in den Geltungsbereich des JSG"
    reference = "SR 922.0 Art. 2"

    def formula(person, period, parameters):
        kategorie = person('jsg_tier_kategorie', period)
        # Categories 1-5 are covered by the act
        return (kategorie >= 1) * (kategorie <= 5)
