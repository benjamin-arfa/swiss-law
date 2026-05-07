"""SR 0.103.2 Art. 32

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class election_term_magnitude(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Election term magnitude (4 years)"

    def formula(person, period, parameters):
        return parameters(period).election_details.mandate_duration_long


class election_term_duration(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Election term duration (2 years)"

    def formula(person, period, parameters):
        return parameters(period).election_details.mandate_duration_short
