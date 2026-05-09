"""SR 232.119 Art. 1a

Generated from: ch/232/de/232.119.md

Art. 1a defines the criteria for a watch to qualify as a "Swiss watch"
(Schweizer Uhr). All conditions (a-d) must be met.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_ausschliesslich_mechanische_uhr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Uhr ist ausschliesslich mechanisch"
    reference = "SR 232.119 Art. 1a lit. a"


class technische_entwicklung_uhr_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die technische Entwicklung der Uhr wurde in der Schweiz vorgenommen"
    reference = "SR 232.119 Art. 1a lit. a"


class werk_ist_schweizerisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrwerk ist schweizerisch im Sinne von Art. 2"
    reference = "SR 232.119 Art. 1a lit. abis"


class werk_in_schweiz_eingeschalt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Werk wurde in der Schweiz eingeschalt"
    reference = "SR 232.119 Art. 1a lit. b"


class endkontrolle_uhr_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Der Hersteller fuehrt die Endkontrolle der Uhr in der Schweiz durch"
    reference = "SR 232.119 Art. 1a lit. c"


class herstellungskosten_anteil_schweiz_uhr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Herstellungskosten der Uhr, die in der Schweiz anfallen (0-1)"
    reference = "SR 232.119 Art. 1a lit. d"


class ist_schweizer_uhr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Uhr gilt als Schweizer Uhr im Sinne von SR 232.119 Art. 1a"
    reference = "SR 232.119 Art. 1a"

    def formula(person, period, parameters):
        # All four conditions must be met cumulatively
        tech_ok = person('technische_entwicklung_uhr_in_schweiz', period)
        werk_ch = person('werk_ist_schweizerisch', period)
        eingeschalt = person('werk_in_schweiz_eingeschalt', period)
        endkontrolle = person('endkontrolle_uhr_in_schweiz', period)
        kosten_anteil = person('herstellungskosten_anteil_schweiz_uhr', period)

        # Art. 1a lit. d: mindestens 60% der Herstellungskosten in der Schweiz
        kosten_ok = kosten_anteil >= 0.60

        return tech_ok * werk_ch * eingeschalt * endkontrolle * kosten_ok
