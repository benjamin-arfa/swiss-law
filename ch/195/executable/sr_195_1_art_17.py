"""SR 195.1 Art. 17

Generated from: ch/195/de/195.1.md

Ausschluss vom Stimmrecht: Auslandschweizer die wegen dauernder
Urteilsunfaehigkeit unter umfassender Beistandschaft stehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unter_umfassender_beistandschaft_wegen_urteilsunfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person wegen dauernder Urteilsunfaehigkeit unter umfassender Beistandschaft steht oder durch Vorsorgebeauftragte vertreten wird"
    reference = "SR 195.1 Art. 17 lit. a"


class auslaendische_erwachsenenschutzmassnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob nach auslaendischem Recht wegen dauernder Urteilsunfaehigkeit eine die Handlungsfaehigkeit aufhebende Massnahme besteht"
    reference = "SR 195.1 Art. 17 lit. b"


class ausgeschlossen_vom_stimmrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person vom Stimmrecht ausgeschlossen ist"
    reference = "SR 195.1 Art. 17"

    def formula(person, period, parameters):
        lit_a = person('unter_umfassender_beistandschaft_wegen_urteilsunfaehigkeit', period)
        lit_b = person('auslaendische_erwachsenenschutzmassnahme', period)
        return lit_a + lit_b > 0
