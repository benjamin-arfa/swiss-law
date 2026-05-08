"""SR 952.0 Art. 1, 1a, 1b

Generated from: ch/952/de/952.0.md

Geltungsbereich und Definition Bank / Innovationsfoerderung:
- Art. 1: Gesetz gilt fuer Banken, Privatbankiers, Sparkassen.
  Keine gewerbsmaessige Entgegennahme von Publikumseinlagen ohne
  Bankbewilligung. Ausdruck "Bank" nur fuer bewilligte Institute.
- Art. 1a: Als Bank gilt, wer hauptsaechlich im Finanzbereich taetig
  ist und: (a) gewerbsmaessig Publikumseinlagen >100 Mio. CHF
  entgegennimmt; (b) bis 100 Mio. CHF und anlegt/verzinst; oder
  (c) sich bei Banken refinanziert.
- Art. 1b: Innovationsfoerderung: Einlagen bis 100 Mio. CHF, weder
  angelegt noch verzinst. Schwellenueberschreitung: Meldung innert
  10 Tagen, Bewilligungsgesuch innert 90 Tagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class bankg_ist_hauptsaechlich_im_finanzbereich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut ist hauptsaechlich im Finanzbereich taetig"
    reference = "SR 952.0 Art. 1a"


class bankg_publikumseinlagen_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der entgegengenommenen Publikumseinlagen (CHF)"
    reference = "SR 952.0 Art. 1a"


class bankg_nimmt_gewerbsmaessig_einlagen_entgegen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut nimmt gewerbsmaessig Publikumseinlagen entgegen"
    reference = "SR 952.0 Art. 1a"


class bankg_legt_einlagen_an_oder_verzinst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut legt Einlagen an oder verzinst sie"
    reference = "SR 952.0 Art. 1a lit. b"


class bankg_refinanziert_bei_banken(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut refinanziert sich in erheblichem Umfang bei Banken"
    reference = "SR 952.0 Art. 1a lit. c"


class bankg_ist_bank(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut gilt als Bank nach Art. 1a BankG"
    reference = "SR 952.0 Art. 1a"

    def formula_2019(person, period, parameters):
        import numpy as np

        im_finanzbereich = person('bankg_ist_hauptsaechlich_im_finanzbereich', period)
        einlagen = person('bankg_publikumseinlagen_betrag', period)
        gewerbsmaessig = person('bankg_nimmt_gewerbsmaessig_einlagen_entgegen', period)
        anlegt = person('bankg_legt_einlagen_an_oder_verzinst', period)
        refinanziert = person('bankg_refinanziert_bei_banken', period)

        p = parameters(period).sr952_0
        schwelle = p.publikumseinlagen_schwelle  # 100'000'000

        # lit. a: >100 Mio gewerbsmaessig
        lit_a = gewerbsmaessig * (einlagen > schwelle)
        # lit. b: bis 100 Mio, anlegen/verzinsen
        lit_b = gewerbsmaessig * (einlagen <= schwelle) * anlegt
        # lit. c: Refinanzierung bei Banken
        lit_c = refinanziert

        return im_finanzbereich * (lit_a + lit_b + lit_c)


class bankg_ist_innovationsfoerderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut faellt unter Innovationsfoerderung (Art. 1b BankG)"
    reference = "SR 952.0 Art. 1b"

    def formula_2019(person, period, parameters):
        import numpy as np

        im_finanzbereich = person('bankg_ist_hauptsaechlich_im_finanzbereich', period)
        einlagen = person('bankg_publikumseinlagen_betrag', period)
        gewerbsmaessig = person('bankg_nimmt_gewerbsmaessig_einlagen_entgegen', period)
        anlegt = person('bankg_legt_einlagen_an_oder_verzinst', period)

        p = parameters(period).sr952_0
        schwelle = p.publikumseinlagen_schwelle  # 100'000'000

        return (
            im_finanzbereich
            * gewerbsmaessig
            * (einlagen <= schwelle)
            * np.logical_not(anlegt)
        )


class bankg_innovationsfoerderung_schwelle_ueberschritten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwelle von 100 Mio. CHF ueberschritten (Meldepflicht)"
    reference = "SR 952.0 Art. 1b Abs. 6"

    def formula_2019(person, period, parameters):
        einlagen = person('bankg_publikumseinlagen_betrag', period)
        p = parameters(period).sr952_0
        schwelle = p.publikumseinlagen_schwelle
        return einlagen > schwelle


class bankg_meldung_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Meldung an FINMA bei Schwellenueberschreitung (Tage)"
    reference = "SR 952.0 Art. 1b Abs. 6"

    def formula_2019(person, period, parameters):
        import numpy as np

        p = parameters(period).sr952_0
        return np.full(person.count, p.meldung_frist_tage)


class bankg_bewilligungsgesuch_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Bewilligungsgesuch bei Schwellenueberschreitung (Tage)"
    reference = "SR 952.0 Art. 1b Abs. 6"

    def formula_2019(person, period, parameters):
        import numpy as np

        p = parameters(period).sr952_0
        return np.full(person.count, p.bewilligungsgesuch_frist_tage)
