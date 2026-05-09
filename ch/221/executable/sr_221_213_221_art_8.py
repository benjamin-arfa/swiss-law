"""SR 221.213.221 Art. 8 – Pachtzins für Rebboden

Generated from: ch/221/de/221.213.221.md

Der höchstzulässige Pachtzins für Rebboden setzt sich zusammen aus
dem Basispachtzins von 5.2 Prozent des Bodenertragswertes, bereinigt
aufgrund der örtlichen Verhältnisse und allfälligen betriebsbezogenen
Zuschlägen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

BASISPACHTZINS_REBBODEN_RATE = 0.052  # 5.2%


class hoechstzulaessiger_pachtzins_rebboden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Höchstzulässiger Pachtzins für Rebboden (CHF)"
    reference = "SR 221.213.221 Art. 8"

    def formula(person, period, parameters):
        import numpy as np

        bodenertragswert = person('bodenertragswert_vl4', period)
        oertl_anpassung = person('oertliche_anpassung_prozent', period)
        zuschlag_arr = person('zuschlag_arrondierung', period)
        zuschlag_lage = person('zuschlag_guenstige_lage', period)

        oertl_anpassung_clamped = np.clip(oertl_anpassung, -15, 15) / 100
        zuschlag_arr_clamped = np.clip(zuschlag_arr, 0, 15) / 100
        zuschlag_lage_clamped = np.clip(zuschlag_lage, 0, 15) / 100

        basispachtzins = bodenertragswert * BASISPACHTZINS_REBBODEN_RATE
        bereinigter_pachtzins = basispachtzins * (1 + oertl_anpassung_clamped)
        total = bereinigter_pachtzins * (1 + zuschlag_arr_clamped + zuschlag_lage_clamped)

        return total
