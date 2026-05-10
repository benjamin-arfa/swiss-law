"""SR 196.1 Art. 16

Generated from: ch/196/de/196.1.md

Rechte Dritter: Vermoegenswerte koennen nicht eingezogen werden, wenn
bestimmte Rechte Dritter bestehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schweizerische_behoerde_macht_rechte_geltend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine schweizerische Behoerde Rechte an den Vermoegenswerten geltend macht"
    reference = "SR 196.1 Art. 16 lit. a"


class dritter_hat_gutglaeubig_dingliche_rechte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein der PEP nicht nahestehender Dritter gutglaeubig dingliche Rechte erworben hat"
    reference = "SR 196.1 Art. 16 lit. b"


class einziehung_ausgeschlossen_rechte_dritter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einziehung wegen Rechten Dritter ausgeschlossen ist"
    reference = "SR 196.1 Art. 16"

    def formula(person, period, parameters):
        behoerde = person('schweizerische_behoerde_macht_rechte_geltend', period)
        dritter = person('dritter_hat_gutglaeubig_dingliche_rechte', period)
        return behoerde + dritter > 0
