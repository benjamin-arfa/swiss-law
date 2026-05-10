"""SR 151.15 Art. 6

Generated from: ch/151/de/151.15.md

Entscheid ueber Finanzhilfen: EDI bei ueber CHF 200'000, Buero bei
bis CHF 200'000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beantragter_beitrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoehe des beantragten Beitrags fuer Finanzhilfen"
    reference = "SR 151.15 Art. 6"


class entscheid_durch_edi(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das EDI ueber die Finanzhilfe entscheidet (Beitrag ueber CHF 200'000)"
    reference = "SR 151.15 Art. 6 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        beitrag = person('beantragter_beitrag', period)
        return beitrag > 200000


class entscheid_durch_buero(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Buero ueber die Finanzhilfe entscheidet (Beitrag bis CHF 200'000)"
    reference = "SR 151.15 Art. 6 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        beitrag = person('beantragter_beitrag', period)
        return beitrag <= 200000
