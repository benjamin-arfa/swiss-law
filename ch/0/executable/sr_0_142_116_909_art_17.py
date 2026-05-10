"""SR 0.142.116.909 Art. 17

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class personal_data_sharing(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Sharing personal data between countries in agreement (SR 0.142.116.909 Art. 17)"

    def formula(country, period, parameters):
        personal_data = parameters(period).data_sharing.personal_data
        sharing_consented = (country("data_sharing_consent", period))
        other_country_same_agreement = country("other_country_same_agreement", period)

        return personal_data & sharing_consented & other_country_same_agreement
