"""SR 979.1 Art. 6

Generated from: ch/979/de/979.1.md

Art. 6 Grundsaetze der Entwicklungspolitik:
In the framework of the Bretton Woods institutions, Swiss positions and
decisions concerning developing countries must take into account the
principles and objectives of Swiss development policy.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bw_entscheid_betrifft_entwicklungslaender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Entscheid im Rahmen der BW-Institutionen Entwicklungslaender betrifft"
    reference = "SR 979.1 Art. 6"


class bw_entwicklungspolitik_zu_beruecksichtigen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Grundsaetze der schweizerischen Entwicklungspolitik zu beruecksichtigen sind"
    reference = "SR 979.1 Art. 6"

    def formula(person, period, parameters):
        return person('bw_entscheid_betrifft_entwicklungslaender', period)
