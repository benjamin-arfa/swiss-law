"""SR 241 Art. 9

Generated from: ch/de/241.md

Standing to sue: persons threatened or harmed in their customer base,
credit, professional reputation, or economic interests may request
prohibition, removal, or declaration of unlawfulness.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class klageberechtigt_uwg_art9(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nach Art. 9 UWG klageberechtigt ist"
    reference = "SR 241 Art. 9 Abs. 1"


class anspruch_verbot_verletzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf Verbot einer drohenden Verletzung besteht"
    reference = "SR 241 Art. 9 Abs. 1 Bst. a"


class anspruch_beseitigung_verletzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf Beseitigung einer bestehenden Verletzung besteht"
    reference = "SR 241 Art. 9 Abs. 1 Bst. b"


class anspruch_feststellung_widerrechtlichkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf Feststellung der Widerrechtlichkeit besteht"
    reference = "SR 241 Art. 9 Abs. 1 Bst. c"


class anspruch_schadenersatz_uwg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf Schadenersatz und Genugtuung nach OR besteht"
    reference = "SR 241 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        return person('klageberechtigt_uwg_art9', period)
