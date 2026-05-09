"""SR 952.02 Art. 6 — Gewerbsmaessigkeit

Generated from: ch/952/de/952.02.md

Abs. 1: Gewerbsmaessig handelt, wer:
  a) dauernd mehr als 20 Publikumseinlagen/kryptobasierte Vermoegenswerte
     entgegennimmt; oder
  b) sich oeffentlich dafuer empfiehlt (auch wenn <20 entgegengenommen).

Abs. 2: Nicht gewerbsmaessig, wer >20 entgegennimmt/empfiehlt, wenn:
  a) Einlagen von hoechstens 1 Mio. CHF;
  b) kein Zinsdifferenzgeschaeft;
  c) schriftliche Information ueber: 1) keine FINMA-Aufsicht,
     2) keine Einlagensicherung.

Abs. 4: Bei Schwellenueberschreitung (>1 Mio. CHF):
  Meldung an FINMA innert 10 Tagen, Bewilligungsgesuch innert 30 Tagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class bankv_anzahl_publikumseinlagen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl entgegengenommener Publikumseinlagen/kryptobasierter Vermoegenswerte"
    reference = "SR 952.02 Art. 6 Abs. 1 lit. a"


class bankv_empfiehlt_sich_oeffentlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Empfiehlt sich oeffentlich zur Entgegennahme von Publikumseinlagen"
    reference = "SR 952.02 Art. 6 Abs. 1 lit. b"


class bankv_einlagen_gesamtbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtbetrag entgegengenommener Einlagen (CHF)"
    reference = "SR 952.02 Art. 6 Abs. 2 lit. a"


class bankv_betreibt_zinsdifferenzgeschaeft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut betreibt Zinsdifferenzgeschaeft"
    reference = "SR 952.02 Art. 6 Abs. 2 lit. b"


class bankv_einleger_schriftlich_informiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einleger schriftlich informiert ueber fehlende Aufsicht und Einlagensicherung"
    reference = "SR 952.02 Art. 6 Abs. 2 lit. c"


class bankv_ist_gewerbsmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut handelt gewerbsmaessig i.S.d. BankG"
    reference = "SR 952.02 Art. 6"

    def formula_2017(person, period, parameters):
        import numpy as np

        p = parameters(period).sr952_02
        schwelle_anzahl = p.gewerbsmaessig_schwelle_anzahl  # 20
        schwelle_betrag = p.gewerbsmaessig_schwelle_betrag  # 1'000'000

        anzahl = person('bankv_anzahl_publikumseinlagen', period)
        empfiehlt = person('bankv_empfiehlt_sich_oeffentlich', period)
        betrag = person('bankv_einlagen_gesamtbetrag', period)
        zinsdiff = person('bankv_betreibt_zinsdifferenzgeschaeft', period)
        informiert = person('bankv_einleger_schriftlich_informiert', period)

        # Abs. 1: grundsaetzlich gewerbsmaessig
        grundsaetzlich = (anzahl > schwelle_anzahl) + empfiehlt

        # Abs. 2: Ausnahme — nicht gewerbsmaessig wenn alle Bedingungen erfuellt
        ausnahme = (
            (betrag <= schwelle_betrag)
            * np.logical_not(zinsdiff)
            * informiert
        )

        return (grundsaetzlich >= 1) * np.logical_not(ausnahme)


class bankv_gewerbsmaessig_schwelle_ueberschritten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwellenwert von 1 Mio. CHF fuer Nicht-Gewerbsmaessigkeit ueberschritten"
    reference = "SR 952.02 Art. 6 Abs. 4"

    def formula_2019(person, period, parameters):
        p = parameters(period).sr952_02
        betrag = person('bankv_einlagen_gesamtbetrag', period)
        return betrag > p.gewerbsmaessig_schwelle_betrag


class bankv_meldepflicht_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer FINMA-Meldung bei Schwellenueberschreitung (Tage)"
    reference = "SR 952.02 Art. 6 Abs. 4"

    def formula_2019(person, period, parameters):
        import numpy as np

        p = parameters(period).sr952_02
        return np.full(person.count, p.meldepflicht_frist_tage)


class bankv_bewilligungsgesuch_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Bewilligungsgesuch bei Schwellenueberschreitung (Tage)"
    reference = "SR 952.02 Art. 6 Abs. 4"

    def formula_2019(person, period, parameters):
        import numpy as np

        p = parameters(period).sr952_02
        return np.full(person.count, p.bewilligungsgesuch_frist_tage)
