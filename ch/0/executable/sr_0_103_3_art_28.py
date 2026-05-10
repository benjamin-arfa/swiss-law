"""SR 0.103.3 Art. 28

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_cooperation_effort(Variable):
    value_type = bool
    entity = Committee
    definition_period = YEAR
    label = "Effort in cooperating with relevant entities for enforced disappearance protection (Art. 28 SR 0.103.3)"

    def formula(committee, period, parameters):
        works_with_unOrgans = True  # e.g., UN working groups, specialized committees
        works_with_treaty_bodies = True  # e.g., HRC, CEDAW, etc.
        works_with_regional_organizations = True  # e.g., COE, AU, etc.

        return (works_with_unOrgans & works_with_treaty_bodies & works_with_regional_organizations)
