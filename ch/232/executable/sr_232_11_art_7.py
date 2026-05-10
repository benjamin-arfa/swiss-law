"""SR 232.11 Art. 7

Generated from: ch/232/de/232.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ersthinterlegung_in_pvu_staat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Marke erstmals in einem Mitgliedstaat der Pariser Verbandsübereinkunft hinterlegt"
    reference = "SR 232.11 Art. 7 Abs. 1"


class monate_seit_ersthinterlegung(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Monate seit der Ersthinterlegung im Ausland"
    reference = "SR 232.11 Art. 7 Abs. 1"


class hinterlegungsprioritaet_beanspruchbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Hinterlegungspriorität nach Pariser Verbandsübereinkunft kann beansprucht werden"
    reference = "SR 232.11 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        pvu_staat = person('ersthinterlegung_in_pvu_staat', period)
        monate = person('monate_seit_ersthinterlegung', period)
        # Hinterlegung in der Schweiz innerhalb von 6 Monaten nach Ersthinterlegung
        return pvu_staat * (monate <= 6)
