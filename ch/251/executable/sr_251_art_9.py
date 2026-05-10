"""SR 251 Art. 9

Generated from: ch/de/251.md

Merger notification duty: required when combined turnover exceeds
CHF 2 billion globally or CHF 500 million in Switzerland, and at
least two participating enterprises each have Swiss turnover of
at least CHF 100 million.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsatz_gesamt_milliarden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtumsatz der beteiligten Unternehmen in Milliarden CHF"
    reference = "SR 251 Art. 9 Abs. 1 Bst. a"


class umsatz_schweiz_millionen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Auf die Schweiz entfallender Gesamtumsatz in Millionen CHF"
    reference = "SR 251 Art. 9 Abs. 1 Bst. a"


class mindestens_zwei_unternehmen_100mio(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob mindestens zwei beteiligte Unternehmen je CHF 100 Mio. Umsatz in der Schweiz erzielen"
    reference = "SR 251 Art. 9 Abs. 1 Bst. b"


class unternehmen_mit_marktbeherrschung_beteiligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Unternehmen mit festgestellter marktbeherrschender Stellung beteiligt ist"
    reference = "SR 251 Art. 9 Abs. 4"


class meldepflicht_zusammenschluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Meldepflicht fuer den Zusammenschluss besteht"
    reference = "SR 251 Art. 9"

    def formula(person, period, parameters):
        umsatz_global = person('umsatz_gesamt_milliarden', period) >= 2.0
        umsatz_ch = person('umsatz_schweiz_millionen', period) >= 500.0
        schwelle_a = (umsatz_global + umsatz_ch) > 0
        schwelle_b = person('mindestens_zwei_unternehmen_100mio', period)
        umsatz_pflicht = schwelle_a * schwelle_b
        marktbeherrschung = person('unternehmen_mit_marktbeherrschung_beteiligt', period)
        return (umsatz_pflicht + marktbeherrschung) > 0
