"""SR 952.0 Art. 3, 3a

Generated from: ch/952/de/952.0.md

Bewilligung zum Geschaeftsbetrieb und Kantonalbanken:
- Art. 3: Bewilligungsvoraussetzungen: Statuten, Mindestkapital,
  guter Ruf, qualifizierte Beteiligung >=10%, Wohnsitz.
  Meldepflicht bei Erwerb/Veraenderung qualifizierter Beteiligung
  (Schwellen 20%, 33%, 50%).
- Art. 3a: Kantonalbank: kantonaler Erlass; Kanton haelt >1/3 Kapital
  und >1/3 Stimmen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class bankg_hat_statuten_und_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bank hat Statuten mit Geschaeftskreis und Verwaltungsorganisation"
    reference = "SR 952.0 Art. 3 Abs. 2 lit. a"


class bankg_mindestkapital_einbezahlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bank weist voll einbezahltes Mindestkapital aus"
    reference = "SR 952.0 Art. 3 Abs. 2 lit. b"


class bankg_guter_ruf_geschaeftsfuehrung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Geschaeftsfuehrung geniesst guten Ruf und bietet Gewaehr"
    reference = "SR 952.0 Art. 3 Abs. 2 lit. c"


class bankg_qualifizierte_beteiligung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoehe der qualifizierten Beteiligung an der Bank (Prozent)"
    reference = "SR 952.0 Art. 3 Abs. 2 lit. cbis"


class bankg_hat_qualifizierte_beteiligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person haelt qualifizierte Beteiligung (>=10%) an einer Bank"
    reference = "SR 952.0 Art. 3 Abs. 2 lit. cbis"

    def formula(person, period, parameters):
        beteiligung = person('bankg_qualifizierte_beteiligung_prozent', period)
        p = parameters(period).sr952_0
        schwelle = p.qualifizierte_beteiligung_schwelle  # 10.0
        return beteiligung >= schwelle


class bankg_meldepflichtige_schwelle_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Meldepflichtige Beteiligungsschwelle erreicht (20%, 33%, 50%)"
    reference = "SR 952.0 Art. 3 Abs. 5"

    def formula(person, period, parameters):
        beteiligung = person('bankg_qualifizierte_beteiligung_prozent', period)
        # Schwellen: 20, 33, 50 Prozent
        return (beteiligung >= 20) + (beteiligung >= 33) + (beteiligung >= 50)


class bankg_bewilligungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bank erfuellt alle Bewilligungsvoraussetzungen nach Art. 3"
    reference = "SR 952.0 Art. 3"

    def formula(person, period, parameters):
        return (
            person('bankg_hat_statuten_und_organisation', period)
            * person('bankg_mindestkapital_einbezahlt', period)
            * person('bankg_guter_ruf_geschaeftsfuehrung', period)
        )


class bankg_ist_kantonalbank(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut ist Kantonalbank (Art. 3a)"
    reference = "SR 952.0 Art. 3a"


class bankg_kanton_kapitalbeteiligung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kapitalbeteiligung des Kantons an der Bank (Prozent)"
    reference = "SR 952.0 Art. 3a"


class bankg_kanton_stimmenanteil_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Stimmenanteil des Kantons an der Bank (Prozent)"
    reference = "SR 952.0 Art. 3a"


class bankg_erfuellt_kantonalbank_kriterien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Erfuellt Kantonalbank-Kriterien: Kanton >1/3 Kapital und >1/3 Stimmen"
    reference = "SR 952.0 Art. 3a"

    def formula(person, period, parameters):
        kapital = person('bankg_kanton_kapitalbeteiligung_prozent', period)
        stimmen = person('bankg_kanton_stimmenanteil_prozent', period)
        p = parameters(period).sr952_0
        min_anteil = p.kantonalbank_min_beteiligung  # 33.33

        return (kapital > min_anteil) * (stimmen > min_anteil)
