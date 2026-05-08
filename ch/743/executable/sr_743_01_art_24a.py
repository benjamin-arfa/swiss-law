"""SR 743.01 Art. 24a

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Dienstunfaehigkeit.
Wer wegen Alkohol-, Betaeubungsmittel- oder Arzneimitteleinfluss oder
aus anderen Gruenden nicht ueber die erforderliche koerperliche und
geistige Leistungsfaehigkeit verfuegt, ist dienstunfaehig und darf
keine sicherheitsrelevante Taetigkeit im Seilbahnbereich ausueben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_person_unter_alkoholeinfluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person unter Alkoholeinfluss steht"
    reference = "SR 743.01 Art. 24a"


class seilbahn_person_unter_betaeubungsmitteleinfluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person unter Betaeubungsmittel- oder Arzneimitteleinfluss steht"
    reference = "SR 743.01 Art. 24a"


class seilbahn_person_sonstige_leistungsminderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person aus anderen Gruenden nicht leistungsfaehig ist"
    reference = "SR 743.01 Art. 24a"


class seilbahn_person_dienstunfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person im Seilbahnbereich als dienstunfaehig gilt"
    reference = "SR 743.01 Art. 24a"

    def formula(person, period, parameters):
        alkohol = person('seilbahn_person_unter_alkoholeinfluss', period)
        betaeubungsmittel = person('seilbahn_person_unter_betaeubungsmitteleinfluss', period)
        sonstige = person('seilbahn_person_sonstige_leistungsminderung', period)
        return (alkohol + betaeubungsmittel + sonstige) > 0
