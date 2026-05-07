"""SR 0.142.116.909 Art. 13

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class escort_identification_documents(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ability of treaty partner state escorts to prove identity and assignment"

    def formula(person, period, parameters):
        transit_permit = person("transit_permit", period)
        valid_id = person("valid_identity_document", period)
        valid_assignment_proof = person("valid_assignment_proof", period)

        return (transit_permit and valid_id and valid_assignment_proof)
