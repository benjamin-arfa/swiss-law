"""SR 0.103.2 Art. 44

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *

class adheres_to_human_rights_procedures(Variable):
    value_type = bool
    entity = World  # This variable affects all entities across the World tax unit
    definition_period = YEAR
    label = "Adheres to human rights procedures (Art. 44 SR 0.103.2)"

    def formula-world(world, period, parameters):
        return True  # Always True, as it's a procedural aspect, not calculable
