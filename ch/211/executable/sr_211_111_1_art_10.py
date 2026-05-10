"""SR 211.111.1 Art. 10

Generated from: ch/211/de/211.111.1.md

Berichterstattung: Meldepflichten nach Eingriffen an urteilsunfaehigen
Personen und Personen unter Beistandschaft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_heileingriff_an_urteilsunfaehiger_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Heileingriff nach Art. 2 Abs. 2 an einer urteilsunfaehigen Person durchgefuehrt wurde"
    reference = "SR 211.111.1 Art. 10 Abs. 1"


class hat_person_unter_beistandschaft_sterilisiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Person unter umfassender Beistandschaft oder dauernd Urteilsunfaehige sterilisiert wurde"
    reference = "SR 211.111.1 Art. 10 Abs. 2"


class meldefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Meldefrist in Tagen nach Durchfuehrung des Eingriffs"
    reference = "SR 211.111.1 Art. 10"

    def formula(person, period, parameters):
        heileingriff = person('hat_heileingriff_an_urteilsunfaehiger_durchgefuehrt', period)
        beistandschaft = person('hat_person_unter_beistandschaft_sterilisiert', period)
        # Art. 10 Abs. 1: 10 Tage; Art. 10 Abs. 2: 30 Tage
        return heileingriff * 10 + beistandschaft * (1 - heileingriff) * 30
