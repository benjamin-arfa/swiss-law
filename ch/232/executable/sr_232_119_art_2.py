"""SR 232.119 Art. 2

Generated from: ch/232/de/232.119.md

Art. 2 defines the criteria for a watch movement to qualify as
"Swiss" (schweizerisches Uhrwerk).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class technische_entwicklung_werk_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die technische Entwicklung des Uhrwerks wurde in der Schweiz vorgenommen"
    reference = "SR 232.119 Art. 2 Abs. 1 lit. a"


class werk_in_schweiz_zusammengesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrwerk wurde in der Schweiz zusammengesetzt"
    reference = "SR 232.119 Art. 2 Abs. 1 lit. abis"


class werk_in_schweiz_kontrolliert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrwerk wird durch den Hersteller in der Schweiz kontrolliert"
    reference = "SR 232.119 Art. 2 Abs. 1 lit. b"


class herstellungskosten_anteil_schweiz_werk(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Herstellungskosten des Werks, die in der Schweiz anfallen (0-1)"
    reference = "SR 232.119 Art. 2 Abs. 1 lit. bbis"


class wertanteil_bestandteile_schweiz_werk(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wertanteil der Bestandteile schweizerischer Fabrikation am Gesamtwert aller Bestandteile (0-1)"
    reference = "SR 232.119 Art. 2 Abs. 1 lit. c"


class ist_schweizerisches_uhrwerk(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrwerk gilt als schweizerisch im Sinne von SR 232.119 Art. 2"
    reference = "SR 232.119 Art. 2"

    def formula(person, period, parameters):
        # All conditions must be met cumulatively (Abs. 1 lit. a-c)
        tech_ok = person('technische_entwicklung_werk_in_schweiz', period)
        zusammengesetzt = person('werk_in_schweiz_zusammengesetzt', period)
        kontrolliert = person('werk_in_schweiz_kontrolliert', period)
        kosten_anteil = person('herstellungskosten_anteil_schweiz_werk', period)
        wertanteil = person('wertanteil_bestandteile_schweiz_werk', period)

        # Abs. 1 lit. bbis: mindestens 60% Herstellungskosten in CH
        kosten_ok = kosten_anteil >= 0.60

        # Abs. 1 lit. c: mindestens 50% Wertanteil CH-Bestandteile
        wert_ok = wertanteil >= 0.50

        return tech_ok * zusammengesetzt * kontrolliert * kosten_ok * wert_ok
