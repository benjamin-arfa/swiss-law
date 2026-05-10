"""SR 745.1 Art. 6

Generated from: ch/745/de/745.1.md

Personenbefoerderungskonzessionen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_personenbefoerderungskonzession(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen besitzt eine Personenbefoerderungskonzession des Bundes"
    reference = "SR 745.1 Art. 6 Abs. 1"


class konzession_maximale_dauer_jahre(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Konzessionsdauer in Jahren"
    reference = "SR 745.1 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        # Art. 6 Abs. 3: Konzession wird fuer hoechstens 25 Jahre erteilt,
        # bei Seilbahnen fuer hoechstens 40 Jahre.
        ist_seilbahn = person('ist_seilbahn_unternehmen', period)
        return where(ist_seilbahn, 40.0, 25.0)


class ist_seilbahn_unternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen betreibt eine Seilbahn"
    reference = "SR 745.1 Art. 6 Abs. 3"
