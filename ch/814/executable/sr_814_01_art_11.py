"""SR 814.01 Art. 11

Generated from: ch/814/de/814.01.md

Emissionsbegrenzungen: Grundsatz. Emissionen bei der Quelle begrenzen,
Vorsorgeprinzip, Verschaerfung bei schaedlichen Einwirkungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class betreibt_anlage_mit_emissionen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine Anlage betreibt, die Emissionen verursacht"
    reference = "SR 814.01 Art. 11 Abs. 1"


class emissionen_technisch_begrenzbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Emissionen technisch und betrieblich begrenzt werden koennen"
    reference = "SR 814.01 Art. 11 Abs. 2"


class emissionen_wirtschaftlich_tragbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Emissionsbegrenzung wirtschaftlich tragbar ist"
    reference = "SR 814.01 Art. 11 Abs. 2"


class einwirkungen_schaedlich_oder_laestig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Einwirkungen schaedlich oder laestig sind oder werden koennten"
    reference = "SR 814.01 Art. 11 Abs. 3"


class emissionsbegrenzung_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Pflicht zur Emissionsbegrenzung besteht"
    reference = "SR 814.01 Art. 11"

    def formula(person, period, parameters):
        betreibt = person('betreibt_anlage_mit_emissionen', period)
        return betreibt


class emissionsbegrenzung_verschaerft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob verschaerfte Emissionsbegrenzungen gelten (bei schaedlichen Einwirkungen)"
    reference = "SR 814.01 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        betreibt = person('betreibt_anlage_mit_emissionen', period)
        schaedlich = person('einwirkungen_schaedlich_oder_laestig', period)
        return betreibt * schaedlich
