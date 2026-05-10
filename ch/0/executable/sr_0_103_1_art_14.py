"""SR 0.103.1 Art. 14

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries.entities import Country


class free_primary_education_commitment(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Country commitment to free primary education (Art. 14 of Social Security Convention)" 

    def formula(countries, period, parameters):
        return countries("free_primary_education_commitment", period)
