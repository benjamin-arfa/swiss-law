"""SR 311.1 Art. 25a

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mord_begangen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche einen Mord (Art. 112 StGB) begangen"
    reference = "SR 311.1 Art. 25a Abs. 1 lit. a"


class freiheitsentzug_min_drei_jahre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wurde der Jugendliche zu mindestens 3 Jahren Freiheitsentzug verurteilt"
    reference = "SR 311.1 Art. 25a Abs. 1 lit. b"


class keine_unterbringung_angeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wurde keine Unterbringung nach Art. 15 angeordnet"
    reference = "SR 311.1 Art. 25a Abs. 1 lit. c"


class schwerwiegende_gefahr_fuer_dritte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Stellt der Jugendliche eine schwerwiegende Gefahr fuer Dritte dar"
    reference = "SR 311.1 Art. 25a Abs. 1 lit. d"


class verwahrungsvorbehalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sind alle Voraussetzungen fuer einen Verwahrungsvorbehalt erfuellt"
    reference = "SR 311.1 Art. 25a"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        mord = person('mord_begangen', period)
        strafe = person('freiheitsentzug_min_drei_jahre', period)
        keine_unterbringung = person('keine_unterbringung_angeordnet', period)
        gefahr = person('schwerwiegende_gefahr_fuer_dritte', period)
        return (alter >= 16) * mord * strafe * keine_unterbringung * gefahr
