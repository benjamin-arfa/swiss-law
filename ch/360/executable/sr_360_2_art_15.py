"""SR 360.2 Art. 15

Generated from: ch/360/de/360.2.md

Datenkontrolle: Frist von 60 Tagen fuer Berichtigung mangelhafter Eintraege.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_eintrag_mangelhaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "NES-Eintrag ist mangelhaft und wurde zur Berichtigung zurueckgewiesen"
    reference = "SR 360.2 Art. 15 Abs. 3"


class nes_berichtigungsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Berichtigung mangelhafter NES-Eintraege in Tagen"
    reference = "SR 360.2 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        return person('nes_eintrag_mangelhaft', period) * 0 + 60


class nes_tage_seit_rueckweisung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Tage seit Rueckweisung des mangelhaften Eintrags"
    reference = "SR 360.2 Art. 15 Abs. 3"


class nes_eintrag_wird_geloescht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Mangelhafter Eintrag wird durch die Aufsicht geloescht"
    reference = "SR 360.2 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        mangelhaft = person('nes_eintrag_mangelhaft', period)
        tage = person('nes_tage_seit_rueckweisung', period)
        return mangelhaft * (tage >= 60)
