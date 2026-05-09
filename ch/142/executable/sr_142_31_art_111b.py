"""SR 142.31 Art. 111b - Reexamen (Reconsideration)

Generated from: ch/142/fr/142.31.md

Reconsideration of asylum decisions:
- Request must be filed in writing with SEM within 30 days
  of discovering the grounds for reconsideration
- Must be duly motivated
- No preparatory phase
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lasi_jours_depuis_decouverte_motif(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours depuis la decouverte du motif de reexamen"
    reference = "SR 142.31 Art. 111b al. 1"


class lasi_demande_reexamen_dans_delai(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La demande de reexamen a ete deposee dans le delai de 30 jours"
    reference = "SR 142.31 Art. 111b al. 1"

    def formula(person, period, parameters):
        jours = person('lasi_jours_depuis_decouverte_motif', period)
        return jours <= 30
