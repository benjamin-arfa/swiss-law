"""SR 425.15 Art. 14

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ausserordentlicher_mehraufwand_stunden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ausserordentlicher Mehraufwand in Stunden (neben Sitzungsvorbereitung/-nachbereitung)"
    reference = "SR 425.15 Art. 14 Abs. 1"


class stundenansatz_ausserordentlicher_mehraufwand(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Stundenansatz fuer ausserordentlichen Mehraufwand in CHF"
    reference = "SR 425.15 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return 120.0


class entschaedigung_ausserordentlicher_mehraufwand(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entschaedigung fuer ausserordentlichen Mehraufwand in CHF"
    reference = "SR 425.15 Art. 14"

    def formula(person, period, parameters):
        stunden = person('ausserordentlicher_mehraufwand_stunden', period)
        return stunden * 120.0
