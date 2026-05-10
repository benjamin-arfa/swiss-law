"""SR 211.111.1 Art. 2

Generated from: ch/211/de/211.111.1.md

Sterilisation: Definition des medizinischen Eingriffs und Abgrenzung
zu Heileingriffen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eingriff_hebt_fortpflanzungsfaehigkeit_auf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Eingriff die Fortpflanzungsfaehigkeit einer Person auf Dauer aufhebt"
    reference = "SR 211.111.1 Art. 2 Abs. 1"


class ist_heileingriff_mit_begleiterscheinung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Heileingriff handelt, dessen unvermeidliche Begleiterscheinung die Aufhebung der Fortpflanzungsfaehigkeit ist"
    reference = "SR 211.111.1 Art. 2 Abs. 2"


class ist_sterilisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Eingriff als Sterilisation im Sinne dieses Gesetzes gilt"
    reference = "SR 211.111.1 Art. 2"

    def formula(person, period, parameters):
        hebt_auf = person('eingriff_hebt_fortpflanzungsfaehigkeit_auf', period)
        heileingriff = person('ist_heileingriff_mit_begleiterscheinung', period)
        return hebt_auf * (1 - heileingriff)


class durchfuehrende_person_ist_arzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die durchfuehrende Person eine Aerztin oder ein Arzt ist"
    reference = "SR 211.111.1 Art. 2 Abs. 3"
