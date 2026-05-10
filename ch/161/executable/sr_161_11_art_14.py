"""SR 161.11 Art. 14

Generated from: ch/161/fr/161.11.md

Transmission of election records: government transmits to Federal Council
after appeal deadline expires. Election forms and ballots sent to
Federal Statistical Office within 10 days of appeal deadline.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class odp_delai_recours_expire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le delai de recours est expire"
    reference = "SR 161.11 Art. 14 al. 1"


class odp_delai_remise_bulletins_ofs_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour remettre les bulletins a l'OFS apres expiration du delai de recours (10 jours)"
    reference = "SR 161.11 Art. 14 al. 2"

    def formula(person, period, parameters):
        return 10
