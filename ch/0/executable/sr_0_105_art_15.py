"""SR 0.105 Art. 15

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *

class evidence_from_torture_allowed(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "Admissibility of statements obtained by torture (Art. 15 EU Anti-Torture Convention)"

    def formula(person, period, parameters):
        has_evidence_from_torture = False  # This variable would typically be linked to real-world data

        if has_evidence_from_torture:
            return True
        else:
            return False
