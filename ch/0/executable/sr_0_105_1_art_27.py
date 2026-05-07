"""SR 0.105.1 Art. 27

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class protocol_entry_force(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Protocol entry into force (Art. 27 SR 0.105.1)"

    def formula(country, period, parameters):
        signed = country("protocol_signed", period)
        ratified = country("protocol_ratified", period)

        deposited_documents = country("protocol_deposited_documents", period)

        return (signed & ratified) & (~deposited_documents)
