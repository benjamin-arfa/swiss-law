"""SR 0.105 Art. 5

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class cantonal_jurisdiction(Variable):
    value_type = bool
    entity = Country
    label = "Conditions under which CH exercises cantonal jurisdiction (Art. 5 SR 0.105)"

    def formula(country, period, parameters):
        crime_commitment_location_in_ch = country("crime_commitment_location_in_ch", period)
        offender_is_swiss_citizen = country("offender_is_swiss_citizen", period)
        victim_is_swiss_citizen = country("victim_is_swiss_citizen", period)
        offender_is_present_in_ch = country("offender_is_present_in_ch", period)

        return (crime_commitment_location_in_ch | 
                (offender_is_swiss_citizen | 
                 victim_is_swiss_citizen | 
                 (not victim_is_swiss_citizen & country("can_exercise_jurisdiction_on_foreign_victims", period))) | 
                offender_is_present_in_ch)
