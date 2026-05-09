"""SR 232.119 Art. 2a

Generated from: ch/232/de/232.119.md

Art. 2a defines the criteria for a watch component to qualify as
"Swiss" (schweizerischer Bestandteil).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bestandteil_in_schweiz_kontrolliert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Der Bestandteil wird durch den Hersteller in der Schweiz kontrolliert"
    reference = "SR 232.119 Art. 2a lit. a"


class herstellungskosten_anteil_schweiz_bestandteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Herstellungskosten des Bestandteils, die in der Schweiz anfallen (0-1)"
    reference = "SR 232.119 Art. 2a lit. b"


class ist_schweizerischer_bestandteil(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Der Bestandteil gilt als schweizerisch im Sinne von SR 232.119 Art. 2a"
    reference = "SR 232.119 Art. 2a"

    def formula(person, period, parameters):
        kontrolliert = person('bestandteil_in_schweiz_kontrolliert', period)
        kosten_anteil = person('herstellungskosten_anteil_schweiz_bestandteil', period)

        # Art. 2a lit. b: mindestens 60% der Herstellungskosten in der Schweiz
        kosten_ok = kosten_anteil >= 0.60

        return kontrolliert * kosten_ok
