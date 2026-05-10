"""SR 0.142.116.727 Art. 6

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class in_atypical_temporary_work_arrangement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Employed in atypical temporary work arrangement (Art. 6 para. 2 AHVG)"

    def formula(person, period, parameters):
        employment_contract_with_host_country = person("employment_contract_with_host_country", period)
        is_young_employed_permanent = person("is_young_employed_permanent", period)
        return employment_contract_with_host_country != "yes" | is_young_employed_permanent


class is_young_employed_permanent(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Permanent employment with a youth below 26 (prohibited under Art. 6 para. 1 AHVG)"

    def formula(person, period, parameters):
       age = (period.date - person("birth_date", period)).days / 365.25
       permanent_employment = person("permanent_employment", period)
       return (age < 26) & permanent_employment
