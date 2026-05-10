"""SR 943.02 Art. 2

Generated from: ch/943/de/943.02.md

Freier Zugang zum Markt:
- Jede Person darf Waren/Dienstleistungen/Arbeitsleistungen in der ganzen
  Schweiz anbieten, wenn die Tätigkeit im Kanton der Niederlassung zulässig ist
- Vorschriften des Kantons der Niederlassung/des Sitzes gelten
- Niederlassungsfreiheit für rechtmässige Ausübung auf dem ganzen Gebiet
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_niederlassung_oder_sitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Niederlassung oder Sitz in der Schweiz hat"
    reference = "SR 943.02 Art. 2 Abs. 1"


class taetigkeit_im_niederlassungskanton_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Erwerbstätigkeit im Kanton der Niederlassung/des Sitzes zulässig ist"
    reference = "SR 943.02 Art. 2 Abs. 1"


class hat_freien_marktzugang(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person freien Zugang zum Schweizer Binnenmarkt hat"
    reference = "SR 943.02 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        niederlassung = person('hat_niederlassung_oder_sitz_schweiz', period)
        zulaessig = person('taetigkeit_im_niederlassungskanton_zulaessig', period)
        return niederlassung * zulaessig
