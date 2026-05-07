"""SR 0.142.116.702 Art. 8

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *

class international_treaties_binding(Variable):
    value_type = bool
    entity = None
    # Could apply to entity == None if this applies on a scenario level (Country, etc.)
    # definition_period = YEAR  # Would be necessary but entity == None.
    label = "Binding international treaties commitments (Art. 8 SR 0.142.116.702)"

    def formula():
        return True

# For each treaty, create parameters to store binding (True or False)
