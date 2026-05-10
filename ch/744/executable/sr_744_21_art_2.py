"""SR 744.21 Art. 2

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class untersteht_gesetz_sr_744_21(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen untersteht dem Gesetz über Treibstoffzollbefreiung (SR 744.21)"
    reference = "SR 744.21 Art. 2"

    def formula(person, period, parameters):
        # To be set externally: whether the entity is a company subject to SR 744.21
        return person('untersteht_gesetz_sr_744_21', period)


class enteignungsrecht_sr_744_21(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung zum Enteignungsrecht gemäss BG vom 20. Juni 1930 über die Enteignung (SR 711)"
    reference = "SR 744.21 Art. 2"

    def formula(person, period, parameters):
        # Art. 2: Companies subject to SR 744.21 have the right of expropriation
        # pursuant to the Federal Act of 20 June 1930 on Expropriation (SR 711)
        untersteht = person('untersteht_gesetz_sr_744_21', period)
        return untersteht
