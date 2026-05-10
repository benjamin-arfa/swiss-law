"""SR 351.20 Art. 27

Generated from: ch/351/de/351.20.md
Appeal deadlines for international court cooperation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schlussverfuegung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um eine Schlussverfuegung"
    reference = "SR 351.20 Art. 27"


class ist_zwischenverfuegung_art24_abs2(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um eine Zwischenverfuegung nach Art. 24 Abs. 2"
    reference = "SR 351.20 Art. 27"


class beschwerdefrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beschwerdefrist in Tagen ab schriftlicher Eroeffnung"
    reference = "SR 351.20 Art. 27"

    def formula(person, period):
        schlussverfuegung = person('ist_schlussverfuegung', period)
        # Schlussverfuegung: 20 Tage, Zwischenverfuegung: 10 Tage
        return where(schlussverfuegung, 20, 10)
