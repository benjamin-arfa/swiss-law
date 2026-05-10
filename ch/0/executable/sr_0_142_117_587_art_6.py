"""SR 0.142.117.587 Art. 6

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class employment_contract_rights(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Rights from employment contract (Art. 6 SR 0.142.117.587)"

    def formula(person, period, parameters):
        foreign_labor_law = parameters(period).foreigners.labour_law_rights
        young_professional_contract_rights = person("young_professional_contract_rights", period)
        return foreign_labor_law & young_professional_contract_rights

class customary_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Customary compensation according to region and profession (Art. 6 SR 0.142.117.587)"

    def formula(person, period, parameters):
        compensation_customary = person("compensation_customary", period)
        return compensation_customary

class employment_contract(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Employment contract between employer and employee (Art. 6 SR 0.142.117.587)"

    def formula(person, period, parameters):
        employment_agreement = person("employment_agreement", period)
        return employment_agreement
