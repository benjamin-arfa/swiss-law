"""SR 0.103.1 Art. 12

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Define the healthcare outcome variable




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
