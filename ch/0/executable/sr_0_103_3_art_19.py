"""SR 0.103.3 Art. 19

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class missing_person_data_usage(Variable):
    value_type = bool
    entity = None
    definition_period = YEAR
    label = "Missing person data usage for search purposes (Art. 19 SR 0.103.3)"

    def formula(*, period, parameters):
        data_usage = parameters(period).social_securitydata_usage.missing_person_search
        rights_protection = parameters(period).social_securitydata_usage.dignity_protection_threshold

        return data_usage / rights_protection
