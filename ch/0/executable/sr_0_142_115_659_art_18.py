"""SR 0.142.115.659 Art. 18

Generated from: ch/0/de/0.142.115.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_requesting_party(Variable):
    value_type = bool
    entity = Institution  # Changed from Person to Institution
    definition_period = MONTH
    label = "Institution is requesting an expert consultation (Art. 18 SR 0.142.115.659)"

    def formula(institution, period, parameters):
        institution_id = institution.id
        other_contracting_party_id = parameters(period).international_agreements.sr_0_142_115_659.contracting_party2
        other_contracting_party_id_2 = parameters(period).international_agreements.sr_0_142_115_659.contracting_party1

        request_sent = institution.sent_expert_consultation_request
        request_from_other_party = request_sent.any(period) | institution.sent_expert_consultation_request.exists(period)
        
        return request_from_other_party
