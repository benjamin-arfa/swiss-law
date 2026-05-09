"""SR 241 Art. 4

Generated from: ch/de/241.md

Inducement to breach of contract: enticing customers to break contracts,
inducing disclosure of trade secrets, or inducing revocation of
consumer credit contracts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class verleitung_vertragsbruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Abnehmer zum Vertragsbruch verleitet werden"
    reference = "SR 241 Art. 4 Bst. a"


class verleitung_geheimnisverrat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Arbeitnehmer zum Verrat von Fabrikations- oder Geschaeftsgeheimnissen verleitet werden"
    reference = "SR 241 Art. 4 Bst. c"


class verleitung_widerruf_konsumkredit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Konsument zum Widerruf eines Konsumkreditvertrags verleitet wird"
    reference = "SR 241 Art. 4 Bst. d"


class verleitung_vertragsverletzung_unlauter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob unlautere Verleitung zu Vertragsverletzung nach Art. 4 vorliegt"
    reference = "SR 241 Art. 4"

    def formula(person, period, parameters):
        return (
            person('verleitung_vertragsbruch', period)
            + person('verleitung_geheimnisverrat', period)
            + person('verleitung_widerruf_konsumkredit', period)
        ) > 0
