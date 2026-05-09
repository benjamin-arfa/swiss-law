"""SR 0.672.916.311 Art. 14 - Entry into force and denunciation

Art. 14:
- Par. 1: Arrangement enters into force 60 days after signature.
- Par. 2: Either party may denounce with 6 months' notice before end
  of calendar year; takes effect at year-end.

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class arrangement_ch_at_en_vigueur(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "CH-AT tax relief arrangement is in force (Art. 14 par. 1)"
    default_value = True


class delai_entree_vigueur_jours(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Entry into force: 60 days after signature (Art. 14 par. 1)"
    default_value = 60


class delai_denonciation_mois(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Denunciation notice period: at least 6 months before year-end (Art. 14 par. 2)"
    default_value = 6
