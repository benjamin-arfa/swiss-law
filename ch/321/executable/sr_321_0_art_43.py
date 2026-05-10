"""SR 321.0 Art. 43

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schwerste_einzelstrafe_monate(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Strafe fuer die schwerste Einzeltat (in Monaten)"
    reference = "SR 321.0 Art. 43 Abs. 1"


class gesetzliches_hoechstmass_monate(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesetzliches Hoechstmass der Strafart (in Monaten)"
    reference = "SR 321.0 Art. 43 Abs. 1"


class gesamtstrafe_max_monate(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Gesamtstrafe bei Konkurrenz (schwerste Strafe + max. Haelfte, begrenzt durch gesetzliches Hoechstmass)"
    reference = "SR 321.0 Art. 43 Abs. 1"

    def formula(person, period, parameters):
        schwerste = person('schwerste_einzelstrafe_monate', period)
        hoechstmass = person('gesetzliches_hoechstmass_monate', period)
        erhoehung = schwerste * 1.5
        return where(erhoehung > hoechstmass, hoechstmass, erhoehung)
