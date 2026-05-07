"""SR 744.211 Art. 20

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_211_art_20_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.211 Art. 20 - Aufgehoben (repealed since 1977-01-01)"
    reference = "SR 744.211 Art. 20"

    def formula(person, period, parameters):
        # Article repealed by Art. 153 lit. m of the ordinance of 27 Oct. 1976
        # on the admission of persons and vehicles to road traffic, with effect from 1 Jan. 1977
        return period.start.date.year < 1977
