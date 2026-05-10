"""SR 0.142.116.727 Art. 4

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class youth_work_contract_duration(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Duration of youth work contract (Art. 4 of the SR 0.142.116.727)"

    def formula(person, period, parameters):
        contract_start_date = person("youth_work_contract_start_date", period)
        contract_end_date = person("youth_work_contract_end_date", period)

        return (contract_end_date - contract_start_date).days // 30.44  # Convert to months

class youth_work_contract_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligibility for youth work contract (Art. 4 of the SR 0.142.116.727)"

    def formula(person, period, parameters):
        insurance_coverage = person("insurance_coverage_for_foreign_work", period)
        employment_conditions = person("employment_conditions_compliance", period)
        host_country_labor_regulations = parameters(period).social_security.youth_work_contract.host_labor_regulations
        return insurance_coverage & employment_conditions & host_country_labor_regulations
