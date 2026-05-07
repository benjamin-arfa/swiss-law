"""SR 0.142.116.822 Art. 13

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import Variable


class data_protection_lawReference(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Data protection law reference (SR 0.142.116.822 Art. 13)"

    def formula(person, period, parameters):
        return "SR 0.142.116.822 Art. 13"
