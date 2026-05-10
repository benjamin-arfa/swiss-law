"""SR 195.1 Art. 11

Generated from: ch/195/de/195.1.md

Eintrag im Auslandschweizerregister: Meldepflicht und Voraussetzung fuer
die Ausuebung von Rechten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_meldepflicht_auslandschweizerregister(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person sich zur Eintragung ins Auslandschweizerregister melden muss"
    reference = "SR 195.1 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        schweizer = person('ist_schweizer_staatsangehoeriger', period)
        kein_wohnsitz = 1 - person('hat_wohnsitz_in_der_schweiz', period)
        return schweizer * kein_wohnsitz


class eintrag_voraussetzung_fuer_rechte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Eintrag Voraussetzung fuer die Ausuebung der Rechte und Erbringung von Dienstleistungen ist"
    reference = "SR 195.1 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_im_auslandschweizerregister_eingetragen', period)
