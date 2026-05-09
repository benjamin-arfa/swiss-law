"""SR 232.16 Art. 7

Generated from: ch/232/de/232.16.md

Art. 7 defines the farmer's privilege (Landwirteprivileg): farmers who
acquired propagation material may multiply harvest in their own farm.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_landwirt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Landwirt"
    reference = "SR 232.16 Art. 7 Abs. 1"


class vermehrungsmaterial_rechtmaessig_erworben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermehrungsmaterial wurde durch den Sortenschutzinhaber oder mit dessen Zustimmung erworben"
    reference = "SR 232.16 Art. 7 Abs. 1"


class erntegut_im_eigenen_betrieb_gewonnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Erntegut wurde im eigenen Betrieb durch Anbau gewonnen"
    reference = "SR 232.16 Art. 7 Abs. 1"


class landwirteprivileg_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Landwirteprivileg ist anwendbar (Vermehrung im eigenen Betrieb erlaubt)"
    reference = "SR 232.16 Art. 7"

    def formula(person, period, parameters):
        landwirt = person('ist_landwirt', period)
        erworben = person('vermehrungsmaterial_rechtmaessig_erworben', period)
        eigener_betrieb = person('erntegut_im_eigenen_betrieb_gewonnen', period)
        return landwirt * erworben * eigener_betrieb
