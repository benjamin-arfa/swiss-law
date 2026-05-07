"""SR 0.192.030 Art. 30

Generated from: ch/0/de/0.192.030.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import InstitutionalEntity


class required_voting_majority(Variable):
    value_type = float
    entity = InstitutionalEntity
    definition_period = YEAR
    label = "Required majority for Board voting decisions (Article 30 SR 0.192.030)"

    def formula(entity, period, parameters):
        required_majority = parameters(period).institutional_settings.beratende_versammlung.vote_majority
        return required_majority
