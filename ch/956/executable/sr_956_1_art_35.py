"""SR 956.1 Art. 35

Generated from: ch/956/de/956.1.md

Einziehung von Gewinnen:
- FINMA kann Gewinn einziehen bei schwerer Verletzung
- Gilt auch für vermiedene Verluste
- Schätzung möglich wenn Umfang nicht ermittelbar
- Verjährung nach 7 Jahren
- Strafrechtliche Einziehung geht vor
- Eingezogene Vermögenswerte an den Bund (soweit nicht Geschädigten ausbezahlt)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class erzielter_gewinn_durch_verletzung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erzielter Gewinn durch schwere Verletzung aufsichtsrechtlicher Bestimmungen in CHF"
    reference = "SR 956.1 Art. 35 Abs. 1"


class vermiedener_verlust_durch_verletzung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermiedener Verlust durch schwere Verletzung in CHF"
    reference = "SR 956.1 Art. 35 Abs. 2"


class jahre_seit_verletzung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit der schweren Verletzung"
    reference = "SR 956.1 Art. 35 Abs. 4"


class strafrechtliche_einziehung_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob bereits eine strafrechtliche Einziehung nach StGB Art. 70-72 erfolgt ist"
    reference = "SR 956.1 Art. 35 Abs. 5"


class einziehung_nicht_verjaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht zur Einziehung noch nicht verjährt ist"
    reference = "SR 956.1 Art. 35 Abs. 4"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_verletzung', period)
        verjaehrung = parameters(period).sr_956_1.verjaehrungsfrist_einziehung_jahre
        return jahre < verjaehrung


class einziehungsbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einzuziehender Betrag in CHF (Gewinn oder vermiedener Verlust)"
    reference = "SR 956.1 Art. 35"

    def formula(person, period, parameters):
        import numpy as np
        gewinn = person('erzielter_gewinn_durch_verletzung', period)
        vermieden = person('vermiedener_verlust_durch_verletzung', period)
        schwer = person('schwere_verletzung_aufsichtsrecht', period)
        nicht_verjaehrt = person('einziehung_nicht_verjaehrt', period)
        straf = person('strafrechtliche_einziehung_erfolgt', period)

        betrag = np.maximum(gewinn, vermieden)
        return betrag * schwer * nicht_verjaehrt * (straf == False)
