"""SR 0.106 Art. 2

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.entities import (
    superEntity, Building,
    LocationBuilding, LocationZone,
    Person, Household),
from openfisca_core.period import MONTH

class visitation_allowed(Variable):
    value_type = bool
    default_entity = LocationBuilding
    default_period = DAY
    label = "Visitation allowed at designated locations"
    definition_period = MONTH

    def formula(loc, period, parameters):
        control_entities = loc('government_control_entities', period)
        government_entities = control_entities('type', period)
        return superEntity(loc, period).has_any_entity(government_entities)
