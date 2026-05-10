"""SR 0.142.116.657 Art. 8

Generated from: ch/0/de/0.142.116.657.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stagiaire_quota(Variable):
    value_type = int
    entity = Institution
    definition_period = YEAR
    label = "Stagiaire quota for the following year (Art. 8 SR 0.142.116.657)"

    def formula(institution, period, parameters):
        quota_parameters = parameters(period)
        minimum_quota = quota_parameters.contracting_agreements.stagiaire_quota.minimum
        allocation = quota_parameters.contracting_agreements.stagiaire_quota.allocation
        return max(minimum_quota, allocation)

class allocated_stagiaires(Variable):
    value_type = int
    entity = Institution
    definition_period = YEAR
    label = "Number of stagiaires allocated to this institution"

    def formula(institution, period, parameters):
        quota = institution("stagiaire_quota", period)
        return min(quota, institution("requested_stagiaires", period))
