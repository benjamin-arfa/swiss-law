"""SR 0.142.116.909 Art. 8

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class transfer_request(Variable):
    value_type = bool
    entity = Person, Country
    label = "Asylum transfer request under Art. 8 SR 0.142.116.909"

    def formula(person, period, parameters, countries):
        application = person("transfer_applicaton", period)
        return application

class transfer_request_status(Variable):
    value_type = str
    entity = Country
    label = "Status of asylum transfer request under Art. 8 SR 0.142.116.909"

    def formula(countries, period, parameters):
        sender_country = countries.by_key("CHE")  # Switzerland, assume this as sender
        receiver_location = parameters(period).asylum_transfer_countries
        if countries.in_(receiver_location):
            return "Authorized"
        else:
            return "Rejected"

class countries(EntitySet):
    label = "Countries participating in the transfer of asylum seekers under Art. 8 SR 0.142.116.909"
    countries:
        CHE: Switzerland
        ...  # more countries
