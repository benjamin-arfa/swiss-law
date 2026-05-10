"""SR 192.126 Art. 33

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class in_probezeit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person befindet sich in der Probezeit"
    reference = "SR 192.126 Art. 33"

class probezeit_dauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vereinbarte Probezeit in Monaten (max. 3, Art. 33)"
    reference = "SR 192.126 Art. 33"

    def formula(person, period, parameters):
        # Art. 33: Probezeit betraegt 1 Monat, kann auf max. 3 Monate verlaengert werden
        return where(person('in_probezeit', period.first_month), 1, 0)

class kuendigungsfrist_probezeit_tage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Kuendigungsfrist waehrend Probezeit in Tagen (Art. 33 Abs. 2)"
    reference = "SR 192.126 Art. 33"

    def formula(person, period, parameters):
        # Art. 33 Abs. 2: 7 Tage waehrend der Probezeit
        return person('in_probezeit', period) * 7
