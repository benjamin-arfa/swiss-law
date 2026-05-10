"""SR 161.11 Art. 5

Generated from: ch/161/fr/161.11.md

Transmission of provisional results: cantonal central service transmits
electronically to federal service. Results must not be published before
voting day at 12:00.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class odp_resultats_provisoires_transmis_electroniquement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Les resultats provisoires sont transmis sous forme electronique"
    reference = "SR 161.11 Art. 5 al. 2"


class odp_heure_publication_resultats_provisoires(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Heure avant laquelle les resultats provisoires ne peuvent etre publies (12h)"
    reference = "SR 161.11 Art. 5 al. 4"

    def formula(person, period, parameters):
        return 12
