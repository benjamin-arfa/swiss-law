"""SR 837.0 Art. 10

Generated from: ch/837/de/837.0.md

Art. 10: Arbeitslosigkeit (Definition of unemployment)
- Abs. 1: Wholly unemployed = not in any employment relationship and seeking
  full-time work.
- Abs. 2: Partially unemployed:
  a. not in any employment and seeking only part-time work, or
  b. has part-time work and seeks full-time or additional part-time work.
- Abs. 2bis: Not partially unemployed if normal working hours are temporarily
  reduced (short-time work).
- Abs. 3: The job-seeker is only considered unemployed once registered for
  job placement.
- Abs. 4: Provisional suspension in a public-law employment relationship
  (pending appeal with suspensive effect) is equivalent to unemployment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_in_arbeitsverhaeltnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Steht in einem Arbeitsverhaeltnis"
    reference = "SR 837.0 Art. 10 Abs. 1"


class alv_sucht_vollzeitbeschaeftigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Sucht eine Vollzeitbeschaeftigung"
    reference = "SR 837.0 Art. 10 Abs. 1"


class alv_sucht_teilzeitbeschaeftigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Sucht eine Teilzeitbeschaeftigung"
    reference = "SR 837.0 Art. 10 Abs. 2"


class alv_hat_teilzeitbeschaeftigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hat eine Teilzeitbeschaeftigung"
    reference = "SR 837.0 Art. 10 Abs. 2 Bst. b"


class alv_zur_arbeitsvermittlung_angemeldet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Zur Arbeitsvermittlung angemeldet"
    reference = "SR 837.0 Art. 10 Abs. 3"


class alv_kurzarbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Normale Arbeitszeit voruebergehend verkuerzt (Kurzarbeit)"
    reference = "SR 837.0 Art. 10 Abs. 2bis"


class alv_ganz_arbeitslos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ganz arbeitslos im Sinne von Art. 10 Abs. 1 AVIG"
    reference = "SR 837.0 Art. 10 Abs. 1, 3"

    def formula(person, period, parameters):
        kein_arbv = person('alv_in_arbeitsverhaeltnis', period) == False
        vollzeit = person('alv_sucht_vollzeitbeschaeftigung', period)
        angemeldet = person('alv_zur_arbeitsvermittlung_angemeldet', period)
        return kein_arbv * vollzeit * angemeldet


class alv_teilweise_arbeitslos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Teilweise arbeitslos im Sinne von Art. 10 Abs. 2 AVIG"
    reference = "SR 837.0 Art. 10 Abs. 2, 2bis, 3"

    def formula(person, period, parameters):
        kein_arbv = person('alv_in_arbeitsverhaeltnis', period) == False
        teilzeit_suche = person('alv_sucht_teilzeitbeschaeftigung', period)
        hat_teilzeit = person('alv_hat_teilzeitbeschaeftigung', period)
        vollzeit_suche = person('alv_sucht_vollzeitbeschaeftigung', period)
        angemeldet = person('alv_zur_arbeitsvermittlung_angemeldet', period)
        kurzarbeit = person('alv_kurzarbeit', period)

        # Case a: no employment, seeking part-time
        fall_a = kein_arbv * teilzeit_suche
        # Case b: has part-time, seeking full-time or additional part-time
        fall_b = hat_teilzeit * (vollzeit_suche + teilzeit_suche)

        # Must be registered and not in short-time work
        return (fall_a + fall_b) * angemeldet * (kurzarbeit == False)
