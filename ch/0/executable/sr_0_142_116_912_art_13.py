"""SR 0.142.116.912 Art. 13

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_agreement_suspension(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Suspension of the AHV agreement (Art. 13 SR 0.142.116.912)"

    def formula(countries, period, parameters):
        suspends = countries("suspends_ahv_agreement", period)
        notifies = countries("notifies_ahv_agreement_suspension", period)
        return (suspends | notifies) == 1
