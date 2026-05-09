"""SR 291 Art. 4

Generated from: ch/291/de/291.md

Arrestort als Gerichtsstand: Sieht das IPRG keine andere Zustaendigkeit
in der Schweiz vor, so kann die Klage auf Prosequierung des Arrestes am
schweizerischen Arrestort erhoben werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class keine_andere_zustaendigkeit_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das IPRG keine andere Zustaendigkeit in der Schweiz vorsieht"
    reference = "SR 291 Art. 4"


class arrest_in_schweiz_vollzogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Arrest in der Schweiz vollzogen wurde"
    reference = "SR 291 Art. 4"


class klage_am_arrestort_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Klage auf Prosequierung des Arrestes am Arrestort erhoben werden kann"
    reference = "SR 291 Art. 4"

    def formula(person, period, parameters):
        keine_andere = person('keine_andere_zustaendigkeit_in_schweiz', period)
        arrest = person('arrest_in_schweiz_vollzogen', period)
        return keine_andere * arrest
