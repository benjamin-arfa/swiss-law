"""SR 740.1 Art. 2 - Geltungsbereich

Generated from: ch/740/de/740.1.md

Dieses Gesetz gilt fuer saemtliche Verkehrstraeger, soweit sie einen
Einfluss auf den alpenquerenden Gueterschwerkehr haben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class verkehrstraeger_hat_einfluss_auf_alpenquerenden_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Verkehrstraeger hat einen Einfluss auf den alpenquerenden Gueterschwerkehr"
    reference = "SR 740.1 Art. 2"


class gvvg_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gueterverkehrsverlagerungsgesetz ist anwendbar"
    reference = "SR 740.1 Art. 2"

    def formula(self, period, parameters):
        return self('verkehrstraeger_hat_einfluss_auf_alpenquerenden_gueterverkehr', period)
