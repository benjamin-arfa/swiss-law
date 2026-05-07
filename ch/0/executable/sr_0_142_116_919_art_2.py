"""SR 0.142.116.919 Art. 2

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.entities.generic import Person


class country_responsibility_take_in_person(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Country responsibility to take in a person under SR 0.142.116.919 Art. 2"

    def formula(person, period, parameters):
        return (person("has_documents_accepted_proof", period) |
                person("makes_credible_citizenship_claim", period))
