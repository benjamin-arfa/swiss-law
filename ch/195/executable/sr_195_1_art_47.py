"""SR 195.1 Art. 47

Generated from: ch/195/de/195.1.md

Notdarlehen: Zinslose Darlehen fuer in Not geratene Personen im Ausland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_in_not_geraten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in Not geraten ist"
    reference = "SR 195.1 Art. 47"


class haelt_sich_voruebergehend_im_ausland_auf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person voruebergehend im Ausland aufhaelt"
    reference = "SR 195.1 Art. 47"


class anspruch_auf_notdarlehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bund der Person ein zinsloses Notdarlehen gewaehren kann"
    reference = "SR 195.1 Art. 47"

    def formula(person, period, parameters):
        in_not = person('ist_in_not_geraten', period)
        voruebergehend = person('haelt_sich_voruebergehend_im_ausland_auf', period)
        return in_not * voruebergehend
