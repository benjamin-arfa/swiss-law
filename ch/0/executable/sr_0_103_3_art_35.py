"""SR 0.103.3 Art. 35

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_jurisdiction(Variable):
    value_type = bool
    entity = Country
    label = "Committee jurisdiction over disappearance cases (Art. 35 SR 0.103.3)"

    def formula(country, period, parameters):
        convention_entry_into_force = parameters(period).convention.entry_into_force
        country_became_party = parameters(period).countries[country.label].became_party_on

        return country_became_party.after(convention_entry_into_force)
