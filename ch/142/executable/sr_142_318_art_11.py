"""SR 142.318 Art. 11

Generated from: ch/142/de/142.318.md

Uebergangsbestimmung: Art. 4-6 gelten nicht fuer bereits angesetzte
Befragungen. Temporaere Vorhaben nach Art. 3 muessen nach Ablauf
dem Plangenehmigungsverfahren unterstellt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class befragung_bereits_angesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob bei Inkrafttreten der Verordnung bereits eine Befragung angesetzt war"
    reference = "SR 142.318 Art. 11 Abs. 1"


class befragungsregeln_art4_6_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Befragungsregeln nach Art. 4-6 anwendbar sind"
    reference = "SR 142.318 Art. 11 Abs. 1"

    def formula_2020_04(person, period, parameters):
        return not_(person('befragung_bereits_angesetzt', period))


class temporaere_vorhaben_plangenehmigung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob temporaere Vorhaben dem Plangenehmigungsverfahren unterstellt werden muessen"
    reference = "SR 142.318 Art. 11 Abs. 2"

    def formula_2020_04(person, period, parameters):
        # Plangenehmigung erst nach Ablauf der Geltungsdauer erforderlich
        return False
