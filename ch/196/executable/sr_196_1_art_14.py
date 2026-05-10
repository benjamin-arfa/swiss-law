"""SR 196.1 Art. 14

Generated from: ch/196/de/196.1.md

Bedingungen und Verfahren der Einziehung: Das Bundesverwaltungsgericht ordnet
die Einziehung an wenn die Bedingungen erfuellt sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermoegenswerte_unterliegen_verfuegungsmacht_pep(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermoegenswerte der Verfuegungsmacht einer PEP oder nahestehenden Person unterliegen"
    reference = "SR 196.1 Art. 14 Abs. 2 lit. a"


class vermoegenswerte_unrechtmaessig_erworben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermoegenswerte unrechtmaessig erworben wurden"
    reference = "SR 196.1 Art. 14 Abs. 2 lit. b"


class vermoegenswerte_nach_art_4_gesperrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermoegenswerte vom Bundesrat nach Art. 4 im Hinblick auf Einziehung gesperrt wurden"
    reference = "SR 196.1 Art. 14 Abs. 2 lit. c"


class einziehung_anzuordnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Bundesverwaltungsgericht die Einziehung anordnen muss"
    reference = "SR 196.1 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        verfuegungsmacht = person('vermoegenswerte_unterliegen_verfuegungsmacht_pep', period)
        unrechtmaessig = person('vermoegenswerte_unrechtmaessig_erworben', period)
        gesperrt = person('vermoegenswerte_nach_art_4_gesperrt', period)
        return verfuegungsmacht * unrechtmaessig * gesperrt
