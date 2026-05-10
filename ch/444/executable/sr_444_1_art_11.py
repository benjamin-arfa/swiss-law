"""SR 444.1 Art. 11

Generated from: ch/444/de/444.1.md

Veroeffentlichung und Einspracheverfahren: Einsprachefrist 30 Tage ab
Veroeffentlichung im Bundesblatt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tage_seit_veroeffentlichung_bundesblatt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Tage seit Veroeffentlichung im Bundesblatt"
    reference = "SR 444.1 Art. 11 Abs. 3"


class einsprache_frist_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die 30-taegige Einsprachefrist abgelaufen ist"
    reference = "SR 444.1 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        tage = person('tage_seit_veroeffentlichung_bundesblatt', period)
        return tage > 30
