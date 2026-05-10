"""SR 195.1 Art. 16

Generated from: ch/195/de/195.1.md

Umfang der politischen Rechte: Auslandschweizer ab 18 Jahren koennen an
eidgenoessischen Wahlen und Abstimmungen teilnehmen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_person(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 195.1 Art. 16 Abs. 1"


class kann_an_eidg_wahlen_teilnehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an eidgenoessischen Wahlen und Abstimmungen teilnehmen kann"
    reference = "SR 195.1 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        auslandschweizer = person('ist_auslandschweizer', period)
        volljaerig = person('alter_person', period) >= 18
        return auslandschweizer * volljaerig
