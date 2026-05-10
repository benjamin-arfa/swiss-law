"""SR 351.93 Art. 17c

Generated from: ch/351/de/351.93.md
Appeal deadlines for US-Swiss mutual legal assistance.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schlussverfuegung_rvus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um eine Schlussverfuegung (vs. Zwischenverfuegung)"
    reference = "SR 351.93 Art. 17c"


class beschwerdefrist_tage_rvus(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beschwerdefrist in Tagen ab schriftlicher Mitteilung der Verfuegung"
    reference = "SR 351.93 Art. 17c"

    def formula(person, period):
        schlussverfuegung = person('ist_schlussverfuegung_rvus', period)
        # Schlussverfuegung: 30 Tage, Zwischenverfuegung: 10 Tage
        return where(schlussverfuegung, 30, 10)
