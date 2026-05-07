"""SR 0.142.117.587 Art. 8

Generated from: ch/0/de/0.142.117.587.md
"""

Because Art. 8 deals with procedural aspects rather than monetary values, a direct OpenFisca implementation isn't applicable. However, this does not preclude the creation of a variable that might reflect the impact of these free procedures:

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class free_procedure_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Benefit of free administrative procedures for young professionals (Art. 8 SR 0.142.117.587)"

    def formula(person, period, parameters):
        is_young_professional = parameters(period).eligibility.young_professional
        return is_young_professional
