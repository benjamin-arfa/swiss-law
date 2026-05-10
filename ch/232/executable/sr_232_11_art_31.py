"""SR 232.11 Art. 31

Generated from: ch/232/de/232.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class inhaber_aelterer_marke(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist Inhaber einer älteren Marke im Sinne von Art. 3 Abs. 1"
    reference = "SR 232.11 Art. 31 Abs. 1"


class widerspruchsfrist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Widerspruchsfrist in Monaten nach Veröffentlichung der Eintragung"
    reference = "SR 232.11 Art. 31 Abs. 2"

    def formula(person, period, parameters):
        # Innerhalb von drei Monaten nach der Veröffentlichung
        return person.filled_array(3)


class widerspruch_gegen_geografische_marke(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Widerspruch richtet sich gegen eine geografische Marke"
    reference = "SR 232.11 Art. 31 Abs. 1bis"


class widerspruch_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Widerspruch gegen Markeneintragung ist zulässig"
    reference = "SR 232.11 Art. 31"

    def formula(person, period, parameters):
        inhaber = person('inhaber_aelterer_marke', period)
        geografisch = person('widerspruch_gegen_geografische_marke', period)
        # Kein Widerspruch gegen geografische Marken (Abs. 1bis)
        return inhaber * not_(geografisch)
