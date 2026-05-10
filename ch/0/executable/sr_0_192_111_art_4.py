"""SR 0.192.111 Art. 4

Generated from: ch/0/de/0.192.111.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ngo_exclusion_exception(Variable):
    value_type = bool
    entity = Ngo
    definition_period = YEAR
    label = "NGO exclusion exception (Art. 4 SR 0.192.111)"

    def formula(ngo, period, parameters):
        purpose_conflict = ngo("ngo_purpose", period)
        activities_conflict = ngo("ngo_activities", period)
        national_security_conflict = ngo("national_security_conflict", period)
        societal_order_conflict = ngo("societal_order_conflict", period)
        health_morality_conflict = ngo("health_morality_conflict", period)
        public_relation_conflict = ngo("public_relation_conflict", period)

        return (
            purpose_conflict | activities_conflict | national_security_conflict |
            societal_order_conflict | health_morality_conflict | public_relation_conflict
        )
