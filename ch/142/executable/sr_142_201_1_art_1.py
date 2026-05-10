"""SR 142.201.1 Art. 1

Generated from: ch/142/de/142.201.1.md

Aufenthalt mit Erwerbstaetigkeit: Vorentscheide und Bewilligungen,
die dem SEM zur Zustimmung zu unterbreiten sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_staatsangehoeriger_nicht_eu_efta(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Staatsangehoerige/r eines Nichtmitgliedstaats der EU/EFTA ist"
    reference = "SR 142.201.1 Art. 1"


class hat_selbstaendige_erwerbstaetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine selbstaendige Erwerbstaetigkeit ausueben will (Art. 19 AIG)"
    reference = "SR 142.201.1 Art. 1 Abs. a Ziff. 1"


class ist_anerkannte_person_wissenschaft_kultur_sport(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person anerkannt ist in Wissenschaft, Kultur oder Sport (Art. 23 Abs. 3 Bst. b AIG)"
    reference = "SR 142.201.1 Art. 1 Abs. a Ziff. 3"


class hat_besondere_berufliche_kenntnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person besondere berufliche Kenntnisse oder Faehigkeiten hat (Art. 23 Abs. 3 Bst. c AIG)"
    reference = "SR 142.201.1 Art. 1 Abs. a Ziff. 4"


class ist_religioese_betreuungsperson(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person religioese Betreuungs-/Lehrperson oder HSK-Lehrkraft ist (Art. 26a AIG)"
    reference = "SR 142.201.1 Art. 1 Abs. a Ziff. 7"


class hat_verstoss_oeffentliche_sicherheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person erheblich oder wiederholt gegen die oeffentliche Sicherheit verstossen hat"
    reference = "SR 142.201.1 Art. 1 Abs. b"


class zustimmung_sem_erwerbstaetigkeit_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung des SEM fuer Aufenthalt mit Erwerbstaetigkeit erforderlich ist"
    reference = "SR 142.201.1 Art. 1"

    def formula(person, period, parameters):
        nicht_eu = person('ist_staatsangehoeriger_nicht_eu_efta', period)
        return nicht_eu * (
            person('hat_selbstaendige_erwerbstaetigkeit', period)
            + person('ist_anerkannte_person_wissenschaft_kultur_sport', period)
            + person('hat_besondere_berufliche_kenntnisse', period)
            + person('ist_religioese_betreuungsperson', period)
            + person('hat_verstoss_oeffentliche_sicherheit', period)
        ) > 0
