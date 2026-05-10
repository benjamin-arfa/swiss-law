"""SR 0.142.116.919 Art. 3

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class laissez_passer_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Eligibility for issuance of laissez-passer (Art. 3 SR 0.142.116.919)"

    def formula(person, period, parameters):
        nationality_verified = parameters(period).government.nationality_verified
        if nationality_verified:
            return True
        else:
            interview_held = parameters(period).government.interview_held
            if interview_held:
                return True
            else:
                return False

    def formula_rules(period, parameters):
        nationality_verified = (
            (parameters(period).government.laissez_passer_application_date
             >= (period.date - timedelta(days=3))) &
            (parameters(period).government.nationality_verified == True)
        )
        interview_held = (
            (parameters(period).government.laissez_passer_application_date
             >= (period.date - timedelta(days=6))) &
            (parameters(period).government.interview_held == True)
        )
        return nationality_verified | interview_held


class laissez_passer_issued(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Laissez-passer issued (Art. 3 SR 0.142.116.919)"

    def formula(person, period, parameters):
        nationality_confirmed = parameters(period).government.nationality_confirmed
        return nationality_confirmed
