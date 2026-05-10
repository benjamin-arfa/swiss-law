"""SR 0.142.117.121 Art. 11

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class change_of_affiliation_form_submitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = 'Change of affiliation form submitted (Art. 11 SR: 0.142.117.121)'

    def formula(person, period, parameters):
        submission_medium = person("submission_medium", period)
        electronic_medium = ["fax", "email", "secure_email"]
        return submission_medium != "none" or submission_medium in electronic_medium
