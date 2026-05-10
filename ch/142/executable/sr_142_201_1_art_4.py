"""SR 142.201.1 Art. 4

Generated from: ch/142/de/142.201.1.md

Verlaengerung von Aufenthaltsbewilligungen in speziellen Faellen, die
dem SEM zur Zustimmung zu unterbreiten sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pass_nicht_verlaengerbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der heimatliche Pass nicht mehr verlaengert werden kann"
    reference = "SR 142.201.1 Art. 4 Bst. a"


class ausbildung_ueber_8_jahre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Aufenthalt fuer Aus-/Weiterbildung voraussichtlich laenger als 8 Jahre dauert"
    reference = "SR 142.201.1 Art. 4 Bst. b"


class nach_aufloesung_ehe_oder_tod(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob nach Aufloesung der ehelichen Gemeinschaft oder Tod des Ehegatten (Art. 50 AIG)"
    reference = "SR 142.201.1 Art. 4 Bst. d"


class zustimmung_sem_verlaengerung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung des SEM fuer die Verlaengerung erforderlich ist"
    reference = "SR 142.201.1 Art. 4"

    def formula(person, period, parameters):
        nicht_eu = person('ist_staatsangehoeriger_nicht_eu_efta', period)
        return (
            person('pass_nicht_verlaengerbar', period)
            + (nicht_eu * person('ausbildung_ueber_8_jahre', period))
            + person('hat_verstoss_oeffentliche_sicherheit', period)
            + person('nach_aufloesung_ehe_oder_tod', period)
        ) > 0
