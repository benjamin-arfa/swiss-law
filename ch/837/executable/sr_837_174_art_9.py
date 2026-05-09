"""SR 837.174 Art. 9 – Beiträge

Generated from: ch/837/de/837.174.md

Die arbeitslose Person und die Arbeitslosenversicherung tragen die
Beiträge je zur Hälfte. Während Tagen ohne Leistungsbezug übernimmt
die Arbeitslosenversicherung den ganzen Beitrag.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class erhaelt_alv_leistung_am_tag(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person erhält an diesem Tag ALV-Leistungen"
    reference = "SR 837.174 Art. 9 Abs. 2"


class bvg_beitrag_anteil_arbeitslose_person(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Anteil der arbeitslosen Person am BVG-Beitrag (CHF)"
    reference = "SR 837.174 Art. 9"

    def formula(person, period, parameters):
        import numpy as np
        beitrag = person('bvg_beitrag_arbeitslose_tag', period)
        erhaelt_leistung = person('erhaelt_alv_leistung_am_tag', period)

        # Abs. 1: Je zur Hälfte bei Leistungsbezug
        # Abs. 2: Kein Anteil der Person bei Tagen ohne Leistung
        return np.where(erhaelt_leistung, beitrag * 0.5, 0)


class bvg_beitrag_anteil_arbeitslosenversicherung(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Anteil der Arbeitslosenversicherung am BVG-Beitrag (CHF)"
    reference = "SR 837.174 Art. 9"

    def formula(person, period, parameters):
        import numpy as np
        beitrag = person('bvg_beitrag_arbeitslose_tag', period)
        erhaelt_leistung = person('erhaelt_alv_leistung_am_tag', period)

        # Abs. 1: Hälfte bei Leistungsbezug
        # Abs. 2: Ganzer Beitrag bei Tagen ohne Leistung
        return np.where(erhaelt_leistung, beitrag * 0.5, beitrag)
