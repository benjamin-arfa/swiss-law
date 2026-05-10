"""SR 251.5 Art. 19

Generated from: ch/251/de/251.5.md

Widerspruchsverfahren: Wird innerhalb von 5 Monaten nach Eingang der
Meldung kein Verfahren eroeffnet, entfaellt die Sanktion.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class meldung_eingegangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Meldung nach Art. 49a Abs. 3 Bst. a KG eingegangen ist"
    reference = "SR 251.5 Art. 19"


class widerspruchsfrist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Eroeffnung eines Verfahrens nach Meldungseingang in Monaten (5 Monate)"
    reference = "SR 251.5 Art. 19"

    def formula(person, period, parameters):
        return 5


class verfahren_innert_frist_eroeffnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob innerhalb der 5-Monats-Frist ein Verfahren eroeffnet wurde"
    reference = "SR 251.5 Art. 19"


class sanktion_entfaellt_widerspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sanktion fuer den gemeldeten Sachverhalt entfaellt (kein Verfahren innert 5 Monaten)"
    reference = "SR 251.5 Art. 19"

    def formula(person, period, parameters):
        return (
            person('meldung_eingegangen', period)
            * not_(person('verfahren_innert_frist_eroeffnet', period))
        )
