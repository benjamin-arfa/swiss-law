"""SR 367.1 Art. 21

Generated from: ch/367/de/367.1.md

Allgemeine Kosten - Verteilschluessel Bund/Kantone.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class allgemeine_kosten_pti(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamte allgemeine Kosten von PTI Schweiz (ueber allg. Voranschlag finanziert)"
    reference = "SR 367.1 Art. 21 Abs. 1"


class ist_bund(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Partei der Bund"
    reference = "SR 367.1 Art. 21 Abs. 1 Bst. a"


class staendige_wohnbevoelkerung_kanton(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Staendige Wohnbevoelkerung des Kantons"
    reference = "SR 367.1 Art. 21 Abs. 1 Bst. b"


class staendige_wohnbevoelkerung_alle_kantone(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Summe der staendigen Wohnbevoelkerung aller Vereinbarungs-Kantone"
    reference = "SR 367.1 Art. 21 Abs. 1 Bst. b"


# --- Computed variables ---

class beitrag_allgemeine_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrlicher Beitrag an die allgemeinen Kosten von PTI Schweiz"
    reference = "SR 367.1 Art. 21 Abs. 1"

    def formula(person, period):
        kosten = person('allgemeine_kosten_pti', period)
        ist_b = person('ist_bund', period)
        wohnbev_kt = person('staendige_wohnbevoelkerung_kanton', period)
        wohnbev_total = person('staendige_wohnbevoelkerung_alle_kantone', period)

        # Bund traegt 30% der Kosten
        bund_anteil = kosten * 0.30

        # Kantone tragen 70%, verteilt nach Wohnbevoelkerung
        kantone_gesamt = kosten * 0.70
        kanton_anteil = where(
            wohnbev_total > 0,
            kantone_gesamt * wohnbev_kt / wohnbev_total,
            0.0
        )

        return where(ist_b, bund_anteil, kanton_anteil)
