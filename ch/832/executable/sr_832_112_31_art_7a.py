"""SR 832.112.31 Art. 7a

Generated from: ch/832/de/832.112.31.md

Art. 7a: Beitraege (Pflegeleistungen)
- Abs. 1: Beitraege pro Stunde fuer ambulante Leistungserbringer:
  a. Abklaerung/Beratung/Koordination (Art. 7 Abs. 2 Bst. a): CHF 76.90
  b. Untersuchung/Behandlung (Art. 7 Abs. 2 Bst. b): CHF 63.00
  c. Grundpflege (Art. 7 Abs. 2 Bst. c): CHF 52.60
- Abs. 2: Verguetung in Zeiteinheiten von 5 Minuten. Mindestens 10 Min.
- Abs. 3: Beitraege pro Tag fuer Pflegeheime nach Pflegebedarfsstufen:
  a. bis 20 Min: CHF 9.60
  b. 21-40 Min: CHF 19.20
  c. 41-60 Min: CHF 28.80
  d. 61-80 Min: CHF 38.40
  e. 81-100 Min: CHF 48.00
  f. 101-120 Min: CHF 57.60
  g. 121-140 Min: CHF 67.20
  h. 141-160 Min: CHF 76.80
  i. 161-180 Min: CHF 86.40
  j. 181-200 Min: CHF 96.00
  k. 201-220 Min: CHF 105.60
  l. mehr als 220 Min: CHF 115.20
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


# --- Input variables ---

class klv_pflege_leistungstyp(Variable):
    """1=Abklaerung/Beratung, 2=Untersuchung/Behandlung, 3=Grundpflege"""
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Typ der Pflegeleistung (1=Abklaerung, 2=Behandlung, 3=Grundpflege)"
    reference = "SR 832.112.31 Art. 7a Abs. 1"


class klv_pflege_dauer_minuten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer der erbrachten Pflegeleistung in Minuten"
    reference = "SR 832.112.31 Art. 7a Abs. 2"


class klv_pflege_ist_pflegeheim(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Leistung wird in einem Pflegeheim erbracht"
    reference = "SR 832.112.31 Art. 7a Abs. 3"


class klv_pflegeheim_pflegebedarf_minuten_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taeglicher Pflegebedarf in Minuten (Pflegeheim)"
    reference = "SR 832.112.31 Art. 7a Abs. 3"


# --- Computed variables ---

class klv_pflege_beitrag_pro_stunde(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "OKP-Beitrag pro Stunde fuer ambulante Pflegeleistungen (CHF)"
    reference = "SR 832.112.31 Art. 7a Abs. 1"

    def formula(person, period, parameters):
        typ = person('klv_pflege_leistungstyp', period)
        # Art. 7a Abs. 1:
        # a. Abklaerung/Beratung/Koordination: CHF 76.90
        # b. Untersuchung/Behandlung: CHF 63.00
        # c. Grundpflege: CHF 52.60
        return select(
            [typ == 1, typ == 2, typ == 3],
            [76.90, 63.00, 52.60],
            default=0.0,
        )


class klv_pflege_verguetete_minuten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Verguetete Pflegeminuten (aufgerundet auf 5-Min-Einheiten, mind. 10 Min)"
    reference = "SR 832.112.31 Art. 7a Abs. 2"

    def formula(person, period, parameters):
        dauer = person('klv_pflege_dauer_minuten', period)
        # Abs. 2: Zeiteinheiten von 5 Min, mindestens 10 Min
        # Aufrunden auf naechstes Vielfaches von 5
        import numpy as np
        aufgerundet = np.ceil(dauer / 5.0) * 5.0
        return where(aufgerundet < 10.0, 10.0, aufgerundet)


class klv_pflege_beitrag_ambulant(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "OKP-Beitrag fuer ambulante Pflegeleistung (CHF)"
    reference = "SR 832.112.31 Art. 7a Abs. 1-2"

    def formula(person, period, parameters):
        beitrag_h = person('klv_pflege_beitrag_pro_stunde', period)
        minuten = person('klv_pflege_verguetete_minuten', period)
        ist_heim = person('klv_pflege_ist_pflegeheim', period)
        # Ambulant: Beitrag pro Stunde * verguetete Stunden
        return where(ist_heim, 0.0, beitrag_h * (minuten / 60.0))


class klv_pflegeheim_beitrag_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "OKP-Beitrag pro Tag fuer Pflegeheim nach Pflegebedarfsstufe (CHF)"
    reference = "SR 832.112.31 Art. 7a Abs. 3"

    def formula(person, period, parameters):
        bedarf = person('klv_pflegeheim_pflegebedarf_minuten_pro_tag', period)
        # Art. 7a Abs. 3: Stufentarif
        return select(
            [
                bedarf <= 20,
                (bedarf > 20) * (bedarf <= 40),
                (bedarf > 40) * (bedarf <= 60),
                (bedarf > 60) * (bedarf <= 80),
                (bedarf > 80) * (bedarf <= 100),
                (bedarf > 100) * (bedarf <= 120),
                (bedarf > 120) * (bedarf <= 140),
                (bedarf > 140) * (bedarf <= 160),
                (bedarf > 160) * (bedarf <= 180),
                (bedarf > 180) * (bedarf <= 200),
                (bedarf > 200) * (bedarf <= 220),
                bedarf > 220,
            ],
            [9.60, 19.20, 28.80, 38.40, 48.00, 57.60,
             67.20, 76.80, 86.40, 96.00, 105.60, 115.20],
            default=0.0,
        )
