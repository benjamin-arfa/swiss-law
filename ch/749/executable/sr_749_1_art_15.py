"""SR 749.1 Art. 15

Generated from: ch/749/fr/749.1.md

Art. 15: Cantonal consultation, publication, and public inspection:
- al. 1: Cantons have 3 months to respond (extendable).
- al. 2: Public inspection for 30 days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltsm_delai_avis_cantons_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Deadline for cantonal opinion in months"
    reference = "SR 749.1 Art. 15 al. 1"

    def formula(person, period, parameters):
        return parameters(period).sr_749_1.delai_avis_cantons_mois


class ltsm_duree_mise_enquete_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duration of public inspection in days"
    reference = "SR 749.1 Art. 15 al. 2"

    def formula(person, period, parameters):
        return parameters(period).sr_749_1.duree_mise_enquete_jours
