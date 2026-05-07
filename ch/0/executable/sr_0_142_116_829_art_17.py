"""SR 0.142.116.829 Art. 17

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class exemption_due_to_international_agreement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemption from AHV contribution due to international agreement"

    def formula(person, period, parameters):
        nationality = person("nationality", period)
        return (nationality == "Serbia") | (nationality == "refugee")
