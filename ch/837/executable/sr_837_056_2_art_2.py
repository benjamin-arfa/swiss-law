"""SR 837.056.2 Art. 2

Generated from: ch/837/de/837.056.2.md

Ansätze für Unterkunft am Kursort (Reimbursement rates for accommodation at
course location for unemployment insurance participants).

- Monthly accommodation: CHF 300
- Hotel (if short course/compelling reasons): 80% of costs, max CHF 80/night
- Hotel rate does NOT apply to weekly commuters (Wochenaufenthalter)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class alv_kurs_unterkunft_verguetung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "ALV-Vergütung für Unterkunft am Kursort (CHF)"
    reference = "SR 837.056.2 Art. 2"

    def formula_2003_07(person, period, parameters):
        import numpy as np

        braucht_hotel = person('alv_kurs_hotel_noetig', period)
        ist_wochenaufenthalter = person('alv_kurs_wochenaufenthalter', period)
        hotel_kosten_pro_nacht = person('alv_kurs_hotel_kosten_pro_nacht', period)
        uebernachtungen = person('alv_kurs_uebernachtungen_im_monat', period)

        p = parameters(period).sr837_056_2.unterkunft
        monatspauschale = p.monatspauschale
        hotel_anteil = p.hotel_kostenanteil
        hotel_max = p.hotel_max_pro_nacht

        # Hotel reimbursement: 80% of actual cost, max CHF 80/night
        hotel_verguetung_pro_nacht = np.minimum(
            hotel_kosten_pro_nacht * hotel_anteil,
            hotel_max
        )
        hotel_total = hotel_verguetung_pro_nacht * uebernachtungen

        # Hotel rate does not apply to weekly commuters (Art. 2 Abs. 3)
        hotel_berechtigt = braucht_hotel * (1 - ist_wochenaufenthalter)

        return np.where(
            hotel_berechtigt,
            hotel_total,
            monatspauschale
        )


class alv_kurs_hotel_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Auf Hotelunterkunft angewiesen (kurze Kursdauer oder andere zwingende Gründe)"
    reference = "SR 837.056.2 Art. 2 Abs. 2"


class alv_kurs_wochenaufenthalter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist Wochenaufenthalter/in"
    reference = "SR 837.056.2 Art. 2 Abs. 3"


class alv_kurs_hotel_kosten_pro_nacht(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachgewiesene Hotelkosten pro Übernachtung (CHF)"
    reference = "SR 837.056.2 Art. 2 Abs. 2"


class alv_kurs_uebernachtungen_im_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Übernachtungen im Monat"
    reference = "SR 837.056.2 Art. 2 Abs. 2"
