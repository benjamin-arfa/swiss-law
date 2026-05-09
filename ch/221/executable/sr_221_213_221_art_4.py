"""SR 221.213.221 Art. 4 – Abgeltung der Verpächterlasten

Generated from: ch/221/de/221.213.221.md

Die Abgeltung der Verpächterlasten setzt sich zusammen aus:
a) Boden: 1.1% des Ertragswertes
b) Ökonomiegebäude/Grundinfrastruktur: 6.5% des Ertragswertes für
   Abschreibungen + 29% des Mietwertes für Unterhalt/Versicherungen
c) Abschreibung auf Dauerkulturen
d) Betriebsleiterwohnung: 3.6% des Ertragswertes für Abschreibungen
   + 43% des Mietwertes für Unterhalt/Versicherungen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Rates from Art. 4 Abs. 1 (Fassung 2018)
BODEN_ABSCHREIBUNG_RATE = 0.011          # 1.1%
OEKONOMIE_ABSCHREIBUNG_RATE = 0.065      # 6.5%
OEKONOMIE_UNTERHALT_RATE = 0.29          # 29% of Mietwert
WOHNUNG_ABSCHREIBUNG_RATE = 0.036        # 3.6%
WOHNUNG_UNTERHALT_RATE = 0.43            # 43% of Mietwert


class ertragswert_boden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ertragswert des Bodens (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. a"


class ertragswert_oekonomiegebaeude(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ertragswert der Ökonomiegebäude und Grundinfrastruktur (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. b"


class mietwert_oekonomiegebaeude(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mietwert der Ökonomiegebäude (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. b"


class ertragswert_betriebsleiterwohnung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ertragswert der Betriebsleiterwohnung (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. d"


class mietwert_betriebsleiterwohnung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mietwert der Betriebsleiterwohnung (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. d"


class ertragswert_dauerkultur_vollertrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ertragswert der Dauerkultur im ersten Vollertragsjahr (ohne Boden, CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 2"


class gesamtnutzungsdauer_dauerkultur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtnutzungsdauer der Dauerkultur (Jahre)"
    reference = "SR 221.213.221 Art. 4 Abs. 2"


class erneuerung_obliegt_verpaechter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erneuerung der Dauerkultur obliegt dem Verpächter"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. c"


class abgeltung_verpaechterlasten_boden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abgeltung Verpächterlasten – Boden (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('ertragswert_boden', period) * BODEN_ABSCHREIBUNG_RATE


class abgeltung_verpaechterlasten_oekonomie(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abgeltung Verpächterlasten – Ökonomiegebäude (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. b"

    def formula(person, period, parameters):
        ertragswert = person('ertragswert_oekonomiegebaeude', period)
        mietwert = person('mietwert_oekonomiegebaeude', period)
        return ertragswert * OEKONOMIE_ABSCHREIBUNG_RATE + mietwert * OEKONOMIE_UNTERHALT_RATE


class abgeltung_verpaechterlasten_dauerkultur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abschreibung Dauerkulturen (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        ertragswert = person('ertragswert_dauerkultur_vollertrag', period)
        nutzungsdauer = person('gesamtnutzungsdauer_dauerkultur', period)
        obliegt_verpaechter = person('erneuerung_obliegt_verpaechter', period)

        abschreibung = np.where(nutzungsdauer > 0, ertragswert / nutzungsdauer, 0)
        return np.where(obliegt_verpaechter, abschreibung, 0)


class abgeltung_verpaechterlasten_wohnung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abgeltung Verpächterlasten – Betriebsleiterwohnung (CHF)"
    reference = "SR 221.213.221 Art. 4 Abs. 1 lit. d"

    def formula(person, period, parameters):
        ertragswert = person('ertragswert_betriebsleiterwohnung', period)
        mietwert = person('mietwert_betriebsleiterwohnung', period)
        return ertragswert * WOHNUNG_ABSCHREIBUNG_RATE + mietwert * WOHNUNG_UNTERHALT_RATE


class abgeltung_verpaechterlasten_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total Abgeltung der Verpächterlasten (CHF)"
    reference = "SR 221.213.221 Art. 4"

    def formula(person, period, parameters):
        boden = person('abgeltung_verpaechterlasten_boden', period)
        oekonomie = person('abgeltung_verpaechterlasten_oekonomie', period)
        dauerkultur = person('abgeltung_verpaechterlasten_dauerkultur', period)
        wohnung = person('abgeltung_verpaechterlasten_wohnung', period)
        return boden + oekonomie + dauerkultur + wohnung
