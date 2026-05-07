"""SR 0.103.1 Art. 12

Generated from: ch/0/de/0.103.1.md
"""

# Define the healthcare outcome variable
from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class healthy_standard_outcome(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Attainable highest standard of health (Art. 12 of the European Convention on Human Rights)"

    def formula(person, period, parameters):
        raise NotImplementedError(
            "The definition of this variable should be specific to the region/policy under consideration, "
            "as the available information does not provide enough data to calculate the outcome directly."
        )
