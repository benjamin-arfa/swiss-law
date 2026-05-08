"""AG 290.100 § 17

Generated from: ch/ag/de/290.100.md

§ 17 Titelschutz: Using the title of lawyer (Fuersprecher, Rechtsanwalt,
Anwalt, Advokat, or similar misleading title) without a certificate of
competence is punishable by a fine of up to CHF 20,000.
Patent attorneys are exempt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_titelschutz_verletzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Verwendung des Anwaltstitels ohne Faehigkeitsausweis (AG 290.100 § 17 Abs. 1)"
    reference = "AG 290.100 § 17 Abs. 1"


class ag_ist_patentanwalt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ist Patentanwalt (ausgenommen von Titelschutz, AG 290.100 § 17 Abs. 2)"
    reference = "AG 290.100 § 17 Abs. 2"


class ag_titelschutz_busse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Busse wegen Titelschutzverletzung in CHF (AG 290.100 § 17)"
    reference = "AG 290.100 § 17 Abs. 1"

    def formula(person, period, parameters):
        verletzung = person('ag_titelschutz_verletzung', period)
        patentanwalt = person('ag_ist_patentanwalt', period.this_year)
        faehigkeitsausweis = person('ag_faehigkeitsausweis_erhalten', period.this_year)
        # Fine up to 20'000 if title used without certificate (unless patent attorney)
        strafbar = verletzung * (faehigkeitsausweis == 0) * (patentanwalt == 0)
        # Actual fine is discretionary; we model max possible
        return strafbar * 20000
