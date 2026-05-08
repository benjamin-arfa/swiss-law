"""SR 954.11 Art. 13

Generated from: ch/954/de/954.11.md

Gewaehr und qualifizierte Beteiligung bei Finanzinstituten:
- Art. 13: Bewilligungsgesuch muss Angaben zu natuerlichen Personen
  (Nationalitaet, Wohnsitz, Lebenslauf, Strafregister, Betreibungsregister)
  und zu Gesellschaften (Statuten, HR-Auszug, Geschaeftstaetigkeiten)
  enthalten.
- Qualifizierte Beteiligung: >=10% Kapital/Stimmen.
  Wertpapierhaeuser: Meldung innert 60 Tagen nach Geschaeftsjahresende.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class finiv_qualifizierte_beteiligung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Beteiligung am Finanzinstitut (Prozent Kapital/Stimmen)"
    reference = "SR 954.11 Art. 13 Abs. 5"


class finiv_hat_qualifizierte_beteiligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person haelt qualifizierte Beteiligung (>=10%)"
    reference = "SR 954.11 Art. 13 Abs. 5"

    def formula_2020(person, period, parameters):
        beteiligung = person('finiv_qualifizierte_beteiligung_prozent', period)
        p = parameters(period).sr954_11
        return beteiligung >= p.qualifizierte_beteiligung_schwelle


class finiv_guter_ruf_geschaeftsfuehrung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person geniesst guten Ruf und bietet Gewaehr (Art. 13)"
    reference = "SR 954.11 Art. 13 Abs. 2"


class finiv_bewilligungsgesuch_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bewilligungsgesuch enthaelt alle erforderlichen Angaben"
    reference = "SR 954.11 Art. 13"


class finiv_wph_meldepflicht_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Meldung qualifizierter Beteiligungen (Tage nach GJ-Ende)"
    reference = "SR 954.11 Art. 13 Abs. 4"

    def formula_2020(person, period, parameters):
        import numpy as np

        p = parameters(period).sr954_11
        return np.full(person.count, p.wph_meldepflicht_frist_tage)
