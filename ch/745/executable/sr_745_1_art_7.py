"""SR 745.1 Art. 7

Generated from: ch/745/de/745.1.md

Personenbefoerderung von geringer Bedeutung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class benoetigt_kantonale_bewilligung_skilift(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Skilift oder Kleinseilbahn ohne Erschliessungsfunktion benoetigt kantonale Bewilligung"
    reference = "SR 745.1 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        # Art. 7 Abs. 1: Skilifte und Kleinseilbahnen ohne
        # Erschliessungsfunktion benoetigen eine Bewilligung des Kantons.
        ist_skilift_oder_kleinseilbahn = person('ist_skilift_oder_kleinseilbahn', period)
        hat_erschliessungsfunktion = person('personenbefoerderung_erschliessungsfunktion', period)
        return ist_skilift_oder_kleinseilbahn * ~hat_erschliessungsfunktion


class ist_skilift_oder_kleinseilbahn(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlage ist ein Skilift oder eine Kleinseilbahn"
    reference = "SR 745.1 Art. 7 Abs. 1"


class kantonale_bewilligung_maximale_dauer_jahre(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der kantonalen Bewilligung in Jahren (10 Jahre)"
    reference = "SR 745.1 Art. 7 Abs. 4"
    default_value = 10.0
