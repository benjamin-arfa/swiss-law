"""SR 142.318 Art. 6

Generated from: ch/142/de/142.318.md

Teilnahme der Rechtsvertretung, bevollmaechtigter Personen und der
Hilfswerkvertretung: Kann die Rechtsvertretung nicht teilnehmen, wird
die Befragung ohne sie durchgefuehrt und entfaltet ihre Rechtswirkung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rechtsvertretung_kann_teilnehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die zugewiesene Rechtsvertretung an der Befragung teilnehmen kann"
    reference = "SR 142.318 Art. 6 Abs. 1"


class befragung_ohne_rechtsvertretung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Befragung ohne Rechtsvertretung gueltig ist und Rechtswirkung entfaltet"
    reference = "SR 142.318 Art. 6 Abs. 1"

    def formula_2020_04(person, period, parameters):
        kann_teilnehmen = person('rechtsvertretung_kann_teilnehmen', period)
        return not_(kann_teilnehmen)


class hilfswerkvertretung_kann_teilnehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Hilfswerkvertretung an der Befragung teilnehmen kann"
    reference = "SR 142.318 Art. 6 Abs. 2"


class befragung_ohne_hilfswerkvertretung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Befragung ohne Hilfswerkvertretung gueltig ist"
    reference = "SR 142.318 Art. 6 Abs. 2"

    def formula_2020_04(person, period, parameters):
        kann_teilnehmen = person('hilfswerkvertretung_kann_teilnehmen', period)
        return not_(kann_teilnehmen)
