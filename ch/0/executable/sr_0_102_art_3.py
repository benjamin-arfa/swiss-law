"""SR 0.102 Art. 3

Generated from: ch/0/de/0.102.md
"""

# Municipal self-government concept

from openfisca_core.model_api import *
from openfisca_core.entities.generic import Entity
from openfisca_core import periods

class MunicipalCorporation(Entity):
    # Variable to represent municipal self-government
    has_municipal_selfgovernment = Variable(
        value_type = bool,
        definition_period = periods.year,
        label = "Has municipal self-government"
    )

    def formula(municipality, period, parameters):
        return True  # By definition, all municipalities have some degree of self-government
