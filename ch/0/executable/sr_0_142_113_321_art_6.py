"""SR 0.142.113.321 Art. 6

Generated from: ch/0/de/0.142.113.321.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person

class gross_benefits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gross benefits (Art. 6 SR 0.142.113.321)"

    def formula(person, period, parameters):
        # Assume benefits are added to gross_benefits variable
        return person("gross_benefits", period)
