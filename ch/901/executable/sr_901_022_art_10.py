"""SR 901.022 Art. 10

Generated from: ch/901/fr/901.022.md

Art. 10: Debut et duree de l'allegement fiscal.

Abs. 1: L'allegement fiscal de la Confederation est accorde pour la duree
de l'allegement octroye par le canton au plus, mais pour 10 annees civiles
au maximum.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rpol_duree_allegement_canton(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree de l'allegement fiscal cantonal (annees)"
    reference = "SR 901.022 Art. 10 al. 1"


class rpol_duree_allegement_federal(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree effective de l'allegement fiscal federal (annees)"
    reference = "SR 901.022 Art. 10 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        duree_canton = person('rpol_duree_allegement_canton', period)
        duree_max = p.sr_901_022.art_10.duree_max_allegement
        return min_(duree_canton, duree_max)
