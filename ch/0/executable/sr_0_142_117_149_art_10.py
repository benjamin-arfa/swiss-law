"""SR 0.142.117.149 Art. 10

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class governmental_contact(Variable):
    value_type = str
    entity = Country
    definition_period = DAY
    label = "Government contact information (Article 10 of the Agreement)"

    def formula(country, period, parameters):
        country_identifier = country('iso_code', period)
        country_data_source = parameters(period).data_sources.government_contacts

        institution_data = country_data_source.get(country_identifier)
        try:
            return institution_data['mail']['institution'] + institution_data['mail']['mailbox']
        except KeyError:
            return f"No governmental contact information found for {country_identifier}"
