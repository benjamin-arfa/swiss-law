"""SR 0.142.115.652.1 Art. 6

Generated from: ch/0/de/0.142.115.652.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class visa_fee_exempt(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Exemption from visa fee for Moldovan citizens (Art. 6 SR 0.142.115.652.1)"

    def formula(person, period, parameters):
        country_of_origin = person("country_of_origin", period)
        exempt_category = person("exempt_category", period)
        residency_status = person("residency_status", period)

        is_moldovan = country_of_origin == "MD"
        exemption_conditions = parameters(period).visa_fee_exemption.conditions
        is_exempt = any(condition(person, period, parameters) or exemption_conditions[condition.name] for condition in exemption_conditions)

        return is_moldovan & is_exempt
