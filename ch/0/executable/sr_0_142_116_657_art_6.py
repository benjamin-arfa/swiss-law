"""SR 0.142.116.657 Art. 6

Generated from: ch/0/de/0.142.116.657.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stagiaire_work_contract_term(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Internship working contract term stipulations (Article 6 SR 0.142.116.657)"

    def formula(person, period, parameters):
        contract_agreement = person("labour_contract_agreement", period)
        min_wage_rate = parameters(period).labour.law.minimum_monthly_wage
        return max(contract_agreement, min_wage_rate)

class stagiaire_insurance_coverage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Internship insurance coverage (Article 6 SR 0.142.116.657)"

    def formula(person, period, parameters):
        contract_agreement = person("labour_contract_agreement", period)
        establishment = person("place_of_work", period)
        return contract_agreement and establishment.has("business_insurance")

class stagiaire_travel_coverage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Internship travel and accommodation coverage (Article 6 SR 0.142.116.657)"

    def formula(person, period, parameters):
        contract_agreement = person("labour_contract_agreement", period)
        return contract_agreement
