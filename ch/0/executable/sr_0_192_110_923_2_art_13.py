"""SR 0.192.110.923.2 Art. 13

Generated from: ch/0/de/0.192.110.923.2.md
"""

from openfisca_core.model_api import *

# Consider the institution-specific exceptions
class epo_president_exceptions(Entities):
    def __init__(self, entities):
        super().__init__(entities)

    def exception_during_driving(self):
        return False  # Traffic infringement not applicable

    def exception_vehicle_related_damage(self):
        return False  # Damage by EPO president's owned vehicle not applicable

    def exception_immunity_revoked(self):
        return self.exception_during_driving() | self.exception_vehicle_related_damage()
