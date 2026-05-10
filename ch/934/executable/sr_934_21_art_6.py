"""SR 934.21 Art. 6

Generated from: ch/934/de/934.21.md

Art. 6 Anstellungsverhaeltnisse:
1. Public-law employment relationships of personnel of existing armament
   operations are converted to private-law employment contracts upon the
   transfer of operations to corporations.
2. The Federal Council issues transitional provisions after consulting
   employee associations; these apply at most until the end of the current
   term of office.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bgrb_oeffentlich_rechtliches_dienstverhaeltnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein oeffentlich-rechtliches Dienstverhaeltnis hat"
    reference = "SR 934.21 Art. 6 Abs. 1"


class bgrb_umwandlung_privatrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Dienstverhaeltnis in ein privatrechtliches Anstellungsverhaeltnis umgewandelt wird"
    reference = "SR 934.21 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        oeffentlich = person('bgrb_oeffentlich_rechtliches_dienstverhaeltnis', period)
        ueberfuehrt = person('bgrb_betrieb_ueberfuehrt', period)
        return oeffentlich * ueberfuehrt
