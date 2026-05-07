"""SR 0.142.117.542 Art. 8

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class international_treaties_exception(Variable):
    value_type = bool
    entity = Country
    definition_class = 'Country'
    label = "International treaties exception (SR 0.142.117.542 Art. 8)"

    def default_value(Country):
        # By default, international treaties are not affected by the agreement
        return True
