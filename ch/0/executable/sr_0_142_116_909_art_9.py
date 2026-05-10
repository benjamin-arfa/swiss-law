"""SR 0.142.116.909 Art. 9

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# These variable declarations are specific to the legal article:
class foreign_national_transfer_procedure(Variable):
    definition_period = MONTH
    value_type = bool
    entity = Person
    label = "Procedure for escorting a foreign national during a transfer (Art. 9 SR 0.142.116.909)"

    def formula(person, period, parameters):
        transfer_occurring = person("is_foreign_national_transferring", period)
        return transfer_occurring

class police_escorting_procedure_followed(Variable):
    definition_period = MONTH
    value_type = bool
    entity = Person
    label = "Police escorting procedure followed for foreign national transfer (Art. 9 SR 0.142.116.909)"

    def formula(person, period, parameters):
        police_escorting_procedure = person("is_police_escorting_foreign_national", period)
        return police_escorting_provincecedure
