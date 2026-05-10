"""SR 0.106 Art. 9

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class country_objects_to_visit(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Whether a state has objected to a visit (Art. 9 SR 0.106)"

    def formula(country, period, parameters):
        national_defense = parameters(period).international_cooperation.objected_visit.reasons.national_defense
        public_security = parameters(period).international_cooperation.objected_visit.reasons.public_security
        prison_disturbances = parameters(period).international_cooperation.objected_visit.reasons.prison_disturbances
        health_concerns = parameters(period).international_cooperation.objected_visit.reasons.health_concerns
        urgent_investigation = parameters(period).international_cooperation.objected_visit.reasons.urgent_investigation

        reasons = any([
            national_defense,
            public_security,
            prison_disturbances,
            health_concerns,
            urgent_investigation
        ])

        return reasons
