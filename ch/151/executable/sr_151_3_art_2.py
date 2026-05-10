"""SR 151.3 Art. 2

Generated from: ch/151/de/151.3.md

Begriffe: Definition von Behinderung und Benachteiligung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_dauernde_beeintraechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine voraussichtlich dauernde koerperliche, geistige oder psychische Beeintraechtigung vorliegt"
    reference = "SR 151.3 Art. 2 Abs. 1"


class beeintraechtigung_erschwert_alltag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beeintraechtigung alltaegliche Verrichtungen erschwert oder verunmoeglicht"
    reference = "SR 151.3 Art. 2 Abs. 1"


class ist_mensch_mit_behinderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Mensch mit Behinderung im Sinne des BehiG gilt"
    reference = "SR 151.3 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        beeintraechtigung = person('hat_dauernde_beeintraechtigung', period)
        erschwert = person('beeintraechtigung_erschwert_alltag', period)
        return beeintraechtigung * erschwert


class benachteiligung_zugang_baute(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Benachteiligung beim Zugang zu Bauten/Anlagen aus baulichen Gruenden vorliegt"
    reference = "SR 151.3 Art. 2 Abs. 3"


class benachteiligung_dienstleistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Benachteiligung bei der Inanspruchnahme einer Dienstleistung vorliegt"
    reference = "SR 151.3 Art. 2 Abs. 4"


class benachteiligung_ausbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Benachteiligung bei der Inanspruchnahme von Aus- und Weiterbildung vorliegt"
    reference = "SR 151.3 Art. 2 Abs. 5"
