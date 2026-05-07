"""SR 0.142.117.121 Art. 11

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class change_of_affiliation_form_submitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = 'Change of affiliation form submitted (Art. 11 SR: 0.142.117.121)'

    def formula(person, period, parameters):
        submission_medium = person("submission_medium", period)
        electronic_medium = ["fax", "email", "secure_email"]
        return submission_medium != "none" or submission_medium in electronic_medium
