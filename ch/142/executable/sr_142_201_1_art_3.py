"""SR 142.201.1 Art. 3

Generated from: ch/142/de/142.201.1.md

Erteilung von Kurzaufenthalts-, Aufenthalts- und Niederlassungsbewilligungen
in speziellen Faellen, die dem SEM zur Zustimmung zu unterbreiten sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_keinen_gueltigen_pass(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person keinen gueltigen heimatlichen Pass besitzt"
    reference = "SR 142.201.1 Art. 3 Bst. a"


class nach_widerruf_buergerrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob nach rechtskraeftigem Widerruf des Schweizer Buergerrechts"
    reference = "SR 142.201.1 Art. 3 Bst. c"


class vorzeitige_niederlassungsbewilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob vorzeitige Erteilung der Niederlassungsbewilligung (Art. 34 Abs. 3 AIG)"
    reference = "SR 142.201.1 Art. 3 Bst. d"


class ist_professor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Professor/in ist"
    reference = "SR 142.201.1 Art. 3 Bst. d"


class bewilligung_gestuetzt_art_8_emrk(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Aufenthaltsbewilligung gestuetzt auf Art. 8 EMRK"
    reference = "SR 142.201.1 Art. 3 Bst. f"


class zustimmung_sem_spezielle_bewilligung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung des SEM fuer spezielle Bewilligungen erforderlich ist"
    reference = "SR 142.201.1 Art. 3"

    def formula(person, period, parameters):
        vorzeitig = (
            person('vorzeitige_niederlassungsbewilligung', period)
            * not_(person('ist_professor', period))
        )
        return (
            person('hat_keinen_gueltigen_pass', period)
            + person('hat_verstoss_oeffentliche_sicherheit', period)
            + person('nach_widerruf_buergerrecht', period)
            + vorzeitig
            + person('bewilligung_gestuetzt_art_8_emrk', period)
        ) > 0
