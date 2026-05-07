"""SR 0.131.11 Art. 11

Generated from: ch/0/de/0.131.11.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import EU_Country, Person


class protocol_entry_into_force(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Protocol entry into force (Art. 11 SR 0.131.11)"


    def formula(person, period, parameters):
        num_ratifying_countries = person('num_eu_countries_ratified', period)
        threshold = parameters(period).protocol_threshold


        return (num_ratifying_countries >= threshold)
