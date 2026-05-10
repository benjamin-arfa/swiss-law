"""SR 0.142.115.989 Art. 16

Generated from: ch/0/de/0.142.115.989.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class safe_return_transport_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Eligibility for direct onward return transport to Switzerland (Art. 16 SR 0.142.115.989)"

    def formula(person, period, parameters):
        nationality = person("nationality", period)
        religion = person("religion", period)
        social_group = person("social_group", period)
        political_beliefs = person("political_beliefs", period)
        
        # hardcoded conditions for now
        risks = [
            nationality == "T", # T is just an example for treshold case
            religion == "M", # M is just an example for treshold case
            social_group == "M", # M is just an example for treshold case
            political_beliefs == "M" # M is just an example for treshold case
        ]
        
        has_unsafe_characteristic = any(risks)
        
        has_conviction_risk = params("has_crime_record", person, period)
        
        return not (has_unsafe_characteristic | has_conviction_risk)
