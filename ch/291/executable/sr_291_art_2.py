"""SR 291 Art. 2

Generated from: ch/291/de/291.md

Allgemeine Zustaendigkeit: Sieht dieses Gesetz keine besondere Zustaendigkeit
vor, so sind die schweizerischen Gerichte oder Behoerden am Wohnsitz des
Beklagten zustaendig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beklagter_hat_wohnsitz_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beklagte Wohnsitz in der Schweiz hat"
    reference = "SR 291 Art. 2"


class besondere_zustaendigkeit_vorgesehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das IPRG eine besondere Zustaendigkeit vorsieht"
    reference = "SR 291 Art. 2"


class allgemeine_zustaendigkeit_am_wohnsitz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die allgemeine Zustaendigkeit am Wohnsitz des Beklagten greift"
    reference = "SR 291 Art. 2"

    def formula(person, period, parameters):
        hat_wohnsitz = person('beklagter_hat_wohnsitz_in_schweiz', period)
        keine_besondere = not_(person('besondere_zustaendigkeit_vorgesehen', period))
        return hat_wohnsitz * keine_besondere
