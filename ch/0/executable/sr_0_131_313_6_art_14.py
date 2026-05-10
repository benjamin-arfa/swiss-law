"""SR 0.131.313.6 Art. 14

Generated from: ch/0/de/0.131.313.6.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transborder_radio_frequencies(Variable):
    value_type = set
    entity = Governance
    definition_period = YEAR
    label = "Set of frequencies between phone administrations of CH and DE for transborder radio communications (Art. 14 SR 0.131.313.6)"

    def formula(governance, period, parameters):
        competent_authorities = {
            'CH': parameters(period).intergovernmental.communications.ch_competent_authority,
            'DE': parameters(period).intergovernmental.communications.de_competent_authority
        }
        return set(competent_authority.get_frequencies(parameters(period)) for competent_authority in competent_authorities.values())
