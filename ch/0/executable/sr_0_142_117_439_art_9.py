"""SR 0.142.117.439 Art. 9

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca.switzerland.entities import Person


class risk_of_transit_denial(Variable):
    value_type = bool
    entity = Person
    definition_period = ALWAYS
    label = "Risk of transit denial by Swiss authorities (Art. 9 SR 0.142.117.439)"

    def formula(person, period, parameters):
        return (  # (a)
                person("risk_of_torture_or_punishment", period)
            ) | (
                (  # (b)
                    person("risk_of_prosecution_in_destination_country", period)
                    | person("risk_of_conviction_in_destination_country", period)
                )
            ) | (
                (  # (c)
                    person("public_health_concerns", period)
                    | person("internal_security_concerns", period)
                    | person("public_order_concerns", period)
                    | sum(person("other_national_interests_concerns", period))
                )
            )
