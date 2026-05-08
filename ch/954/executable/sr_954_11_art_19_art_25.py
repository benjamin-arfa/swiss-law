"""SR 954.11 Art. 19, 25

Generated from: ch/954/de/954.11.md

Gewerbsmaessigkeit und qualifizierte Geschaeftsfuehrung bei
Vermoegensverwaltern und Trustees:
- Art. 19: Gewerbsmaessig wenn: (a) Bruttoertrag >50'000 CHF/Jahr;
  (b) >20 Geschaeftsbeziehungen/Jahr; oder (c) Verfuegungsmacht >5 Mio. CHF.
- Art. 25: Qualifizierte Geschaeftsfuehrer: 5 Jahre Berufserfahrung
  und 40 Stunden Ausbildung. Regelmaessige Fortbildung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class finiv_vv_bruttoertrag_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Jaehrlicher Bruttoertrag Vermoegensverwalter/Trustee (CHF)"
    reference = "SR 954.11 Art. 19 Abs. 1 lit. a"


class finiv_vv_anzahl_geschaeftsbeziehungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Geschaeftsbeziehungen pro Jahr"
    reference = "SR 954.11 Art. 19 Abs. 1 lit. b"


class finiv_vv_verfuegungsmacht_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoechstbetrag fremder Vermoegenswerte unter Verfuegungsmacht (CHF)"
    reference = "SR 954.11 Art. 19 Abs. 1 lit. c"


class finiv_vv_gewerbsmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vermoegensverwalter/Trustee ist gewerbsmaessig taetig (Art. 19)"
    reference = "SR 954.11 Art. 19"

    def formula_2020(person, period, parameters):
        ertrag = person('finiv_vv_bruttoertrag_jaehrlich', period)
        beziehungen = person('finiv_vv_anzahl_geschaeftsbeziehungen', period)
        verfuegungsmacht = person('finiv_vv_verfuegungsmacht_betrag', period)

        p = parameters(period).sr954_11
        return (
            (ertrag > p.vv_gewerbsmaessigkeit_ertrag)
            + (beziehungen > p.vv_gewerbsmaessigkeit_beziehungen)
            + (verfuegungsmacht > p.vv_gewerbsmaessigkeit_verfuegungsmacht)
        )


class finiv_gf_berufserfahrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Jahre Berufserfahrung des qualifizierten Geschaeftsfuehrers"
    reference = "SR 954.11 Art. 25 Abs. 1 lit. a"


class finiv_gf_ausbildung_stunden(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Stunden Ausbildung des qualifizierten Geschaeftsfuehrers"
    reference = "SR 954.11 Art. 25 Abs. 1 lit. b"


class finiv_gf_qualifiziert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Geschaeftsfuehrer erfuellt Qualifikationsanforderungen (Art. 25)"
    reference = "SR 954.11 Art. 25"

    def formula_2020(person, period, parameters):
        erfahrung = person('finiv_gf_berufserfahrung_jahre', period)
        ausbildung = person('finiv_gf_ausbildung_stunden', period)

        p = parameters(period).sr954_11
        return (
            (erfahrung >= p.gf_min_berufserfahrung_jahre)
            * (ausbildung >= p.gf_min_ausbildung_stunden)
        )
