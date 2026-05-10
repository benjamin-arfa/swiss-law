"""SR 195.1 Art. 3

Generated from: ch/195/de/195.1.md

Begriffe: Definitionen von Auslandschweizer, Auslandschweizerregister,
Empfangsstaat und Vertretung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schweizer_staatsangehoeriger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person die Schweizer Staatsangehoerigkeit besitzt"
    reference = "SR 195.1 Art. 3 lit. a"


class hat_wohnsitz_in_der_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in der Schweiz Wohnsitz hat"
    reference = "SR 195.1 Art. 3 lit. a"


class ist_im_auslandschweizerregister_eingetragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person im Auslandschweizerregister eingetragen ist"
    reference = "SR 195.1 Art. 3 lit. a"


class ist_auslandschweizer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Auslandschweizerin/Auslandschweizer gilt"
    reference = "SR 195.1 Art. 3 lit. a"

    def formula(person, period, parameters):
        schweizer = person('ist_schweizer_staatsangehoeriger', period)
        kein_wohnsitz = 1 - person('hat_wohnsitz_in_der_schweiz', period)
        eingetragen = person('ist_im_auslandschweizerregister_eingetragen', period)
        return schweizer * kein_wohnsitz * eingetragen
