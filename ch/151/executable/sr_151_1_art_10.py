"""SR 151.1 Art. 10

Generated from: ch/151/de/151.1.md

Kuendigungsschutz: Schutz waehrend Beschwerde-/Schlichtungs-/
Gerichtsverfahren und 6 Monate darueber hinaus.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class innerbetriebliche_beschwerde_haengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein innerbetriebliches Beschwerdeverfahren haengig ist"
    reference = "SR 151.1 Art. 10 Abs. 2"


class schlichtungsverfahren_haengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Schlichtungsverfahren haengig ist"
    reference = "SR 151.1 Art. 10 Abs. 2"


class gerichtsverfahren_haengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Gerichtsverfahren haengig ist"
    reference = "SR 151.1 Art. 10 Abs. 2"


class monate_seit_verfahrensende(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit Ende des Verfahrens"
    reference = "SR 151.1 Art. 10 Abs. 2"


class kuendigungsschutz_glg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Kuendigungsschutz nach GlG Art. 10 besteht"
    reference = "SR 151.1 Art. 10"

    def formula(person, period, parameters):
        beschwerde = person('innerbetriebliche_beschwerde_haengig', period)
        schlichtung = person('schlichtungsverfahren_haengig', period)
        gericht = person('gerichtsverfahren_haengig', period)
        monate = person('monate_seit_verfahrensende', period)
        verfahren_aktiv = beschwerde + schlichtung + gericht > 0
        nachlaufschutz = monate < 6
        return verfahren_aktiv + nachlaufschutz > 0
