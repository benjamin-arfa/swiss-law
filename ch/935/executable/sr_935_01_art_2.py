"""SR 935.01 Art. 2

Generated from: ch/935/de/935.01.md

Meldepflicht:
- Dienstleistungserbringer müssen dem SBFI vor Aufnahme der beruflichen
  Tätigkeit in der Schweiz Meldung erstatten.
- Form, Inhalt und Periodizität durch Bundesrat geregelt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_meldung_erstattet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob dem SBFI Meldung erstattet wurde"
    reference = "SR 935.01 Art. 2 Abs. 1"


class meldepflicht_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Meldepflicht nach BGMD erfüllt ist"
    reference = "SR 935.01 Art. 2"

    def formula(person, period, parameters):
        unterliegt = person('unterliegt_bgmd', period)
        gemeldet = person('hat_meldung_erstattet', period)
        # Meldepflicht gilt nur für BGMD-Unterliegende
        # Erfüllt wenn gemeldet ODER nicht unterliegend
        return gemeldet + (1 - unterliegt)
