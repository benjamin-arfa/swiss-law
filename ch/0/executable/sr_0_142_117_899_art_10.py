"""SR 0.142.117.899 Art. 10

Generated from: ch/0/de/0.142.117.899.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class spatial_scope(Variable):
    value_type = str
    entity = Person
    definition_period = MONTH
    label = "Spatial scope of application (Art. 10)",

    def formula(person, period, parameters):
        return "CH"
