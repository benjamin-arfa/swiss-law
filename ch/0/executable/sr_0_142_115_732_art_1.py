"""SR 0.142.115.732 Art. 1

Generated from: ch/0/de/0.142.115.732.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries.entities import Country, Person


class montenegro_treaty_simplification(Variable):
    value_type = bool
    entity = Person
    definition_period = PERTURBATION
    label = "Simplification of visa issuance for Montenegrin citizens (SR 0.142.115.732, Art. 1)"

    def formula(person, period, parameters):
        country = person("country_of_residence", period)
        purpose = "simplified_treaty_process"
        return country == Country.Montenegro and purpose == "simplified_treaty_process"
