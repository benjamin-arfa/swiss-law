"""SR 0.142.116.822 Art. 2

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class republic_of_serbia_visa_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Visa exemption as a Republic of Serbia citizen (Art. 2 SR 0.142.116.822)"

    def formula(person, period, parameters):
        is_swiss_citizen = person("is_swiss_citizen", period)
        is_serbian_citizen = person("country_of_birth") == "Republic of Serbia"
        visa_exempt_countries = parameters(period).border_controls.visa_exemption.countries
        country = person("country_of_birth")

        return (not is_swiss_citizen and not is_serbian_citizen and country != "Switzerland") & (country in visa_exempt_countries)
