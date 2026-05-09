"""SR 901.022 Art. 23

Generated from: ch/901/fr/901.022.md

Art. 23: Dispositions transitoires pour les cautionnements.

Abs. 2: Les cautionnements octroyes avant l'entree en vigueur de l'ordonnance
du 28 novembre 2007 peuvent etre prolonges jusqu'a 8 ans au maximum.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class rpol_cautionnement_ancien_droit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Cautionnement octroye avant l'ordonnance du 28 novembre 2007"
    reference = "SR 901.022 Art. 23 al. 2"


class rpol_duree_prolongation_cautionnement(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree maximale de prolongation du cautionnement (annees)"
    reference = "SR 901.022 Art. 23 al. 2"

    def formula(person, period, parameters):
        p = parameters(period)
        ancien_droit = person('rpol_cautionnement_ancien_droit', period)
        duree_max = p.sr_901_022.art_23.prolongation_max_cautionnement
        return where(ancien_droit, duree_max, 0)
