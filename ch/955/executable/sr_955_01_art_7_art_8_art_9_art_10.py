"""SR 955.01 Art. 7–10

Generated from: ch/955/de/955.01.md

Berufmaessigkeit der Finanzintermediaere:
- Art. 7: Allgemeine Kriterien fuer berufmaessige Taetigkeit:
  (a) Bruttoerloes >50'000 CHF/Jahr; (b) >20 Geschaeftsbeziehungen/Jahr;
  (c) Verfuegungsmacht ueber >5 Mio. CHF; (d) Transaktionsvolumen >2 Mio. CHF/Jahr.
  Nahestehende Personen: nur bei Erloes >50'000 CHF.
- Art. 8: Kreditgeschaeft: berufmaessig bei Erloes >250'000 CHF UND
  Kreditvolumen >5 Mio. CHF.
- Art. 9: Geld-/Wertuebertragung gilt immer als berufmaessig
  (Ausnahme: nahestehende Person, Erloes <=50'000 CHF).
- Art. 10: Handelstaetigkeit: Bruttogewinn statt Bruttoerloes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class gwv_bruttoerloes_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Jaehrlicher Bruttoerloes aus Finanzintermediation (CHF)"
    reference = "SR 955.01 Art. 7 Abs. 1 lit. a"


class gwv_anzahl_geschaeftsbeziehungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Geschaeftsbeziehungen pro Kalenderjahr"
    reference = "SR 955.01 Art. 7 Abs. 1 lit. b"


class gwv_verfuegungsmacht_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoechstbetrag fremder Vermoegenswerte unter Verfuegungsmacht (CHF)"
    reference = "SR 955.01 Art. 7 Abs. 1 lit. c"


class gwv_transaktionsvolumen_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Jaehrliches Transaktionsvolumen (CHF)"
    reference = "SR 955.01 Art. 7 Abs. 1 lit. d"


class gwv_ist_nahestehende_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertragspartei ist nahestehende Person (Art. 7 Abs. 5)"
    reference = "SR 955.01 Art. 7 Abs. 5"


class gwv_taetigkeit_berufmaessig_allgemein(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Taetigkeit ist berufmaessig nach allgemeinen Kriterien (Art. 7)"
    reference = "SR 955.01 Art. 7"

    def formula(person, period, parameters):
        import numpy as np

        erloes = person('gwv_bruttoerloes_jaehrlich', period)
        beziehungen = person('gwv_anzahl_geschaeftsbeziehungen', period)
        verfuegungsmacht = person('gwv_verfuegungsmacht_betrag', period)
        volumen = person('gwv_transaktionsvolumen_jaehrlich', period)
        nahestehend = person('gwv_ist_nahestehende_person', period)

        p = parameters(period).sr955_01

        # Art. 7 Abs. 1 Kriterien
        krit_a = erloes > p.berufmaessigkeit_bruttoerloes_schwelle  # 50'000
        krit_b = beziehungen > p.berufmaessigkeit_beziehungen_schwelle  # 20
        krit_c = verfuegungsmacht > p.berufmaessigkeit_verfuegungsmacht_schwelle  # 5'000'000
        krit_d = volumen > p.berufmaessigkeit_transaktionsvolumen_schwelle  # 2'000'000

        berufmaessig = krit_a + krit_b + krit_c + krit_d

        # Art. 7 Abs. 4: Nahestehende nur bei Erloes >50'000
        berufmaessig_nahestehend = erloes > p.berufmaessigkeit_bruttoerloes_schwelle

        return np.where(nahestehend, berufmaessig_nahestehend, berufmaessig)


class gwv_kredit_bruttoerloes(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Bruttoerloes aus Kreditgeschaeft (CHF/Jahr)"
    reference = "SR 955.01 Art. 8 Abs. 1 lit. a"


class gwv_kreditvolumen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vergebenes Kreditvolumen (CHF)"
    reference = "SR 955.01 Art. 8 Abs. 1 lit. b"


class gwv_kreditgeschaeft_berufmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kreditgeschaeft ist berufmaessig (Art. 8)"
    reference = "SR 955.01 Art. 8"

    def formula(person, period, parameters):
        erloes = person('gwv_kredit_bruttoerloes', period)
        volumen = person('gwv_kreditvolumen', period)

        p = parameters(period).sr955_01
        return (
            (erloes > p.kredit_berufmaessigkeit_erloes)  # 250'000
            * (volumen > p.kredit_berufmaessigkeit_volumen)  # 5'000'000
        )


class gwv_ist_geld_wertuebertragung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person betreibt Geld- oder Wertuebertragungsgeschaeft"
    reference = "SR 955.01 Art. 9"


class gwv_geld_wertuebertragung_berufmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Geld-/Wertuebertragung ist berufmaessig (Art. 9)"
    reference = "SR 955.01 Art. 9"

    def formula(person, period, parameters):
        import numpy as np

        ist_gwu = person('gwv_ist_geld_wertuebertragung', period)
        nahestehend = person('gwv_ist_nahestehende_person', period)
        erloes = person('gwv_bruttoerloes_jaehrlich', period)

        p = parameters(period).sr955_01
        schwelle = p.berufmaessigkeit_bruttoerloes_schwelle  # 50'000

        # Immer berufmaessig, ausser nahestehend UND Erloes <= 50'000
        ausnahme = nahestehend * (erloes <= schwelle)
        return ist_gwu * np.logical_not(ausnahme)


class gwv_bruttogewinn_handel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Bruttogewinn aus Handelstaetigkeit (CHF/Jahr)"
    reference = "SR 955.01 Art. 10"


class gwv_handelstaetigkeit_berufmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Handelstaetigkeit ist berufmaessig (Art. 10)"
    reference = "SR 955.01 Art. 10"

    def formula(person, period, parameters):
        gewinn = person('gwv_bruttogewinn_handel', period)
        p = parameters(period).sr955_01
        # Art. 10: Bruttogewinn statt Bruttoerloes
        return gewinn > p.berufmaessigkeit_bruttoerloes_schwelle
