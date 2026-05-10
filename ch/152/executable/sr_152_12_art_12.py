"""SR 152.12 Art. 12 - Verlaengerung der Schutzfrist (Extension of Protection Period)

Generated from: ch/152/de/152.12.md

The protection period can be extended by the court management if there
is an overriding legitimate public or private interest against access by third parties.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ueberwiegendes_schutzinteresse_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein ueberwiegendes schutzwuerdiges Interesse gegen Einsichtnahme besteht"
    reference = "SR 152.12 Art. 12 Abs. 1"


class schutzfrist_verlaengert_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schutzfrist durch Beschluss der Gerichtsleitung verlaengert wurde"
    reference = "SR 152.12 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        return person('ueberwiegendes_schutzinteresse_bstger', period)
