"""SR 921.552.1 Art. 12

Generated from: ch/921/de/921.552.1.md

Warenbuchhaltung in Forstbaumschulen und Forstgaerten: Eingang, Vorraete,
Herkunftsblatt und Situationsplan.
Unterlagen 5 Jahre ueber Verkauf hinaus aufbewahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class forstbaumschulen_aufbewahrungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Warenbuchhaltung Forstbaumschulen (Jahre)"
    reference = "SR 921.552.1 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        return 5
