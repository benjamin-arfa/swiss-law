"""SR 251.5 Art. 4

Generated from: ch/251/de/251.5.md

Dauer: Bei 1-5 Jahren Dauer wird der Basisbetrag um bis zu 50% erhoeht.
Bei mehr als 5 Jahren wird fuer jedes zusaetzliche Jahr bis zu 10% aufgeschlagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dauer_wettbewerbsverstoss_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer des Wettbewerbsverstosses in Jahren"
    reference = "SR 251.5 Art. 4"


class dauer_zuschlag_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentualer Zuschlag zum Basisbetrag aufgrund der Dauer des Verstosses"
    reference = "SR 251.5 Art. 4"


class sanktion_nach_dauer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sanktionsbetrag nach Beruecksichtigung der Dauer des Verstosses"
    reference = "SR 251.5 Art. 4"

    def formula(person, period, parameters):
        basisbetrag = person('sanktion_basisbetrag', period)
        dauer = person('dauer_wettbewerbsverstoss_jahre', period)
        zuschlag = person('dauer_zuschlag_prozent', period)
        # 1-5 Jahre: bis zu 50% Erhoehung
        # >5 Jahre: bis zu 10% pro zusaetzliches Jahr
        return basisbetrag * (1 + zuschlag / 100)
