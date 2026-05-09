"""SR 221.213.221 Art. 7 – Pachtzins für Boden (einzelne Grundstücke)

Generated from: ch/221/de/221.213.221.md

Der höchstzulässige Pachtzins für Boden setzt sich zusammen aus dem
Basispachtzins (7% des Bodenertragswertes VL4), bereinigt um örtliche
Verhältnisse (±15%), plus betriebsbezogene Zuschläge (je max 15%).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

BASISPACHTZINS_RATE = 0.07               # 7% des Bodenertragswertes VL4
MAX_OERTLICHE_ANPASSUNG = 0.15           # ±15%
MAX_BETRIEBSBEZOGENER_ZUSCHLAG = 0.15    # je max 15%


class bodenertragswert_vl4(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bodenertragswert der Verkehrslage 4 gemäss Anhang VBB (CHF)"
    reference = "SR 221.213.221 Art. 7 Abs. 2"


class oertliche_anpassung_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Örtliche Anpassung des Basispachtzinses durch kantonale Behörde (Prozent, -15 bis +15)"
    reference = "SR 221.213.221 Art. 7 Abs. 3"
    default_value = 0.0


class zuschlag_arrondierung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betriebsbezogener Zuschlag für bessere Arrondierung (Prozent, 0-15)"
    reference = "SR 221.213.221 Art. 7 Abs. 4 lit. a"
    default_value = 0.0


class zuschlag_guenstige_lage(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betriebsbezogener Zuschlag für günstige Lage (Prozent, 0-15)"
    reference = "SR 221.213.221 Art. 7 Abs. 4 lit. b"
    default_value = 0.0


class hoechstzulaessiger_pachtzins_boden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Höchstzulässiger Pachtzins für Boden einzelner Grundstücke (CHF)"
    reference = "SR 221.213.221 Art. 7"

    def formula(person, period, parameters):
        import numpy as np

        bodenertragswert = person('bodenertragswert_vl4', period)
        oertl_anpassung = person('oertliche_anpassung_prozent', period)
        zuschlag_arr = person('zuschlag_arrondierung', period)
        zuschlag_lage = person('zuschlag_guenstige_lage', period)

        # Clamp adjustments to legal limits
        oertl_anpassung_clamped = np.clip(oertl_anpassung, -15, 15) / 100
        zuschlag_arr_clamped = np.clip(zuschlag_arr, 0, 15) / 100
        zuschlag_lage_clamped = np.clip(zuschlag_lage, 0, 15) / 100

        # Abs. 2: Basispachtzins = 7% des Bodenertragswertes VL4
        basispachtzins = bodenertragswert * BASISPACHTZINS_RATE

        # Abs. 3: Bereinigung um örtliche Verhältnisse
        bereinigter_pachtzins = basispachtzins * (1 + oertl_anpassung_clamped)

        # Abs. 4: Betriebsbezogene Zuschläge
        total = bereinigter_pachtzins * (1 + zuschlag_arr_clamped + zuschlag_lage_clamped)

        return total
