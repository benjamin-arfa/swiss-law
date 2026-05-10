"""SR 455.110.2 Art. 14

Generated from: ch/455/de/455.110.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zeit_seit_aufhaengen_sekunden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zeit seit dem Aufhaengen des Gefluegels in Sekunden"
    reference = "SR 455.110.2 Art. 14 Abs. 3"


class gefluegel_betaeubungszeitfenster_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betaeubungszeitfenster fuer aufgehaengtes Gefluegel konform (12-60 Sek.) nach Art. 14 Abs. 3 SR 455.110.2"
    reference = "SR 455.110.2 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        zeit = person('zeit_seit_aufhaengen_sekunden', period)
        return (zeit >= 12) * (zeit <= 60)
