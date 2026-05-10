"""SR 0.142.116.659 Art. 15

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from datetime import date


class transit_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for transit through Switzerland/Russia (Art. 15 Agreement)"

    def formula(person, period, parameters):
        nationality = person("nationality", period)
        nationality_exclusions = parameters(period).migration.agreements.russia_exclusions
        countries_exclusions = parameters(period).migration.agreements.russia_countries_exclusions

        non_refoulement = ~nationals_nationality_exclusions(nationality, nationality_exclusions) 
        mutual_consent = parameters(period).migration.transit_consent[nationality]
        ongoing_legal_proceedings = person("ongoing_legal_proceedings", period)
        public_interest_reasons = person("public_interest_reasons", period)

        public_health = person("public_health_risks", period)
        internal_security = person("internal_security_risks", period)
        public_order = person("public_order_risks", period)

        readmission_provisions_met = (person("readmission_provisions_met", period))
        return non_refoulement & mutual_consent & (~ongoing_legal_proceedings) & (~public_health) & \
             (~internal_security) & (~public_order) & readmission_provisions_met
