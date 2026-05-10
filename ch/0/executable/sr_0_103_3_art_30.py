"""SR 0.103.3 Art. 30

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class urgent_application_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Eligibility for submitting an urgent application (IAC Art. 30)"

    def formula(person, period, parameters):
        is_not_official = person('not_official_person', period)
        no_abuse_of_rights = person('no_abuse_of_rights', period)
        correctly_submitted = person('correctly_submitted_application', period)
        is_compliant_IAC = person('is_compliant_IAC', period)
        no_duplicate_case = person('no_duplicate_case', period)

        return is_not_official & no_abuse_of_rights & correctly_submitted & is_compliant_IAC & no_duplicate_case
