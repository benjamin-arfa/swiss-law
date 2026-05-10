"""SR 0.142.116.147 Art. 5

Generated from: ch/0/de/0.142.116.147.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class employment_contract_duration(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Duration of employment contract according to Art. 5 SR 0.142.116.147"

    def formula(person, period, parameters):
        start_date = person("employment_start_date", period)
        contract_start = start_date
        if start_date < parameters(period).social_security.unemployment.contract_extension_threshold:
            return "1 year"
        else:
            return "18 months"
