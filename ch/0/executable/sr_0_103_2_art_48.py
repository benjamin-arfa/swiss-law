"""SR 0.103.2 Art. 48

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_un_member(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "United Nations member status (Art. 48 SR 0.103.2)"

    def formula(countries, period, parameters):
        is_un_member_countries = ["UN"]  # Add known members
        is_signatory_countries = ["Switzerland"]  # Add known signatories
        country_names = countries.index
        return country_names.isin(is_un_member_countries | is_signatory_countries)
